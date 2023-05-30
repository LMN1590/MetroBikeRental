from Request import Request

class RoutingRequest:
    def __init__(self, startLoc, endLoc):
        self.reqType='routing'
        self.locations={
            'startLoc': Request(startLoc['lat'],startLoc['long'],'renting'),
            'endLoc': Request(endLoc['lat'],endLoc['long'],'docking')
        }
