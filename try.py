
import numpy as np	
from sklearn import svm
#from sklearn import LinearRegression
from sklearn import linear_model
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from itertools import islice

#Xd = X[:,1:].T
#lb = np.array(statc)
#datums = query + 'data.txt'
settings = np.seterr(all='ignore')

Xd = np.genfromtxt('Appledata.txt')
lbs = np.genfromtxt('Applelab.txt')
#Xd = Xds.T 
lb = lbs.T

#Xd = Xds.T
Xd += 1.0
print Xd
print lb
#return y
n_samples = 56 * 5

clf = linear_model.Ridge(alpha=.05)
clf.fit(Xd[:n_samples / 1.25], lbs[:n_samples / 1.25])
expected = lb[n_samples / .8:]
predicted = clf.predict(Xd[n_samples / .8:])


print(explained_variance_score(expected, predicted))
print(mean_absolute_error(expected, predicted))
print(mean_squared_error(expected, predicted))
print(r2_score(expected, predicted))
pred = np.array([[.15914],[.164299],[.1983024],[7.0589],[7.13570057],[7.016397]])
pred += 1.0

print(clf.predict(pred.T))
