
seats = open('./input.txt').read().split('\n')
# seats = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

INITIAL_ROW_RANGE = [0, 127]
INITIAL_COL_RANGE = [0, 7]

def get_half(some_range):
	difference = some_range[1] - some_range[0]

	if difference % 2 == 0:
		return int(difference/2)
	return int((difference + 1)/2)

def decode_row(encoded_row):
	UPPER_HALF = 'F'
	LOWER_HALF = 'B'

	seat_range = [0, 127]
	for command in encoded_row:
		if command is UPPER_HALF:
			seat_range[1] = seat_range[1] - get_half(seat_range)

		if command is LOWER_HALF:
			seat_range[0] = seat_range[0] + get_half(seat_range)

	last_command = encoded_row[-1]
	if last_command is UPPER_HALF:
		return seat_range[1]

	return seat_range[0]


def decode_col(encoded_col):
	UPPER_HALF = 'L'
	LOWER_HALF = 'R'

	seat_range = [0, 7]
	print(encoded_col)
	for command in encoded_col:
		if command is UPPER_HALF:
			seat_range[1] = seat_range[1] - get_half(seat_range)

		if command is LOWER_HALF:
			seat_range[0] = seat_range[0] + get_half(seat_range)
		print(seat_range)

	last_command = encoded_col[-1]
	if last_command is UPPER_HALF:
		return seat_range[1]

	return seat_range[0]

seats_decoded = []
for seat in seats:
	# first 7 letters are for rows, last 3 are for col
	seat_row_encoded = seat[0:7]
	seat_col_encoded = seat[-3:]

	row = decode_row(seat_row_encoded)
	col = decode_col(seat_col_encoded)
	
	seats_decoded.append(row * 8 + col)





	print('\n')

seats_decoded.sort(reverse=True)
print(seats_decoded[0])