import math
def minmaxx(x,y,numbers):
    if y-x<=1:
        return(max(numbers[x],numbers[y]),min(numbers[x],numbers[y]))
    else:
        (max1,min1)=minmaxx(x,math.floor((x+y)/2),numbers)
        (max2,min2)=minmaxx(math.floor((x+y)/2)+1,y,numbers)
    return(max(max1,max2),min(min1,min2))

numbers = list(map(int,input("enter the elements of your array :").split()))
x = 0
y = len(numbers)-1
max,min=minmaxx(x,y,numbers)
print('the maximum element in your array is',max)
print('the minimum element in your array is',min)

'''
-----------OUTPUT-----------
enter the elements of your array :4 5 6 2 9 2 8
the maximum element in your array is 9
the minimum element in your array is 2
'''
