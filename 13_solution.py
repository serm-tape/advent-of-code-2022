import json

f = open("13_input.txt")
lines = f.read().split('\n')[0:-1]
f.close()


packets = []
for i in range(0, len(lines), 3):
	left = json.loads(lines[i])
	right = json.loads(lines[i+1])
	packets.append(left)
	packets.append(right)	

def in_right_order(left, right):
	o = 0
	#print(f'left: {left}')
	#print(f'right: {right}')
	while o < len(left) and o < len(right):
		if type(left[o]) == int and type(right[o]) == int:
			if left[o] < right[o]:
				return True
			elif left[o] > right[o]:
				return False

		elif type(left[o]) == list and type(right[o]) == list:
			inner_result = in_right_order(left[o], right[o])
			if inner_result is not None:
				return inner_result

		elif type(left[o]) == list and type(right[o]) == int:
			inner_result = in_right_order(left[o], [right[o]])
			if inner_result is not None:
				return inner_result

		elif type(left[o]) == int and type(right[o]) == list:
			inner_result = in_right_order([left[o]], right[o])
			if inner_result is not None:
				return inner_result

		o += 1
	if o == len(left) and o == len(right):
		return None
	else:
		return o == len(left)


right_order = 0
divider_mul = 1
sorted_packet = [packets[0]]
for i in range(1, len(packets)):
	for j in range(len(sorted_packet)):
		if not in_right_order(sorted_packet[j], packets[i]):
			sorted_packet.insert(j, packets[i])
			break
		if j == len(sorted_packet) -1:
			sorted_packet.append(packets[i])
			break

dividers = [[[2]], [[6]]]
for i in range(len(dividers)):
	#print(f'i:{i}')
	for j in range(len(sorted_packet)):
		#print(f'j:{j}')
		if not in_right_order(sorted_packet[j], dividers[i]):
			sorted_packet.insert(j, dividers[i]) 
			print(f'inserted {dividers[i]} at {j}')
			divider_mul *= j+1
			break
		#print(f'j:{j} len(sorted): {len(sorted_packet)}')
		if j == len(sorted_packet) -1:
			divider_mul *= j+2
			print(f'inserted {dividers[i]} at {j+1}')
			sorted_packet.append(dividers[i])
			break

print(f'divider_mul: {divider_mul}')

