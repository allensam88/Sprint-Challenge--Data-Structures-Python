class Node:
	def __init__(self, value=None, next_node=None):
		# the value at this linked list node
		self.value = value
		# reference to the next node in the list
		self.next_node = next_node

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		# set this node's next_node reference to the passed in node
		self.next_node = new_next


class LinkedList:
	def __init__(self):
		# reference to the head of the list
		self.head = None

	def add_to_head(self, value):
		node = Node(value)
		if self.head is not None:
			node.set_next(self.head)

		self.head = node

	def contains(self, value):
		if not self.head:
			return False
		# get a reference to the node we're currently at; update this as we
		# traverse the list
		current = self.head
		# check to see if we're at a valid node
		while current:
			# return True if the current value we're looking at matches our
			# target value
			if current.get_value() == value:
				return True
			# update our current node to the current node's next node
			current = current.get_next()
		# if we've gotten here, then the target node isn't in our list
		return False

# Test scenario
# HEAD = 5
# 5 -> 4 -> 3 -> 2 -> 1 -> Null
# Reverse the pointers
# HEAD = 1
# Null <- 5 <- 4 <- 3 <- 2 <- 1

	def reverse_list(self, node, prev):
		# You must use recursion for this solution
		
		# If no head, then empty list, return nothing
		if self.head is None:
			return None
		
		# Base case: stop when next node pointer is null, then you've reached the tail end
		if node.next_node is None:
			# set the tail as the new head and...
			self.head = node

			# reverse the pointer to the previous node
			node.set_next(prev)
			return # entire call stack

		# Otherwise, if haven't reached the tail yet,
		# temporarily store the next node and...
		next = node.get_next()
		# reverse the pointer to previous node 
		node.set_next(prev)

		# Keep recursing, sending in next node, while the current node becomes the new previous node
		self.reverse_list(next, node)
