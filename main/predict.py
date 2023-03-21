from main import get_model
from transformers import pipeline


def main(question):
    pipeline = get_model()
    prediction = pipeline(question)
    print(prediction)

    label = prediction[0]['label']
    score = prediction[0]['score']

    return label, score