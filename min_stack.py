class MinStack:
	def __init__(self):
    	"""
    	initialize your data structure here.
    	"""
    	self.min_val = []
    	self.data = []

	def push(self, x: int) -> None:
    	if (len(self.data) == 0):
        	self.data.append(x)
        	self.min_val.append(x)
    	elif (len(self.data) != 0):
        	self.data.insert(0, x)
    	# maybe not have repeats in min_val
    	if (self.min_val[0] >= x):
        	self.min_val.insert(0, x)

	def pop(self) -> None:
    	# return value from top of stack and
    	# remove from stack
    	if (len(self.data) == 0):
        	return None
    	elif (len(self.data) > 0):
        	val = self.data[0]
        	if (val == self.min_val[0]):
            	self.min_val.remove(self.min_val[0])
            	self.data.remove(self.data[0])
            	return val
        	elif (val != self.min_val[0]):
            	self.data.remove(self.data[0])
            	return val


	def top(self) -> int:
    	# return top value, no remove
    	return self.data[0]

	def getMin(self) -> int:
    	# return the minimum value in stack
    	return self.min_val[0]



if __name__ == "__main__":
	
