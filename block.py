import pickle
import numpy as np

# Load the trained model
with open(import pickle
import numpy as np

with open("edge_ai_model.pkl", "rb") as f:
    model = pickle.load(f)

def process(input, config):

    data = np.array(input)

    prediction = model.predict([data])

    return {
        "features": prediction.tolist()
    }
    # Convert incoming data to numpy array
    data = np.array(input)

    # Run model prediction
    prediction = model.predict([data])

    return {
        "features": prediction.tolist()
    }
