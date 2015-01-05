def pascal(rows):
	triangle = [[1], [1,1]]
	rowNum = 3
	if rows == 1:
		print(triangle[0])
	if rows == 2:
		print(triangle)
	else: 
		rowNum = 3
		while rowNum <= rows:
			triangle = createRow(triangle, rowNum)
			rowNum += 1

	for row in triangle:
		print(row);
	
def createRow(triangle, rowNum):
	triangle.append([1])
	for i in range(1, rowNum-1):
		val = triangle[rowNum - 2][i-1] + triangle[rowNum - 2][i]
		triangle[rowNum-1].append(val)
	triangle[rowNum-1].append(1)
	return triangle

if __name__ == "__main__":
	pascal(10)
