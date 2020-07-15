import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer


dataset = pd.read_csv("datasets/Data.csv")
#  print(dataset)
X = dataset.iloc[ : , -1].values
Y = dataset.iloc[ : , 3].values


imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(X[ : , 1:3])
