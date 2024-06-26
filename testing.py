import random
import pandas as pd

# Example user interaction data
data = {
    'user_id': [1, 2, 3, 1, 2, 3],
    'item_id': [101, 102, 103, 104, 105, 106],
    'interaction': [5, 3, 4, 2, 5, 1]
}
df = pd.DataFrame(data)

# Split users into groups A and B
df['group'] = df['user_id'].apply(lambda x: 'A' if random.random() < 0.5 else 'B')

# Function to track user interactions
def track_interaction(user_id, item_id, interaction, group):
    print(f"User {user_id} in group {group} interacted with item {item_id} with interaction {interaction}")

# Example tracking
for _, row in df.iterrows():
    track_interaction(row['user_id'], row['item_id'], row['interaction'], row['group'])
