# NFA of binary string with 2nd last bit is 1


accept_state = 'q2'
transition = {
	'q0':{'0':['q0'],'1':['q0','q1'] },
	'q1':{'0':['q2'],'1':['q2']},
	'q2':{'0':['q2'],'1':['q2'] }
	}


# User input
current_state = ['q0']
final_list = []
ini = []

initial_state=['q0']


def get_nfa_states(initial_state):
	ini0 = []
	ini1 = []
	li0 = []
	li1 = []
	li = []
	start_state = initial_state
	final_list.append(start_state)
	for item in start_state:
		# print("List ",item)
		state0 = transition[item]['0']
		ini0.append(state0)
		print(item,"(0)","->" ,state0)
	for i in ini0:
		for j in i:
			li0.append(j)
	print("LIST ", li0)

	li.append(li0)
	print("LI ", li)
	for item in start_state:
		state1 = transition[item]['1']
		print(item,"(1)","->" ,state1)
		ini1.append(state1)
	for k in ini1:
		for l in k:
			li1.append(l)
	print("LIST ", li1)

	li.append(li1)
	print("LI ", li)
	# print("INI is ", ini0)
	for x in li:
		if x not in final_list:
			print("X ", x)
			final_list.append(x)
			print("FINAL LIST ", final_list)
			print("Next state ", x)
			get_nfa_states(i)
			
	
get_nfa_states(initial_state)

# q0 (0) ->q0, q0 (1) -> q0q1
# q0q1 (0) -> q0q2, q0q1 (1) -> q0q1q2
# q0q2 (0) -> q0, q0q2 (1) -> q0q1
# q0q1q2 (0) -> q0q2, q0q1q2 (1) -> q0q1q2
