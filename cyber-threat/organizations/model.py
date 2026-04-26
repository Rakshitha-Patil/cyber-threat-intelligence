import numpy as np
from sklearn.linear_model import LogisticRegression

def train_model():
    # Simulated training data (like network logs)
    # Features: [src_bytes, dst_bytes, count, srv_count]
    
    X = np.array([
        [100, 200, 1, 1],
        [3000, 100, 10, 5],
        [50, 50, 1, 1],
        [5000, 10, 20, 10],
        [200, 300, 2, 2],
        [7000, 5, 30, 15]
    ])

    # Labels: 0 = Normal, 1 = Threat
    y = np.array([0, 1, 0, 1, 0, 1])

    model = LogisticRegression()
    model.fit(X, y)

    return model