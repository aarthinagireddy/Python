import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

train = pd.read_csv('train.csv')
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

print(train.SalePrice.describe())

data = train.select_dtypes(include=[np.number]).interpolate().dropna()
print(sum(data.isnull().sum() != 0))

numeric_features = train.select_dtypes(include=[np.number])
corr = numeric_features.corr()

print(corr['SalePrice'].sort_values(ascending=False)[:5], '\n')
print(corr['SalePrice'].sort_values(ascending=False)[-5:])


y = np.log(data.SalePrice)
x = data.drop(['SalePrice'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=42,test_size=.33)

lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
prediction  = model.predict(X_test)

print ("R^2 is: \n", model.score(X_test, y_test))
print ('RMSE is: \n', mean_squared_error(y_test, prediction))

plt.scatter(prediction, y_test, alpha=.75, color='b')
plt.xlabel('Prediction')
plt.ylabel('Actual')
plt.title('Multiple Regression Model')
plt.show()

