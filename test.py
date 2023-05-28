import numpy as np
from sklearn.neighbors import NearestNeighbors

samples = [[100,0]]
model=NearestNeighbors(n_neighbors=2)
model.fit(samples)

samples2 = [[0,2],[1,0],[0,1]]
model.fit(samples2)
print(model.kneighbors([[100,1]],n_neighbors=1))