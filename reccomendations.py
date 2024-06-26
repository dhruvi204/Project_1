import tensorflow as tf
from tensorflow.keras.layers import Embedding, Dot, Flatten, Input
from tensorflow.keras.models import Model
import pandas as pd

# Example user interaction data
data = {
    'user_id': [1, 2, 3, 1, 2, 3],
    'item_id': [101, 102, 103, 104, 105, 106],
    'interaction': [5, 3, 4, 2, 5, 1]
}
df = pd.DataFrame(data)

# Data Preprocessing
user_ids = df['user_id'].values
item_ids = df['item_id'].values
interactions = df['interaction'].values

# Model definition
user_input = Input(shape=(1,))
item_input = Input(shape=(1,))

user_embedding = Embedding(input_dim=1000, output_dim=50)(user_input)
item_embedding = Embedding(input_dim=1000, output_dim=50)(item_input)

dot_product = Dot(axes=2)([user_embedding, item_embedding])
dot_product = Flatten()(dot_product)

model = Model(inputs=[user_input, item_input], outputs=dot_product)
model.compile(optimizer='adam', loss='mse')

# Training the model
model.fit([user_ids, item_ids], interactions, epochs=5)

# Save the model
model.save('recommendation_model.h5')
