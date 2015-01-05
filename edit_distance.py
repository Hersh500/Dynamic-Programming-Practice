def print_matrix(matrix):
	for row in matrix:
		print(row)

def find_distance (str1, str2, copy, indel):
	s = [ [0 for i in range(0, len(str2) + 1)] for j in range(0, len(str1) + 1)]
	
	for i in range(1, len(str1) + 1):
		s[i][0] = s[i-1][0] + indel
	for j in range(1, len(str2) + 1):
		s[0][j] = s[0][j-1] + indel

	for i in range(1, len(str1) + 1):
		for j in range(1, len(str2) + 1):
			try:
				if str1[i] == str2[j]:
					s[i][j] = s[i-1][j-1]
				else:
					s[i][j] = min(s[i-1][j] + indel, s[i][j-1] + indel, s[i-1][j-1] + copy) 
			except IndexError:
				s[i][j] = min(s[i-1][j] + indel, s[i][j-1] + indel, s[i-1][j-1] + copy) 

	print_matrix(s)

def main():
	str1 = "alligator"
	str2 = "gator"
	copy = 1
	indel = 1 
	
	find_distance(str1, str2, copy, indel)

if __name__ == "__main__":
	main()
	
	
