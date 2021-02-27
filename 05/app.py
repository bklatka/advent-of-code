
seats = open('./input.txt').read().split('\n')


INITIAL_ROW_RANGE = [0, 127]
INITIAL_COL_RANGE = [0, 7]

def get_half(some_range):
	difference = some_range[1] - some_range[0]
	print(difference)

	if difference % 2 == 0:
		return int(difference/2)
	return int((difference + 1)/2 - 1)

def decode_row(encoded_row):
	UPPER_HALF = 'B'
	LOWER_HALF = 'F'

	seat_range = [0, 127]
	print('decoding')
	print(encoded_row)
	for index, command in enumerate(encoded_row):
		if command is UPPER_HALF:
			seat_range[1] = seat_range[1] - get_half(seat_range)

		if command is LOWER_HALF:
			seat_range[0] = seat_range[0] + get_half(seat_range)

		print(seat_range)

	return seat_range


for seat in seats:
	# first 7 letters are for rows, last 3 are for col
	seat_row_encoded = seat[0:7]
	seat_col_encoded = seat[-3:]

	row = decode_row(seat_row_encoded)




	print('\n')
