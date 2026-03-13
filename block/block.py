import pickle
import numpy as np

with open("block/edge_ai_model.pkl", "rb") as f:
    model = pickle.load(f)

def process(input, config):

    data = np.array(input)

    prediction = model.predict([data])

    return {
        "features": prediction.tolist()
    }
