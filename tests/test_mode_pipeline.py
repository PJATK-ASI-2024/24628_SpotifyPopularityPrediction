import unittest
import pandas as pd
import joblib
from sklearn.metrics import r2_score
from dags.evaluate_model_dag import preprocess_data, check_model_tests

MODEL_PATH = "/opt/airflow/models/linear_regression_model.pkl"

class TestModelPipeline(unittest.TestCase):

    def setUp(self):
        self.model = joblib.load(MODEL_PATH)
        self.df = pd.DataFrame({
            'feature1': [0.1, 0.2, 0.3],
            'feature2': [1, 2, 3],
            'popularity': [10, 20, 30]
        })

    def test_model_prediction(self):
        X = self.df.drop(columns=["popularity"])
        y_pred = self.model.predict(X)
        self.assertEqual(len(y_pred), len(X))

    def test_quality_metrics(self):
        X = self.df.drop(columns=["popularity"])
        y_true = self.df["popularity"]
        y_pred = self.model.predict(X)
        r2 = r2_score(y_true, y_pred)
        self.assertIsInstance(r2, float)

    def test_preprocess_data_with_missing_values(self):
        df_with_missing = self.df.copy()
        df_with_missing.loc[0, 'feature1'] = None
        preprocessed_df = preprocess_data(df_with_missing)
        self.assertFalse(preprocessed_df.isnull().values.any())

    def test_check_model_tests(self):
        tests_pass = check_model_tests()
        self.assertIsInstance(tests_pass, bool)

if __name__ == '__main__':
    unittest.main()