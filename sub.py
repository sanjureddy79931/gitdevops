import csv
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

registry = CollectorRegistry()

g = Gauge("subtraction", "Sum of subtractions", registry=registry)
total = 0.0

with open("numbers.csv", mode="r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        num1 = float(row["num1"])
        num2 = float(row["num2"])
        result = num1 - num2
        print(f"Subtraction Result -> {num1} - {num2} = {result}")
        total += result

g.set(total)

push_to_gateway("192.168.49.1:9091", job="subtraction_job", registry=registry)
print("Pushed subtraction_job successfully")
