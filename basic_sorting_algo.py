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
        
arr = [3,2,1,4,0,9,5,7,2,6,10,-3]
insertion_sort(arr)
for element in arr :
  print(element,end =" ")
