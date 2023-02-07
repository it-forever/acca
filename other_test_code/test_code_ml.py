from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

X, y = make_blobs(n_samples=1000, centers=2, n_features=2, random_state=42, cluster_std=7)
plt.scatter(X[:,0], X[:,1],c=y)