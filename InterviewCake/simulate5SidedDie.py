# Simulate 5 Sided Die
# ********************* # 

# You have a function rand7() that generates a random integer from 1 to 7. Use it to write a function rand5() that generates a random integer from 1 to 5.

# rand7() returns each integer with equal probability. rand5() must also return each integer with equal probability.

import random

def rand7():
	return random.randint(1, 7)

def rand5():
	# Implement rand5() using rand7()
	x = rand7()
	if x <= 5:
		return x
	else:
		return rand5()

if __name__ == "__main__":
	print( "Rolling 5-sided die .. ")
	print( [rand5() for _ in range(10) ] )
	
	rand5List = [rand5() for _ in range(1000)]
	hash_table = dict()
	for num in rand5List:
		if num in hash_table:
			hash_table[num] += 1
		else:
			hash_table[num] = 1
	
	print( hash_table)
		
