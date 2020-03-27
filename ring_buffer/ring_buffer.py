from doubly_linked_list import DoublyLinkedList


class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = None
		self.storage = DoublyLinkedList()

	def append(self, item):
		# empty, add item to head
		if self.storage.length == 0:
			self.storage.add_to_head(item)
			self.current = item

		# full, remove from tail, then add to head
		elif self.storage.length == self.capacity:
			self.storage.remove_from_head()
			self.storage.add_to_tail(item)
			self.current = item

		# space remaining, add to tail
		elif self.storage.length < self.capacity:
			self.storage.add_to_tail(item)
			self.current = item

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
print(buffer.get())
buffer.append('e')
print(buffer.get())
buffer.append('f')
print(buffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
