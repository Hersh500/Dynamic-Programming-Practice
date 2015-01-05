def profit_wine(wine_list, year, profit):
	if len(wine_list) == 1:
		return profit[wine_list[0]]*year
	else:
		return max(profit_wine(wine_list[1:],year+1, profit) + profit[wine_list[0]]*year, profit_wine(wine_list[:-1], year+1, profit) + profit[wine_list[-1]]*year)

def main():
	profit = {1:1, 2:4, 3:2, 4:3}
	wine_list = [1,2,3,4]
	print(profit_wine(wine_list, 1, profit))

if __name__ == "__main__":
	main()
	
