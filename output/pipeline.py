from IPython.display import display

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.dummy import DummyClassifier
from sklearn import metrics

import pandas as pd

from dataset import load_dataset

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
        """
        Start the pipeline
        """
        try:
            self.models = [eval(model)() for model in self.models]
        except NameError:
            raise NameError('Model not found')
        self._split_train_test()

    def _split_train_test(self) -> None:
        """
        Split the data into train and test
        """
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.data.drop(columns=['target']),
            self.data['target'],
            test_size=0.2,
            random_state=42
        )

    def fit(self) -> None:
        """
        Fit the models
        """
        for model in self.models:
            model.fit(self.X_train, self.y_train)

    def predict(self) -> pd.DataFrame:
        """
        Predict the models
        """
        self.predictions = {}
        for model in self.models:
            self.predictions[model.__class__.__name__] = model.predict(self.X_test)
        self._compute_scores()

    def _compute_scores(self) -> None:
        self.scores = dict()
        for model in self.models:
            self.scores[model.__class__.__name__] = [metrics.accuracy_score(
                self.y_test,
                self.predictions[model.__class__.__name__],
            )]

    def summary(self) -> pd.DataFrame:
        """
        Summary of the models
        """
        display((
            pd
            .DataFrame(self.scores, index=['Accuracy Score'])
            .T
            .sort_values('Accuracy Score', ascending=False)
        ))

if __name__ == "__main__":
    models = [
        'RandomForestClassifier', 'KNeighborsClassifier', 'DummyClassifier'
    ]
    dataset = load_dataset()
    pipe = Pipeline(models=models, data=dataset)
    pipe.fit()
    pipe.predict()
    pipe.summary()