s = "q{vpln'bH_varHuebcrqxetrHOXEj"
for i in range(256):    
	r = ''    
	for c in s:        
		r += chr(ord(c) ^ i)    
	if r.endswith('}'):        
		print(r)
