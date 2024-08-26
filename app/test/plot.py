import matplotlib.pyplot as plt
import numpy as np

def plot_risk_over_time(high, high_t, low, low_t):
    plt.figure(figsize=(10, 6))
    plt.plot(high_t, high, label="High Risk", color='red')
    plt.plot(low_t, low, label="Low Risk", color='green')
    plt.xlabel("Time (seconds)")
    plt.ylabel("Accuracy (%)")
    plt.title("Risk Classification Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

# You can call this function to generate the graph:
plot_risk_over_time(high, high_t, low, low_t)