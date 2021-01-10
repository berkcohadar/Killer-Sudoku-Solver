from collections import defaultdict
from State import FINALSTATE
import time

class Graph:
	def __init__(self):
		self.bfs_parent = {}
	def heuristic(self, node):
		print("Sum of People: "+ str(node.island1people)+ "\n")
		sum = node.island1people
		if sum == 1:
			return 1
		return 2*sum-3

	def closest(self, queue):
		index = 0
		lowest = 100
		for i in queue:
			print(i.father)
			if self.heuristic(i[-1])+len(i) < lowest:
				lowest = self.heuristic(i[-1])+ len(i)
				index = queue.index(i)
		return index

	def BFS(self, BEGINSTATE):
		self.bfs_parent[BEGINSTATE] = None

		visited = {(BEGINSTATE.father, BEGINSTATE.sons, BEGINSTATE.mother, BEGINSTATE.daughters, BEGINSTATE.police, BEGINSTATE.thief, BEGINSTATE.direction): True}

		queue = [BEGINSTATE]
		counter = 1
		while queue:
			current = queue.pop(self.closest(queue))
			if current.is_done():
				queue.clear()
				self.bfs_parent[FINALSTATE] = current
				print(counter)
				return self.bfs_parent
			for node in reversed(current.getStates()): # node - state current - statelist a-b
				if (node.father, node.sons, node.mother, node.daughters, node.police, node.thief, node.direction) not in visited.keys():
					self.bfs_parent[node] = current
					queue.append(node)
					counter +=1
					visited[(node.father, node.sons, node.mother, node.daughters, node.police, node.thief, node.direction)] = True
		
		return {}

	def node(self, parentList, tail):
		if tail is None:
			return
		if parentList == {} or parentList is None:  # tail not in parentList.keys():
			return
		if tail == FINALSTATE: 
			tail = parentList[tail]
		stack = []
		while tail is not None:
			stack.append(tail)
			tail = parentList[tail]
		while stack:
			print(stack.pop())