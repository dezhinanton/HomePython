import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

one_hot_data = pd.get_dummies(data['whoAmI'])
one_hot_data.index = data.index

data = pd.concat([data, one_hot_data], axis=1)

print(data.head())
