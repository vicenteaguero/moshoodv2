from sklearn.datasets import load_iris
import pandas as pd


def prepare_dataset():
    data = pd.DataFrame(load_iris().data, columns=load_iris().feature_names)
    data["target"] = load_iris().target
    data.rename(
        columns={
            "sepal length (cm)": "sepal_length",
            "sepal width (cm)": "sepal_width",
            "petal length (cm)": "petal_length",
            "petal width (cm)": "petal_width",
        },
        inplace=True,
    )
    return data


def subseting_dataset(data):
    data = data[data["sepal_length"] > 5]
    data = data[(data["sepal_width"] < 4) & (data["sepal_width"] > 2.5)]
    data = data[data["petal_length"] > 2]
    data = data[(data["petal_width"] > 0.5) & (data["petal_width"] < 2)]
    return data


dataset = prepare_dataset()
subset_data = subseting_dataset(data=dataset)
print(subset_data.head())
print(subset_data.target.nunique())
