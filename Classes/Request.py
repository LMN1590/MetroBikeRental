class Request:
    #coords
    #type


    def __init__(self,lat,long,reqType) -> None:
        self.coords={
            "lat": lat,
            "long": long
        }
        self.reqType=reqType

    def debug(self):
        print(self.coords)
        print(self.reqType)