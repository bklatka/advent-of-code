import re as regexp

data = open('./input.txt').read().split('\n')


counter = 0

def count_matches(num_of_letters, letter, password):
	return len(regexp.findall(letter[0], password))


for policy in data:
	amount, valid_letter, password = policy.split(' ')
	

	matches =  count_matches(amount, valid_letter, password)
	if amount == 0:
		max_count = 0
		min_count = 0
	else:
		min_count, max_count = str(amount).split('-')
		max_count = int(max_count)
		min_count = int(min_count)

	if matches <= max_count and matches >= min_count:
		counter = counter + 1	
	

	
print(counter)
