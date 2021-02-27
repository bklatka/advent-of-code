

data = open('./input.txt').read()


data_list = data.split('\n')
data_list = list(map(lambda n: int(n), data_list))
data_list.sort()

reversed = data_list.copy()
reversed.sort(reverse=True)

blacklist = []

for lowI1, low1 in enumerate(data_list):
	for highI, high in enumerate(reversed):
		for lowI2, low2 in enumerate(data_list):
		
			first_value = low1
			second_value = low2
			third = high

			if first_value + second_value + third == 2020:
				print('got it')
				print(first_value, end=" ")
				print(second_value, end=" ")
				print(third, end=" ")
				print('Result is')
				print(first_value * second_value * third)







