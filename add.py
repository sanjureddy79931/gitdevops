import csv
from prometheus_client import Gauge,push_to_gateway, REGISTRY

g=Gauge("addition","Sum of additions")
total=0.0
with open("numbers.csv",mode="r") as f:
	reader=csv.DictReader(f)
	for row in reader:
		num1=float(row["num1"])
		num2=float(row["num2"])
		print(f"Addition Result -> {num1}+{num2}={num1+num2}")

g.set(total)
push_to_gateway("192.168.49.1:9091",job="add_job",registry=REGISTRY)	
print("Prometheus")
		
