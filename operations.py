def findMinNumOps(num, ops):
	for i in range(2, num + 1):
		if (i % 2 == 0 and i % 3 == 0):
			ops[i] = min(ops[i/2] + 1, ops[i/3] + 1, ops[i-1] + 1)
		elif (i % 2 == 0):
			ops[i] = min(ops[i/2] + 1, ops[i-1] + 1)
		elif (i % 3 == 0):
			ops[i] = min(ops[i/3] + 1, ops[i-1] + 1)
		else:
			ops[i] = ops[i-1] + 1
	print(ops)
	return ops[num]
		
	
def main():
	ops = {1:0}
	num = 4 
	print(findMinNumOps(num, ops))

if __name__ == "__main__":
	main()
