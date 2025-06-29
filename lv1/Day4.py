# ------------------------------
# 🧠 List – Ordered, Mutable
# ------------------------------
features = [3.5, 2.1, 5.7, 1.2]  # Stores multiple ML features
features.append(4.9)             # Adds a new value to the end
print("Features List:", features)  # Print full list
print("3rd feature:", features[2])  # Indexing starts from 0

# ------------------------------
# 🧠 Tuple – Ordered, Immutable
# ------------------------------
shape = (28, 28)  # Example: Image dimensions (e.g., MNIST)
print("Image shape:", shape)

# ------------------------------
# 🧠 Set – Unordered, Unique items only
# ------------------------------
labels = [1, 2, 3, 2, 3, 4, 1, 5]
unique_labels = set(labels)  # Removes duplicates
print("Unique Labels:", unique_labels)

# ------------------------------
# 🧠 Dictionary – Key:Value pairs (Like JSON)
# ------------------------------
model_config = {
    "learning_rate": 0.01,
    "epochs": 20,
    "activation": "relu"
}
print("Model Config:", model_config)
print("Learning Rate:", model_config["learning_rate"])  # Access using key

# ------------------------------
# Bonus: Dictionary with list values
# ------------------------------
student_scores = {
    "Suman": [90, 87, 85],
    "Ravi": [78, 81, 84]
}
print("Suman's Scores:", student_scores["Suman"])
