"""
Base classes for Trimet API
"""
from itertools import chain
from json import JSONEncoder
from pprint import PrettyPrinter
from urllib2 import urlopen

from BeautifulSoup import BeautifulStoneSoup
from inflect import engine


def urlize(iterarg):
    """builds proper url from tuple/key,val argument iterator"""
    url = []
    for key, val in iterarg:
        if isinstance(val, list):
            val = ','.join(str(it) for it in val)
        url.append('/'.join([key, str(val)]))
    return '/'.join(url)


def fetch(root):
    """Takes a url and returns response"""
    resp = urlopen(root)

    if resp.code == 200:
        results = BeautifulStoneSoup(resp.read())
        resp.close()
        return results
    else:
        resp.close()
        raise Exception


class LazyApi(object):
    """lazy xml api class"""
    _attrs = {}
    arg_schema = result_schema = []

    @property
    def __dict__(self):
        inflecter = engine()
        return dict([(inflecter.plnoun(key), getattr(self, key))
                     for key in self.result_schema])

    def __getattr__(self, name):
        """once we have fetched an object we can check for attrs"""
        inflecter = engine()
        items = []
        for attr in self._attrs:
            key, value = attr.items().pop()
            if key == inflecter.sinoun(name) or key == name:
                items.append(value)
        return items

    def __str__(self):
        printer = PrettyPrinter(indent=4)
        printer.pprint(self.__dict__)
        return ''

    def json_encode(self):
        """Converts local instance to JSON"""
        return JSONEncoder().encode(self)

    def map_schema(self, results):
        """convert resultset to a list of dictionaries of dictionaries"""
        try:
            assert self.result_schema
            attrs = []
            for item in results.resultset.childGenerator():
                if item.name in self.result_schema:
                    attrs.append({item.name: dict(item.attrs)})
            return attrs
        except AssertionError:
            print "Result schema does not match results"
            raise AssertionError


class Trimet(LazyApi):
    """Base class for building out specific method classes"""
    appID = "32208AFFFAA63FAEEBE5CB299"
    base_url = "http://developer.trimet.org/ws/V1"
    _methods = [u"route", u"dir", u"stop", u"arrivals", u"detour"]
    command_name = ''

    def __init__(self):
        try:
            assert self.command_name in self._methods
            super(Trimet, self).__init__()
        except AssertionError:
            print "You must specify a command method from %s" % (
                self._methods)
            raise AssertionError

    def load(self, params):
        """loads data from api into local instance"""
        # validate we have an arg schema and the params match
        assert self.arg_schema
        assert all(x in  self.arg_schema for x in params.keys())

        arg_iter = chain([('', self.command_name)], params.items(),
                         [('appID', self.appID)])

        formatted_params = urlize(arg_iter)
        root = self.base_url + formatted_params
        results = fetch(root)
        self._attrs = self.map_schema(results)
