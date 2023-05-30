class Request:

    def __init__(self,lat,long,reqType,slots,k=1) -> None:
        self.coords={
            "lat": lat,
            "long": long
        }
        self.slots=slots
        self.k=k
        self.reqType=reqType

    def debug(self):
        print(self.coords)
        print(self.reqType)