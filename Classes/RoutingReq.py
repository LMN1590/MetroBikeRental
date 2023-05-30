from Request import Request

class RoutingRequest:
    def __init__(self, startLoc, endLoc, slots):
        self.reqType='routing'
        self.locations={
            'startLoc': Request(startLoc['lat'],startLoc['long'],'renting',slots),
            'endLoc': Request(endLoc['lat'],endLoc['long'],'docking',slots)
        }
        self.slots=slots
