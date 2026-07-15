import csv
with open("numbers.csv",mode="r") as f:
	reader=csv.DictReader(f)
	for row in reader:
		num1=float(row["num1"])
		num2=float(row["num2"])
		print(f"Division  Result -> {num1} / {num2}={num1/num2}")
		
