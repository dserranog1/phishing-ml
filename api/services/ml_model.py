from joblib import load
from django.conf import settings
import pandas as pd


def predict_with_model(features):
    model = load(
        settings.BASE_DIR / "ml-models" / "tuned_random_forest_classifier.joblib"
    )
    features_df = pd.DataFrame([features])
    return float(model.predict(features_df)[0]), float(
        model.predict_proba(features_df)[:, 1] * 100
    )
