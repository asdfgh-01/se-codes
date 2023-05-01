size = 8
disk_size = 200

def SCAN(arr, head, direction):
	seek_count = 0
	distance, cur_track = 0, 0
	left = []
	right = []
	seek_sequence = []

	# Appending end values which has to be visited before reversing the direction
	if (direction == "left"):
		left.append(0)
	elif (direction == "right"):
		right.append(disk_size - 1)

	for i in range(size):
		if (arr[i] < head):
			left.append(arr[i])
		if (arr[i] > head):
			right.append(arr[i])

	# Sorting left and right vectors
	left.sort(reverse=True)  # big -> small
	right.sort()

	# Run the while loop two times one by one scanning right and left of the head
	run = 2
	while (run != 0):
		if (direction == "left"):
			for i in range(len(left)):
				cur_track = left[i]

				# Appending current track to seek sequence
				seek_sequence.append(cur_track)

				# Calculate absolute distance
				distance = abs(cur_track - head)

				# Increase the total count
				seek_count += distance

				# Accessed track is now the new head
				head = cur_track
			
			direction = "right"
	
		elif (direction == "right"):
			for i in range(len(right)):
				cur_track = right[i]
				
				# Appending current track to seek sequence
				seek_sequence.append(cur_track)

				# Calculate absolute distance
				distance = abs(cur_track - head)

				# Increase the total count
				seek_count += distance

				# Accessed track is now new head
				head = cur_track
			
			direction = "left"
		
		run -= 1

	print("Total number of seek operations =",seek_count)

	print("Seek Sequence is")
	print(seek_sequence[0],end=" ")
	for i in range(1,len(seek_sequence)):
	    print(" ==> ",seek_sequence[i],end=" ")




arr = [ 176, 79, 34, 60, 92, 11, 41, 114 ]
head = 50
direction = "right"

SCAN(arr, head, direction)

'''
Total number of seek operations = 337
Seek Sequence is
60  ==>  79  ==>  92  ==>  114  ==>  176  ==>  199  ==>  41  ==>  34  ==>  11 
'''
