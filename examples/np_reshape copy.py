'''
A classic real-world application for np.reshape is flattening a multi-dimensional matrix into a 1D vector (or vice versa) for Machine Learning model compatibility.Many machine learning libraries (like Scikit-Learn) require input data to be structured as a flat, 2D table where each row is a single sample and each column is a feature. However, real-world data like neural signals, raw audio clips, or time-series sensor data often naturally arrives in structured multi-dimensional blocks. np.reshape allows you to pivot the data instantly without moving or copying it in memory.
'''

## Example

import numpy as np

arr = np.arange(6)  
reshaped = np.reshape(arr, (2,3))
print(reshaped)



'''
Real-World Scenario: Smart Watch Gesture RecognitionSuppose you are building a machine learning pipeline for a smartwatch health app. The watch tracks wrist movement using an IMU sensor that records data across 3 spatial axes (X, Y, and Z acceleration).To detect a specific gesture (like a hand wave), the watch captures data in 2-second windows at a sampling rate of 50 readings per second. This gives you a natural 2D block of data per gesture: (50 timestamps, 3 axes). However, to feed this window into a Scikit-Learn classifier, you must reshape that 2D matrix into a flat 1D vector of 150 features.Here is the complete production-ready code you can run immediately:
'''

# 1. Generate pseudo-data: A single 2-second gesture window captured by the sensor
# Dimensions: 50 sensor readings across 3 geometric axes (X, Y, Z)
# Shape: (50, 3) -> Total of 150 unique continuous values
np.random.seed(42)
raw_sensor_window = np.random.uniform(-2.0, 2.0, size=(50, 3))

print("--- Data Ingested From Smartwatch Hardware ---")
print(f"Original Sensor Matrix Shape: {raw_sensor_window.shape} (Timestamps, Axes)")
print(f"First 3 timestamps (X, Y, Z raw values):\n{raw_sensor_window[:3]}\n")

# 2. Reshape the 2D window into a flat 1D feature vector for a Machine Learning model
# The target shape is 150 columns (1D array)
# Using -1 tells NumPy to automatically calculate the exact dimension size
ml_ready_vector = raw_sensor_window.reshape(1, -1)

print("--- Data Formatted For Machine Learning Classifier ---")
print(f"Reshaped Vector Shape:       {ml_ready_vector.shape} (Samples, Features)")
print(f"First 6 feature elements:     {ml_ready_vector[0, :6]}\n")

# 3. Reverse the process: Reshape it back to 2D for human-readable visualization
reconstructed_matrix = ml_ready_vector.reshape(50, 3)

print("--- Data Reconstructed For UI Visualization ---")
print(f"Reconstructed Shape:         {reconstructed_matrix.shape}")
print(f"Verification Match?          {np.array_equal(raw_sensor_window, reconstructed_matrix)}")


'''
Why np.reshape is Perfect Here
Zero-Copy Performance: Instead of creating a brand-new array in your RAM and physically copying all 150 values (which eats battery life on a smartwatch), np.reshape simply changes the internal metadata (the view) of how NumPy reads the existing memory block. It happens instantaneously.

The Magic -1 Dimension: If you don't want to manually calculate the math (50 * 3 = 150), passing -1 inside reshape(1, -1) forces NumPy to do the arithmetic for you. It automatically looks at the total data payload size and builds the correct shape.

Structural Integrity: As seen in the output, when flattening and un-flattening data, the structural order of your array elements remains perfectly preserved.
'''