class Stations:
    #coords
    #property

    def __init__(self,raw) -> None:
        rawCoords = raw['geometry']['coordinates']
        self.coords = {
            'lat': rawCoords[1],
            'long': rawCoords[0]
        }

        rawProperty = raw['properties']
        self.utilAvailable = {
            'bikesAvailable': rawProperty['bikesAvailable'],
            'docksAvailable': rawProperty['docksAvailable']
        }

        self.name = raw['properties']['name']

    def debug(self):
        print(self.coords)
        print(self.utilAvailable)
        print(self.name)