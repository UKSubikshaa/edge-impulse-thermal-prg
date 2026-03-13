import pickle
import numpy as np

# Load the trained model
with open("block/edge_ai_model.pkl", "rb") as f:
    model = pickle.load(f)

def process(input, config):
    
    # Convert input to numpy array
    data = np.array(input)

    # Run prediction
    prediction = model.predict([data])

    return {
        "features": prediction.tolist()
    }
