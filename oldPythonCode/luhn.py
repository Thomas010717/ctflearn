#card number multiple of 123457
#the Luhn check digit is valid

def mul(num):
	return int(num) % 123457 == 0
		

def luhn_check(num):
#reverse the digits, multiply 2 for the odd index, minus 9 for value that exceed 9, check the sum if its multiple of 10.
	digits = [int(d) for d in str(num)]
	digits = digits[::-1] 
	checksum = 0
	
	for i, d in enumerate(digits):
		if i%2==1:
			d*=2
			if d>9:
				d-=9
		checksum +=d
	return checksum % 10 == 0
	
c1=543210
c2=1234

for i in range(1000000):
	full = str(c1)+str(i).zfill(6)+str(c2)
	if luhn_check(full) and mul(full):
		print(full)
