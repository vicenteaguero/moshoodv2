from sklearn.datasets import load_iris
import pandas as pd


def prepare_dataset() -> pd.DataFrame:
    """
    Prepare the Iris dataset.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the Iris dataset with renamed columns.

    """
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


def subseting_dataset(data: pd.DataFrame) -> pd.DataFrame:
    """
    Subset the dataset based on specific conditions.

    Args:
        data (pd.DataFrame): The input pandas DataFrame containing the dataset.

    Returns:
        pd.DataFrame: A subset of the input DataFrame that meets the specified conditions.

    """
    data = data[data["sepal_length"] > 5]
    data = data[(data["sepal_width"] < 4) & (data["sepal_width"] > 2.5)]
    data = data[data["petal_length"] > 2]
    data = data[(data["petal_width"] > 0.5) & (data["petal_width"] < 2)]
    return data

def load_dataset() -> pd.DataFrame:
    """
    Load and subset the dataset.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the subset of the Iris dataset.
    """
    dataset = prepare_dataset()
    return subseting_dataset(data=dataset)

if __name__ == "__main__":
    ...