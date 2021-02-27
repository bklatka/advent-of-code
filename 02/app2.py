import re as regexp

data = open('./input.txt').read().split('\n')


counter = 0

def count_matches(letter, password):
	return len(regexp.findall(letter, password))


for policy in data:
	amount, pattern, password = policy.split(' ')

	match_count = 0

	valid_letter = pattern[0] # cut ":" sign
	
	first_index, second_index = map(lambda n:int(n) - 1, amount.split('-'))

	if password[first_index] == valid_letter:
		match_count = match_count + 1

	if password[second_index] == valid_letter:
		match_count = match_count + 1

	
	if match_count == 1:
		counter = counter + 1
	

	
print(counter)
