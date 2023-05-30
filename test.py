import sys
sys.path.insert(1, './Classes')
sys.path.insert(2, './Global')

from reqType import requestType
from ModelBank import ModelBank
from Request import Request
from RoutingReq import RoutingRequest

bank = ModelBank()
testReq = Request(-118.48155,33.99556,'docking')

startLoc = {
    'lat':-118.48155,  
    'long': 33.99556
}
endLoc = {
    'lat':-118.27917,
    'long':34.02371
}
testRouting = RoutingRequest(startLoc,endLoc)
print(bank.predict(testRouting))
