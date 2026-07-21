import csv
from prometheus_client import Gauge, push_to_gateway, REGISTRY

# 1. Define the metric
g = Gauge("subtraction", "Sum of subtractions")
total = 0.0

with open("numbers.csv", mode="r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        num1 = float(row["num1"])
        num2 = float(row["num2"])
        
        # Calculate the subtraction
        result = num1 - num2
        print(f"Subtraction Result -> {num1} - {num2} = {result}")
        
        # 2. Update the total!
        total += result 

# 3. Set the final calculated total to the Gauge
g.set(total)

# 4. Push to the gateway (updated the job name to make more sense)
push_to_gateway("192.168.49.1:9091", job="subtraction_job", registry=REGISTRY)	
print("Metrics successfully pushed to Prometheus Pushgateway")
