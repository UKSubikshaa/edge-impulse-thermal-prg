import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def process(input, config):

    # Convert incoming data to numpy array
    data = np.array(input)

    # Run model prediction
    prediction = model.predict([data])

    return {
        "features": prediction.tolist()
    }
