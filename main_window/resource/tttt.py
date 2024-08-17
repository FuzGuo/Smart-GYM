import matplotlib.pyplot as plt

# Optimized dropout rates and corresponding F1 scores
dropout_rates = [0.1, 0.2, 0.3, 0.4, 0.5]
f1_scores = [85.32, 90.81, 89.67, 87.54, 88.45]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(dropout_rates, f1_scores, marker='o', linestyle='-', color='orange')

# Add title and labels
plt.title('Relationship between Dropout Rate and F1 Score')
plt.xlabel('Dropout Rate')
plt.ylabel('F1 Score')

# Set y-axis range
plt.ylim(80, 100)

# Display grid
plt.grid(True)

# Show the plot
plt.show()