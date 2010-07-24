"""repsresentation of arrivals"""

from base import Trimet


class Arrivals(Trimet):
    """arrival times and location attrs"""
    command_name = u'arrivals'
    arg_schema = ['locIDs']
    result_schema = [u'errorMessage', u'location',
                     u'arrival', u'routeStatus']

    def load(self, locations):
        """takes a list of location ids"""
        try:
            assert isinstance(locations, list)
            super(Arrivals, self).load({'locIDs': locations})
        except AssertionError:
            print "Locations must be a list"


class Detours(Trimet):
    """Detour information per route"""
    command_name = u'detours'
    arg_schema = [u'routes']
    result_schema = [u'errorMessage', u'detour']

    def load(self, routes):
        """given a list of routes returns detours"""
        try:
            assert isinstance(routes, list)
            super(Detours, self).load({'routes': routes})
        except AssertionError:
            print "Routes must be a list"


class TripPlanner(Trimet):
    """plan a trip somewhere"""
    command_name = u'trips/tripplanner'
    arg_schema = [u'fromPlace', u'fromCoord', u'toPlace', u'toCoord',
                  u'Date', u'Time', u'Min', u'Arr', u'Walk', u'Mode',
                  u'Format', u'MaxIntineraries']
    result_schema = [u'date', u'time', u'request', u'from', u'to',
                     u'itinerary', u'location', u'fromList',
                     u'toList', u'error']

    def load(self, fromPlace=None, fromCoord=None, toPlace=None,
             toCoord=None, Date=None, Time=None, Min=None, Arr=None,
             Walk=None, Mode=None, Format='XML', MaxIntineraries=3):
        """plans a trip"""
        super(TripPlanner, self).load(dict(
                fromPlace=fromPlace, fromCoord=fromCoord,
                toPlace=toPlace, toCoord=toCoord,
                Date=Date, Time=Time, Min=Min,
                Arr=Arr, Walk=Walk, Mode=Mode,
                Format='XML', MaxIntineraries=3))


if __name__ == "__main__":
    AR = Arrivals()
    AR.load(locations=[1927])
    print AR

    DT = Detours()
    DT.load(routes=[1927, 12963])
    print DT

    TP = TripPlanner()
    TP.load(fromPlace='airport', toPlace='pioneer square',
            Time='5:00pm')
    print TP
