import csv
from prometheus_client import Gauge, push_to_gateway, REGISTRY

# Define the metric for division
g = Gauge("division", "Sum of divisions")
total = 0.0

with open("numbers.csv", mode="r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        num1 = float(row["num1"])
        num2 = float(row["num2"])
        
        # Safety check: prevent division by zero crashes
        if num2 == 0.0:
            print(f"Warning: Skipping division by zero for row ({num1} / {num2})")
            continue
            
        # Calculate the division
        result = num1 / num2
        print(f"Division Result -> {num1} / {num2} = {result}")
        
        # Add to the total
        total += result 

# Set the final calculated total to the Gauge
g.set(total)

# Push to the gateway with a unique job name
push_to_gateway("192.168.49.1:9091", job="division_job", registry=REGISTRY)	
print("Division metrics successfully pushed to Prometheus Pushgateway.")
		
