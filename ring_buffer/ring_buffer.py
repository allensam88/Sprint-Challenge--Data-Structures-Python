from doubly_linked_list import DoublyLinkedList


class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current_head = None
		self.storage = DoublyLinkedList()

	def append(self, item):
		# ---deprecated---
		# empty, add item to head
		# if self.storage.length == 0:
		# 	self.storage.add_to_head(item)
		# 	self.current_head = self.storage.head

		# if full, remove from tail, then add to head
		if self.storage.length == self.capacity:
			self.current.value = item
			self.current = self.current.next
			self.storage.tail = self.current

		# if empty or space remaining, add to tail, reset current
		elif self.storage.length < self.capacity:
			self.storage.add_to_tail(item)
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
