## Example

import numpy as np

a = np.array([[1, 2]])
b = np.array([[3, 4]])
print(np.concatenate((a, b), axis=0))

# or

a1 = np.array([[10,20], [30,40]], dtype=np.int32)
a2 = np.array([[50, 60]], dtype=np.int32)

output_array = np.empty((3,2), dtype=np.float32)

results = np.concatenate(
    (a1, a2),
    axis=0,
    out=output_array,
    casting="same_kind"
)

print(results)

'''
A classic real-world application for np.concatenate is merging data from multiple edge sources, files, or sessions into a single dataset for batch processing.In analytics and machine learning pipelines, data rarely arrives all at once. It often arrives in separate pieces—such as distinct logs from two different servers, sensor data recorded across separate shifts, or customer transaction files broken up by calendar months. np.concatenate links these independent arrays together along a specified axis to build a unified database.
'''

'''
Real-World Scenario: Fleet Management Telemetry AggregationSuppose you manage logistics for a delivery company. You track your delivery trucks using IoT telematics boxes that log a truck's spatial coordinates and velocity.
'''

# 1. Generate pseudo-data for Truck A (Shift 1)
# Data structure: 4 timestamps, each recording [Latitude, Longitude, Speed_kmh]
# Shape: (4, 3)
truck_a_telemetry = np.array([
    [-1.2921, 36.8219, 45.5],
    [-1.2950, 36.8250, 52.1],
    [-1.2985, 36.8310, 0.0],   # Stopped at delivery point
    [-1.3010, 36.8345, 38.2]
])

# 2. Generate pseudo-data for Truck B (Shift 1)
# Data structure: 3 timestamps, tracking the same metrics
# Shape: (3, 3)
truck_b_telemetry = np.array([
    [-1.2840, 36.8150, 60.0],
    [-1.2892, 36.8198, 55.4],
    [-1.2915, 36.8210, 48.1]
])

print("--- Independent Sensor Arrays ---")
print(f"Truck A Telemetry Shape: {truck_a_telemetry.shape}")
print(f"Truck B Telemetry Shape: {truck_b_telemetry.shape}\n")

# 3. Use np.concatenate to combine the arrays vertically (adding more rows)
# axis=0 stacks rows on top of each other. 
# Target combined shape will be: (4 + 3, 3) -> (7, 3)
unified_fleet_data = np.concatenate((truck_a_telemetry, truck_b_telemetry), axis=0)

print("--- Unified Fleet Database (Concatenated) ---")
print(f"Combined Data Shape:     {unified_fleet_data.shape}")
print(f"Total Combined Records:  {len(unified_fleet_data)} timestamps logged.")
print("\nFull Telemetry Matrix:")
print(unified_fleet_data)

# 4. Instantly run fleet-wide analytics on the combined array
fleet_average_speed = np.mean(unified_fleet_data[:, 2])
print(f"\nFleet Average Speed:     {fleet_average_speed:.2f} km/h")


'''
Why np.concatenate is Perfect HereAxis Flexibility: By switching to axis=1, you can instantly stack arrays horizontally. For instance, if you had a separate array containing the weather conditions for those exact same timestamps, axis=1 would add it cleanly as a fourth column.

Batch Ingestion Input: It takes its inputs as a Python tuple or list (array1, array2, ...). This means you can pass an entire dynamic python list of 500 truck logs into a single call, and it will bind them all instantly.

Vector Optimization: Unlike Python's standard list.extend(), which shifts unstructured references around, np.concatenate maps out the final combined size, requests a matching contiguous RAM slot, and transfers the raw bits efficiently.
'''