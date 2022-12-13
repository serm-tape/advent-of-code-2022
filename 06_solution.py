f = open("06_input.txt")
lines = f.read().split('\n')

window_length = 14
window_start = 0
for line in lines:
	print(f'line len = {len(line)}')
	if line != '':
		while window_start < len(line):
			window_end = window_start + window_length
			window = line[window_start:window_end]
			is_marker = True
			print(f'window start: {window_start}')
			for i in range(window_length):
				for j in range(i+1, window_length):
					print(f'window: {window}, i:{i}, j:{j}')
					if window[i] == window[j]:
						window_start += i+1
						is_marker = False
						break
				if not is_marker:
					break

			print(f'is marker: {is_marker}')
			if is_marker:
				print(f'first marker = {window_end}')
				break

f.close()