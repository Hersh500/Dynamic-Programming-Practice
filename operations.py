''' On a positive integer, you can perform any one of the following 3 steps. 
	1.) Subtract 1 from it. ( n = n - 1 )  , 
	2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )  , 
	3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ). 

	Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1
	eg: 1.)For n = 1 , output: 0       2.) For n = 4 , output: 2  ( 4  /2 = 2  /2 = 1 )    3.)  For n = 7 , output: 3  (  7  -1 = 6   /3 = 2   /2 = 1 )'''

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
