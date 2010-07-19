"""repsresentation of arrivals"""

from base import Trimet


class Arrivals(Trimet):
    """arrival times and location attrs"""
    command_name = u'arrivals'
    arg_schema = ['locIDs']
    result_schema = [u'errorMessage', u'location',
                     u'arrival', u'blockPosition',
                     u'trip', u'layover',
                     u'routeStatus']

    def load(self, locations):
        """takes a list of location ids"""
        try:
            assert isinstance(locations, list)
            super(Arrivals, self).load({'locIDs': locations})
        except AssertionError:
            print "Locations must be a list"

if __name__ == "__main__":
    AR = Arrivals()
    AR.load(locations=[1927, 12963])
    print AR
