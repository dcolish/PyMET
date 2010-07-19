from pprint import PrettyPrinter

from  base import Trimet


class Route(Trimet):
    """route times and location attrs"""
    arg_schema = ['locIDs']
    result_schema = [u'errorMessage', u'route',
                     u'dir', u'stop']

    def __init__(self):
        self.command_name = u'route'
        super(Trimet, self).__init__()

    def __repr__(self):
        return str({'route': foo.route,
                    'dir': foo.dir,
                    'stop': foo.stop})


if __name__ == "__main__":
    foo = Route()
    foo.fetch({'locIDs': 1927})
    pp = PrettyPrinter(indent=4)
    pp.pprint(foo)
