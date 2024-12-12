#defining a function for the selection sort 
#algorithm

def selection_sort(arr):
  #get the lenghth of the array 
  n = len(arr)
  #looping through the array 
  for i in range(n-1):
    #this outter loop is responsible for finding the minimun element in the array.
    #creating a varianle that will hold the index of the minimum element in the array
    min_index = i
    for j in range(i+1,n):
      if arr[j] < arr[min_index]:
        if arr[j] < arr[min_index]:
          min_index = j
  #swapping the minimum element with the first element of the unsorted part of the array

    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr 

#example usage 
numbers = [5,2,8,1,9,3]
sorted_numbers =selection_sort(numbers)
print(sorted_numbers)