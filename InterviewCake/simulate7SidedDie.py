# Simulate 7 Sided Die:
# ********************* #

# You have a function rand5() that generates a random integer
# from 1 to 5. Use it to write a function rand7() that
# generates a random integer from 1 to 7.

# rand5() returns each integer with equal probability.
# rand7() must also return each integer with equal probability. 

import random

def rand5():
	return random.randint(1,5)

def rand7():
	# Implement rand7() using rand5()
	res = [[1,2,3,4,5], [6,7,1,2,3], [4,5,6,7,1], [2,3,4,5,6], [7,0, 0, 0,0]]
	row = rand5() - 1
	col = rand5() - 1
	if row * col >= 21 or res[row][col] == 0:
		return rand7()

	return res[row][col]

if __name__ =="__main__":
	print ("Simulate 7 Sided Die")
	rand7List = [rand7() for _ in range(10)]
	print (rand7List)

	# Pring Histogram
	histList = [rand7() for _ in range(500)]
	hist = dict()

	for x in histList:
		if x in hist:
			hist[x] += 1
		else:
			hist[x] = 1

	for x in hist:
		count = hist[x]
		for i in range(count):
			print (x, end = "")
		print("\n")        
