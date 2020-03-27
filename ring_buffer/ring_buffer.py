from doubly_linked_list import DoublyLinkedList


class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = None
		self.storage = DoublyLinkedList()

	def append(self, item):
		# empty, add item to head
		# ---deprecated---
		# Note: no longer needed since redundant with storage length < buffer capacity condition
		# if self.storage.length == 0:
		# 	self.storage.add_to_head(item)
		# 	self.current = self.storage.head
		
		# cursor that indicates the current item on the ring
		cursor = self.current

		# if full...
		if self.storage.length == self.capacity:
			# set the cursor value to new item
			cursor.value = item
			# if the cursor has reached the end
			if cursor is self.storage.tail:
				# then reset cursor to the head
				self.current = self.storage.head
			else:	
				# otherwise move current cursor to the cursor's next node
				self.current = cursor.next

		# if empty or space remaining...
		elif self.storage.length < self.capacity:
			# add item to the end
			self.storage.add_to_tail(item)
			# set current cursor to the head
			self.current = self.storage.head

	def get(self):
		# Note:  This is the only [] allowed
		list_buffer_contents = []

		current_node = self.storage.head

		if self.storage.length == 0:
			return None

		while current_node:
			list_buffer_contents.append(current_node.value)
			current_node = current_node.next

		return list_buffer_contents

buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
print(buffer.get()) # should return ['a', 'b', 'c', 'd']
buffer.append('e')
print(buffer.get()) # should return ['a', 'b', 'c', 'd', 'e']
buffer.append('f')
print(buffer.current.value)
print(buffer.current.next.value)
print(buffer.get()) # should return ['f', 'b', 'c', 'd', 'e']
buffer.append('g')
print(buffer.current.value)
print(buffer.current.next.value)
print(buffer.get()) # should return ['f', 'g', 'c', 'd', 'e']
buffer.append('h')
print(buffer.current.value)
print(buffer.current.next.value)
buffer.append('i')
print(buffer.current.value)
# print(buffer.current.next.value)
print(buffer.get()) # should return ['f', 'g', 'h', 'i', 'e']
buffer.append('j')
buffer.append('k')
print(buffer.get()) # should return ['k', 'g', 'h', 'i', 'j']

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
