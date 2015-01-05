'''
Suppose you are a computer scientist/art thief who has broken into a major art gallery. 
All you have with you to haul out your stolen art is your knapsack which only holds W pounds of art, but for every piece of art you know its value and its weight. 
Write a dynamic programming function to help you maximize your profit.
Here is a sample problem for you to use to get started: Suppose your knapsack can hold a total weight of 20. 
You have 5 items as follows:

item     weight      value
  1        2           3
  2        3           4
  3        4           8
  4        5           8
  5        9          10 '''

class StolenItem:
	def __init__(self, theID, theValue, theWeight):
		self.ID = theID
		self.value = theValue
		self.weight = theWeight

def dpMaxProfit (itemList, knapWeight, maxProfits, weightsUsed):
	maxProfit = 0

	for knapWeights in range (knapWeight + 1):
		print "KNAPWEIGHT:", knapWeights - 1, " ", maxProfits
		newItem = itemList[0]

		for item in [x for x in itemList if x.weight <= knapWeights]:
			if maxProfits[knapWeights - item.weight] + item.value > maxProfit: 
				maxProfit = maxProfits[knapWeights - item.weight] + item.value
				newItem = item
		maxProfits[knapWeights] = maxProfit
		weightsUsed[knapWeights] = newItem.weight

	return(maxProfits[knapWeight])
	
def reMaxProfit(itemList, knapWeight):
	if knapWeight < 1:
		return 0 

	l1 = [x for x in itemList if x.weight <= knapWeight]	
	profitList = [(item.value + reMaxProfit(itemList, knapWeight-item.weight)) for item in l1]

	if len(profitList) > 0:
		return max(profitList)
	else:
		return 0 
		
def _weightsUsed(weightList, knapWeight):
	weight = knapWeight
	while weight > 0:
		print(weightList[weight])
		weight -= weightList[weight]
recurse = True
if recurse:
	maxProfits = [0] * (knapWeight + 1)
	weightsUsed = [0] * (knapWeight + 1)

def main():
	itemList = [StolenItem(1,3,2), StolenItem(2,4,3), StolenItem(3,8,4), StolenItem(4,8,5), StolenItem(5,10,9)]
	knapWeight = 20
	if !recurse:
		maxProfits = [0] * (knapWeight + 1)
		weightsUsed = [0] * (knapWeight + 1)
		print(dpMaxProfit(itemList, knapWeight, maxProfits, weightsUsed))
		print _weightsUsed(weightsUsed, knapWeight)
	else:	
		print (reMaxProfit(itemList, knapWeight))

if __name__ == "__main__":
	main()
