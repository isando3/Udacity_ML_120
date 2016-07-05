# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 18:24:30 2016

@author: isando3
"""


#import libraries 
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.linear_model import SGDClassifier

#additional plotting tools
def Draw(pred, features,  name="iris.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][1], features[ii][2], color = colors[pred[ii]])
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()




#loading the sample data from the built-in datasets
iris = datasets.load_iris()
iris_X = iris.data

iris_Y = iris.target
##print iris_X, iris_Y

#visual inspection of the data
#APPLY HERE THE METHOD LEARNED IN THE BOOK

#run a knn classification 
np.random.seed(10)
indices = np.random.permutation(len(iris_X))
#train 
iris_X_train = iris_X[indices[:-10]]
print iris_X_train
iris_Y_train = iris_Y[indices[:-10]]
print iris_Y_train
iris_X_test = iris_X[indices[-10:]]
iris_Y_test = iris_Y[indices[-10:]]

#print iris_X_test, iris_Y_test


#Use knn to classify the data
from sklearn.neighbors import KNeighborsClassifier
#declare clf 
knn = KNeighborsClassifier()
#fit clf
knn.fit(iris_X_train, iris_Y_train)
#predict using clf
pred =knn.predict(iris_X_test)
#get the score of the classifier
print knn.score(iris_X_test, pred)
#Draw(pred,iris_X_test, name="iris_clusters.pdf")

#let's test the best variables in the set 
X_indices = np.arange(iris_X_train.shape[-1])
selector = SelectPercentile(f_classif, percentile=10)
selector.fit(iris_X_train, iris_Y_train)
print -np.log10(selector.pvalues_), selector.pvalues_

scores = -np.log10(selector.pvalues_)
scores /= scores.max()
#plt.bar(X_indices - .45, scores, width=.2,
        #label=r'Univariate score ($-Log(p_{value})$)', color='g')

red_X = iris.data[:,:2]
red_y = iris.target
colors = "bry"

#standarize
#mean= red_X.mean(axis=0)
#std = red_X.std(axis=0)
#red_X = (red_X- mean)/std
h = 0.2 #step in mesh
clf = SGDClassifier(alpha=0.001, n_iter=100).fit(red_X, red_y)

# create a mesh to plot in
x_min, x_max = red_X[:, 0].min() - 1, red_X[:, 0].max() + 1
y_min, y_max = red_X[:, 1].min() - 1, red_X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, m_max]x[y_min, y_max].
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
# Put the result into a color plot
Z = Z.reshape(xx.shape)
cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
plt.axis('tight')

# Plot also the training points
for i, color in zip(clf.classes_, colors):
    idx = np.where(red_y == i)
    plt.scatter(red_X[idx, 0], red_X[idx, 1], c=color, label=iris.target_names[i],
                cmap=plt.cm.Paired)
plt.title("Decision surface of multi-class SGD")
plt.axis('tight')

# Plot the three one-against-all classifiers
xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
coef = clf.coef_
intercept = clf.intercept_
def plot_hyperplane(c, color):
    def line(x0):
        return (-(x0 * coef[c, 0]) - intercept[c]) / coef[c, 1]

    plt.plot([xmin, xmax], [line(xmin), line(xmax)],
             ls="--", color=color)

for i, color in zip(clf.classes_, colors):
    plot_hyperplane(i, color)
plt.legend()
plt.show()




