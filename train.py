import pandas as pd
# from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np

df = pd.read_csv("data/train.csv")
X = df.drop(columns=['Disease']).to_numpy()
y = df['Disease'].to_numpy()
labels = np.sort(np.unique(y)
y = np.array([np.where(labels == x) for x in y]).flatten()

model = RandomForestClassifier(max_features=1, n_estimators=200, min_samples_leaf=4, min_samples_split = 8, random_state=42).fit(X, y)

with open("model.pkl", 'wb') as f:
    pickle.dump(model, f)
