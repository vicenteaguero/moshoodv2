from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.dummy import DummyClassifier
from sklearn import metrics

import pandas as pd

class Pipeline:

    def __init__(
            self,
            models: list = ['RandomForestClassifier'],
            data: pd.DataFrame = None
        ) -> None:
        self.models = models
        self.data = data
        self._start()

    def _start(self) -> pd.DataFrame:
        self.models = [eval(model)() for model in self.models]

    def split_train_test(self) -> None:
        ...

    def fit(self) -> None:
        for model in self.models:
            model.fit(self.X_train, self.y_train)

    def predict(self) -> pd.DataFrame:
        ...

    def summary(self) -> pd.DataFrame:
        ...

if __name__ == "__main__":
    pipe = Pipeline()