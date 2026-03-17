import csv
import math

# Generates sample server load data
with open('server_load.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Hour', 'Load'])
    for i in range(25):
        # Simulating server load with a sine wave + baseline
        load = 50 + 30 * math.sin(i / 3.0) 
        writer.writerow([i, round(load, 2)])

print("Data generated in server_load.csv")