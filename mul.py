import csv
from prometheus_client import Gauge, push_to_gateway, REGISTRY

# Define the metric for multiplication
g = Gauge("multiplication", "Sum of multiplications")
total = 0.0

with open("numbers.csv", mode="r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        num1 = float(row["num1"])
        num2 = float(row["num2"])
        
        # Calculate the multiplication
        result = num1 * num2
        print(f"Multiplication Result -> {num1} * {num2} = {result}")
        
        # Add to the total
        total += result 

# Set the final calculated total to the Gauge
g.set(total)

# Push to the gateway with a unique job name
push_to_gateway("192.168.49.1:9091", job="multiplication_job", registry=REGISTRY)	
print("Multiplication metrics successfully pushed to Prometheus Pushgateway.")
