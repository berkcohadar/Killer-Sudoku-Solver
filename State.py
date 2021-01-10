class State(object):
	def __init__(self, father, sons, mother, daughters, police, thief, direction, fPassed, sPassed, mPassed, dPassed, pPassed, tPassed, people,moves):
		self.father = father
		self.sons = sons
		self.mother = mother
		self.daughters = daughters
		self.police = police
		self.thief = thief
		self.island1people = father + mother + police + sons + daughters + thief
		self.island2people = fPassed + sPassed + mPassed + dPassed + pPassed + tPassed
		self.direction = direction

		self.fPassed = fPassed
		self.sPassed = sPassed
		self.mPassed = mPassed
		self.dPassed = dPassed
		self.pPassed = pPassed
		self.tPassed = tPassed

		self.people = people
		self.moves = moves

	def getStates(self):
		states_list = []
		if not self.is_valid() or self.is_done():
			return states_list
		person_counter = 1
		if self.direction == Group.goTo:
			person_counter = -1
		for i in self.moves:
			(f,s,m,d,p,t) = i
			self.new_state(states_list, f,s,m,d,p,t, person_counter)
		return states_list

	def new_state(self, states_list, f,s,m,d,p,t, person_counter):
		newState = State(	self.father + person_counter * f, self.sons + person_counter * s, self.mother + person_counter * m, self.daughters + person_counter * d, self.police + person_counter * p, self.thief + person_counter * t, 
							self.direction + person_counter * 1,
							self.fPassed - person_counter * f, self.sPassed - person_counter * s, self.mPassed - person_counter * m, self.dPassed - person_counter * d, self.pPassed - person_counter * p, self.tPassed - person_counter * t,
							self.people,self.moves)
		if newState.is_valid():
			states_list.append(newState)

	def is_valid(self):
		if (self.father < 0 or self.sons < 0 or self.mother < 0 or self.daughters < 0 or self.police < 0 or self.thief < 0
			or self.father > 1 or self.sons > 2 or self.mother > 1 or self.daughters > 2 or self.police > 1 or self.thief > 1
		 	or (self.direction != 0 and self.direction != 1)):
			return False

		if (self.father == 0 and self.mother == 1 and self.sons > 0) or (self.fPassed == 0 and self.mPassed == 1 and self.sPassed > 0):
			return False
		if (self.mother == 0 and self.father == 1 and self.daughters > 0) or (self.mPassed == 0 and self.fPassed == 1 and self.dPassed > 0):
			return False
		if (self.thief > 0 and self.police == 0 and (self.mother>0 or self.father>0 or self.sons>0 or self.daughters>0)) or (
			self.tPassed > 0 and self.pPassed == 0 and (self.mPassed>0 or self.fPassed>0 or self.sPassed>0 or self.dPassed>0)):
			return False
		return True

	def is_done(self):
		return self.thief == 0 and self.police == 0 and self.mother == 0 and self.father == 0 and self.sons == 0 and self.daughters == 0 and self.direction == Group.backTo

	def __str__(self):
		return "State(f: %d, s: %d, m: %d, d: %d, p: %d, t: %d , direction: %d, f: %d, s: %d, m: %d, d: %d, p: %d, t: %d)\n" % (
			self.father , self.sons , self.mother , self.daughters , self.police , self.thief , 
											self.direction, 
			self.fPassed, self.sPassed, self.mPassed, self.dPassed, self.pPassed, self.tPassed, )

class Group:
	goTo = 1
	backTo = 0
	def __init__(self, father, sons, mother, daughters, police, thief, boatCapacity):
		self.father = father
		self.sons = sons
		self.mother = mother
		self.daughters = daughters
		self.police = police
		self.thief = thief
		self.boatCapacity = boatCapacity

FINALSTATE = State(-1, -1, -1, -1, -1, -1, Group.backTo, -1, -1, -1, -1, -1, -1, None,None)



