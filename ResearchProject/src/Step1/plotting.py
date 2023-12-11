from feature_analysis import gen_accuracies
import matplotlib.pyplot as plt

sorted_accuracies = gen_accuracies()
models, accuracies = zip(*sorted_accuracies)

# Plotting the accuracies
plt.figure(figsize=(10, 6))
plt.bar(models, accuracies, color='skyblue')
plt.title('Model Accuracies')
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.ylim(0, 1)  # Set y-axis limit between 0 and 1 for accuracy values
plt.xticks(rotation=25, ha='right')  # Rotate x-axis labels for better readability
plt.show()