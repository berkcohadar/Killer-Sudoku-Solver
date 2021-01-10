from Graph import Graph
from State import State, Group, FINALSTATE

def boatPassengers(boatCapacity):
	moves = []
	for f in range(boatCapacity + 1):
		for m in range(boatCapacity + 1):
			for s in range(boatCapacity + 1):
				for d in range(boatCapacity + 1):
					for p in range(boatCapacity + 1):
						for t in range(boatCapacity + 1):
							if (m+f+p+d+s+t <= boatCapacity) and (m == 1 or f == 1 or p == 1) and (d < 2 or t < 2 or s < 2):
								moves.append((f,s,m,d,p,t))
	return moves

def runBFS(g, BEGINNING):
	p = g.BFS(BEGINNING)
	if len(p):
		g.path(p, FINALSTATE)
	else:
		print("No Solution")


father,sons,mother,daughters,police,thief,boatCapacity = 1,2,1,2,1,1,2
people = Group(father,sons,mother,daughters,police,thief,boatCapacity)
moves = boatPassengers(boatCapacity)
BEGINNING = State(people.father, people.sons, people.mother, people.daughters, people.police, people.thief, Group.goTo, 0, 0, 0, 0, 0, 0, people, moves)
g = Graph()
runBFS(g, BEGINNING)