from pprint import PrettyPrinter

from base import Trimet


class Arrivals(Trimet):
    """arrival times and location attrs"""
    command_name = u'arrivals'
    arg_schema = ['locIDs']
    result_schema = [u'errorMessage', u'location',
                     u'arrival', 'blockPosition', u'trip', u'layover',
                     u'routeStatus']

    def __repr__(self):
        return str({'locations': foo.locations,
                    'arrivals': foo.arrivals})


if __name__ == "__main__":
    foo = Arrivals()
    foo.fetch({'locIDs': [1927]})
    pp = PrettyPrinter(indent=4)
    pp.pprint(foo)
