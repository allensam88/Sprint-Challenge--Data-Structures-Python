from doubly_linked_list import DoublyLinkedList


class RingBuffer:
	def __init__(self, capacity):
		self.capacity = capacity
		self.current = None
		self.storage = DoublyLinkedList()

	def append(self, item):
		if self.storage.length == 0:
			self.storage.add_to_head(item)

		elif self.storage.length > 0:
			self.storage.add_to_tail(item)

	def get(self):
		# Note:  This is the only [] allowed
		list_buffer_contents = []

		if self.storage.length == 0:
			return None

		while self.storage.length > 0:
			node = self.storage.remove_from_head()
			list_buffer_contents.append(node)

		return list_buffer_contents

buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
print(buffer.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
