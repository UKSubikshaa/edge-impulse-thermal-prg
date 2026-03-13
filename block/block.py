import pickle
import numpy as np

# Load the trained model
with open("block/edge_ai_model.pkl", "rb") as f:
    model = pickle.load(f)


def process(input, config):

    # Convert input data to numpy
    data = np.array(input)

    # Run model prediction
    prediction = model.predict([data])

    # Return result to Edge Impulse
    return {
        "features": prediction.tolist()
    }
