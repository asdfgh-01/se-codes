def findMin(diff):
    index = -1
    minimum = 999999999
    for i in range(len(diff)):
        if (not diff[i][1] and minimum > diff[i][0]):
            minimum = diff[i][0]
            index = i
    return index
def SSTF(sequence, head):            
    if (len(sequence) == 0):
        return
    l = len(sequence)
    diff = [0] * l
    for i in range(l):
        diff[i] = [0, 0]                         # [numeric difference between, used or not]
    seek_count = 0
    seek_sequence = [0] * (l + 1)                # l+1 cuz sequence contains head as well
    for i in range(l):
        seek_sequence[i] = head
        for i in range(len(diff)):
            diff[i][0] = abs(sequence[i] - head) # diff list -> difference betweeen all seq and head
        index = findMin(diff)                    # find the smallest one 
        diff[index][1] = True                    # in 2nd part of diff list -> make that smallest index true to show its been used
        seek_count += diff[index][0]
        head = sequence[index]
    seek_sequence[l] = head   # for the last value
    print("Seek Sequence is")
    print(seek_sequence[0],end=" ")
    for i in range(1,l + 1):
        print(" ==> ",seek_sequence[i],end=" ")
    return seek_count

if __name__ == "__main__":
    Number_disk = int(input("Enter the number of disks: "))
    if Number_disk > 0:
        head = int(input("Enter initial header position: "))
        while not head in range(Number_disk + 1):
            head = int(input("Please enter valid initial head position: "))
        sequence = []
        sequence = list(map(int, input("Enter the sequence:").split()))
        for i in sequence:
            if i < 0 or i >= Number_disk:
                print("Sequence out of range")
                exit(0)

        seek_operations = SSTF(sequence, head)
        print("\nSeek Time: ", seek_operations) 

'''
Enter the number of disks: 500
Enter initial header position: 50
Enter the sequence:176 79 34 60 92 11 41 114
Seek Sequence is
50  ==>  41  ==>  34  ==>  11  ==>  60  ==>  79  ==>  92  ==>  114  ==>  176
Seek Time:  204
'''