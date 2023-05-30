samples = []
from sklearn.neighbors import NearestNeighbors
neigh = NearestNeighbors(n_neighbors=1)
neigh.fit(samples)
#print(neigh.kneighbors([[1., 1., 1.]],n_neighbors=1))