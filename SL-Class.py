
from sklearn import tree #import scikit-learn library 
# 0=Bumpy 1=Smooth
xfeatures = [[140, 1], [130, 1], [150, 0], [170, 0]]
# 0=Apple 1=Orange
ylabels = [0,0,1,1]

# Fit Classifier
dtClf = tree.DecisionTreeClassifier()
dtClf = dtClf.fit(xfeatures,ylabels)


print dtClf.predict([[170,0]])


#Google Developers Recipe
