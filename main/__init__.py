import os
from transformers import pipeline



def get_model():
    try:
        model = pipeline(
            "sentiment-analysis",
            model="model/pipe/",
            tokenizer="model/pipe/"
        )
        return model

    except KeyError:
        raise Exception("Model not found")