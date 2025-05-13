n=0;

with open("data.dat") as file:
	for line in file:
		line = line.strip()
		zero = line.count('0')
		one = line.count('1')
		if (zero % 3 == 0 or one % 2 == 0):
			n += 1

print(n)

