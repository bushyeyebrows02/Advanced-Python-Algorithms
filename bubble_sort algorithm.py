#implementing a bubble_sort algorithm

#first start by defining a function that takes an array as an arguement
def bubble_sort(arr):
    # getting the length of an array
    n = len(arr)
    #Now the algorithm has to traverse throughout the array elements in order to sort them.
    #do this by creating a nested loop.
    
    #Outter loop
    #The outter loop controls the number of passes through the array. ensuring that in each pass
    # the largest unsorted value is moved to its correct position. 
    for i in range(n-1):
        print(f"pass{i+1}:")
        #last i elements are already sorted
        #inner loop.
        #the Inner loop compares the adjacent elements & swappes them
        for j in range(n-i-1):
            #swapping
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"After comparing index {j} and {j+1}:{arr}")
        print(f"End of Pass {i+1}: {arr}")
    return arr

numbers = [64,34,25,22,11,90]
print("Unsorted Array:", numbers)
sorted_numbers = bubble_sort(numbers)
print("Sorted array:", sorted_numbers)

#This bubble_sort algorithm can be improved further for it to effeciently handle
#even Arrays that are small in size. This can be done by modifying the loop specifically
#like so

my_array =[7, 3, 9, 12, 11]
#remember to get the length of the array
n = len(my_array)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array{j+1] = my_array[j+1], my_array[j]
            swapped = True
    if not swapped:
        brak
print("sorted array," my_array)
            
        