'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
''''
print("Hello World")
fruits = ["apple","banana"]
x = fruits[0]
l = len(fruits)
print("length is",l,"and x is",x)
fruits.append("guava")
''' 
def bubble_sort(arr) :
  for i in range(0,len(arr)-1) :
    swap = 0
    for j in range (0,len(arr)-1-i) :
      if arr[j] > arr[j+1] :
        swap = 1
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
    if swap == 0 :
      return
  '''
   2 4 6 3
  '''
def insertion_sort(arr) :
  for i in range(1,len(arr)) :
    x = arr[i]
    j = i-1
    while j >= 0 and arr[j] > x : 
      arr[j+1] = arr[j]
      j = j-1
    arr[j+1] = x
    
def selection_sort(arr) :
  for i in range(0,len(arr)-1) :
    min = i
    for j in range(i,len(arr)) :
      if arr[j] < arr[min] :
        min = j
    if min != i :
      temp = arr[i]
      arr[i] = arr[min]
      arr[min] = temp
    
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def BinarySearch(arr,left,right,val) :
    mid = int((left+right)/2)
    print(left,right)
    if left > right :
        return -1
    if arr[mid] == val :
        print("got it",mid)
        return mid
    elif arr[mid] > val:
        BinarySearch(arr,left,mid-1,val)
    else :
        BinarySearch(arr,mid+1,right,val)

arr = [3,2,1,4,0,9,5,7,2,6,10,-3]
selection_sort(arr)
for element in arr :
  print(element,end =" ")

arr1 = [1,2,3,4,5,6,7,8,9,10]
print(BinarySearch(arr,0,len(arr1)-1,3))
#print(idx)
