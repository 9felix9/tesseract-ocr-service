import glob
import os
from datetime import datetime

import joblib
from joblib import dump
from sklearn.pipeline import Pipeline
from src.settings import settings


class InferenceError(Exception):
    pass


def load_latest_model(sub_dir="") -> Pipeline:
    list_of_files = glob.glob(f'{"trained_models"}/{sub_dir}/*.joblib')
    if not list_of_files:
        raise InferenceError("No model found.")
    latest_file = max(list_of_files, key=os.path.getctime)
    return joblib.load(latest_file)


def save_model(model, name, prefix="", base_dir="", sub_dir=""):
    model_path = f"{base_dir}{settings.MODEL_PATH}/{sub_dir}/{prefix}{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}-{name}-model.joblib"
    dump(model, model_path)
    return model_path
