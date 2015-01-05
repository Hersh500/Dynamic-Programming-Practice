''' Edit Distance Problem: Given two strings of size m, n and set of operations replace (R), insert (I) and delete (D) all at equal cost. 
	Find minimum number of edits (operations) required to convert one string into another.'''

def print_matrix(matrix): #prints all rows in a two dimensional array 
	for row in matrix:
		print(row)

def find_distance (str1, str2, copy, indel): #Uses a two dimensional array to find the edit distance
	s = [ [0 for i in range(0, len(str2) + 1)] for j in range(0, len(str1) + 1)]
	
	for i in range(1, len(str1) + 1): #Initializes the array 
		s[i][0] = s[i-1][0] + indel
	for j in range(1, len(str2) + 1):
		s[0][j] = s[0][j-1] + indel

	for i in range(1, len(str1) + 1): #Loops through the array, using dynamic programming 
		for j in range(1, len(str2) + 1):
			try:
				if str1[i] == str2[j]: 
					s[i][j] = s[i-1][j-1]
				else:
					s[i][j] = min(s[i-1][j] + indel, s[i][j-1] + indel, s[i-1][j-1] + copy) #Uses the min to find the Minimum Edit Distance, finds the least costly edit
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
	
	
