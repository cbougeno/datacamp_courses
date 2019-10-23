# Supervised learning
The goal is frequently:
+ Automate time-consuming or expensive manual tasks
+ Make predictions about future
+ Need labeled data
---
## Classification
+ Target variable consists of categories
### K-nearest Neighbors
+ Basic idea: Predict the label of a data point by
    + Looking the 'k' closest labeled data points
    + Taking a majority vote
    + No missing data on DataFrame
    
```python
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
dataframe = pd.DataFrame()
X_new = dataframe['new']
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(dataframe['data'], dataframe['target'])
    
prediction = knn.predict(X_new)
```
## Regression
+ Target variable is continuous (like price of a house) 
---
# Naming Convetions
+ Features = predictor variables = independent variables
+ Target variables = dependent variables = response variable
---
# Global
+ It's necessary split the data on train and test
```python
from sklearn.model_selection import train_test_split
import pandas as pd
X = pd.DataFrame()
y = pd.DataFrame()

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)
```