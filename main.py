import sys
sys.path.insert(1, './Global')
sys.path.insert(2, './Classes')

import time

from reqType import requestType
from Request import Request
from BikeDataCache import BikeDataCache

cache = BikeDataCache(5)
cache.debug()

time.sleep(2)
cache.update()
cache.debug()

time.sleep(15)
cache.update()
cache.debug()

