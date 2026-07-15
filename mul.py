import csv
with open("numbers.csv",mode="r") as f:
	reader=csv.DictReader(f)
	for row in reader:
		num1=float(row["num1"])
		num2=float(row["num2"])
		print(f"Multiplication  Result -> {num1} x {num2}={num1*num2}")
		
