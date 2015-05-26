"""
function generator makes the agents that will be in the model and puts them in a list. I'll have to give a name to the output of this function, I'll call it agents.

effectively, the name of each agent will be its place in the list, or, in other words, the objects don't really have names, but they can be pointed to by using agents[0] for the first object, etc. 

natures_course is the function that happens every night. it has agents meet, decide to fuck, spread disease or not. 

note: for 100% you must put in "100". "1" will be interpreted as 1%
"""
import random

#prompt user for 
catch = percenterizer(catch_rate)
adult, percent_disease, virgin, percent_no_comply bla bla

def percenterizer(percent):
	if percent < 1: x = percent
	else: x = percent/100.0
	return x

def sex(A1, A2):
	A1.partners.append(A2.id)
	A2.partners.append(A1.id)
	if (A1.disease == True or A2.disease == True) and (random.uniform(0,1)<catch): 
		A1.disease, A2.disease = True, True
	
def deteriorating_morality(A1, A2):
	#DEFINITION TBA

class agent(object):
	def __init__(self, id_number, disease = False, comply = True, partners = ["yes"]):
		self.partners = partners
		self.id = id_number
		self.disease = disease
	def execute(self, other):
		if comply or other.comply:
			if (self.partners[0] == "yes" and other.partners[0] == "yes") or deteriorating_morality(self, other) == True:
				sex(self, other)  
			else: pass
		else: sex(self, other)

def generator(adult, percent_disease, virgin, percent_no_comply):
	L = range(adult+virgin+1)
	i = 0
	disease = percenterizer(percent_disease)
	no_comply = percenterizer(percent_no_comply)
	while i < disease*no_comply*adult:
		L[i] = agent(i, True, False)
		i = i+1
	while i < disease*(1-no_comply)*adult:
		L[i] = agent(i, True, True)
		i = i+1
	while i < (1-disease)*no_comply*adult:
		L[i] = agent(i, False, False)
		i = i+1
	while i < (1-disease)*(1-no_comply)*adult:
		L[i] = agent(i)
		i = i+1
	while i < adult + no_comply*virgin:
		L[i] = agent(i, False, False, partners = [])
		i = i+1
	while i < adult + virgin + 1:
		L[i] = agent(i, False, True, partners = [])
	return L

def state_of_the_world(L):
	c, v = 0, 0	
	for i in range(len(L)):
		if L[i].disease: c = c+1
		else: pass
		if L[i].disease and not L[i].partners[0] == "yes": v = v+1
		else: pass
	return (c/float(len(L)), float(v)/virgins)

def natures_course(catch, percent_comply, L, iterations):
	R = []	
	i = 0
	while i < iterations:
		j = 0
		while j < len(L)/2
			pair = random.sample(L, 2)
			pair[0].execute(pair[1])			
			j = j+1
		stats = state_of_the_world(L)
		R.append(stats)
		print "overall fraction infected = %s, fraction initial virgins infected = %s" % stats
		i = i+1
