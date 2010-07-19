from itertools import chain
from urllib2 import urlopen

from BeautifulSoup import BeautifulStoneSoup
from inflect import engine


class LazyApi(object):
    """lazy xml api class"""
    _attrs = {}

    def __getattr__(self, name):
        """once we have fetched an object we can check for attrs"""
        p = engine()
        items = []
        for x in self._attrs:
            key, value = x.items().pop()
            if key == p.sinoun(name) or key == name:
                items.append(value)
        return items

    def urlize(self, iterarg):
        # x must be a key
        foo = []
        for x, y in iterarg:
            if isinstance(y, list):
                y = ','.join(map(str, y))
            foo.append('/'.join([x, str(y)]))
        return '/'.join(foo)


class Trimet(LazyApi):
    appID = "32208AFFFAA63FAEEBE5CB299"
    base_url = "http://developer.trimet.org/ws/V1"
    _methods = [u"route", u"dir", u"stop", u"arrivals", u"detour"]
    command_name = ''
    arg_schema = result_schema = []

    def __init__(self):
        try:
            assert self.command_name in self._methods
        except Exception:
            print "You must specify a command method from %s" % (
                self._methods)

    def fetch(self, params):
        # validate we have an arg schema and the params match
        assert self.arg_schema
        assert all(x in  self.arg_schema for x in params.keys())

        arg_iter = chain([('', self.command_name)], params.items(),
                         [('appID', self.appID)])

        formatted_params = self.urlize(arg_iter)
        root = self.base_url + formatted_params
        resp = urlopen(root)

        if resp.code == 200:
            results = BeautifulStoneSoup(resp.read())
            resp.close()

            self._attrs = [{item.name: dict(item.attrs)}
                           for item in results.resultset.childGenerator()
                           if item.name in self.result_schema]
        else:
            resp.close()
            raise Exception
