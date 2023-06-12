from Request import Request

class RoutingRequest:
    def __init__(self, startLoc, endLoc, slots):
        self.reqType='routing'
        self.locations={
            'startLoc': Request(startLoc['lat'],startLoc['long'],'renting',slots,k=10),
            'endLoc': Request(endLoc['lat'],endLoc['long'],'docking',slots,k=10)
        }
        self.slots=slots
