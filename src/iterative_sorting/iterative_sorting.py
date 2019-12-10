# TO-DO: Complete the selection_sort() function below

def selection_sort(arr):
    #-1 becaus3e once you get to the end of the array you
    #don't need to do another comparison
    for i in range(0, len(arr) -1):
        #Via iteration, find the smallest element
        #set the first index of the iteration as the min
        minIndex = i
        #on next iteration, start with the next index,
        #i + 1 because we are only iterating the right side
        #of the list from the last min index
        for j in range(i + 1, len(arr)):
            #compare elements
            if arr[i] < arr[minIndex]:
                # start to swap elements
                minIndex = j
            #at the end of the iteration switch values
            #if you find an item that has a lower value we need to switch
            if minIndex != i:
            #swap elements
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    #indexing length of where to make comparisons
    #minus one because you can't make a comparison at the end of the array
    indexing_length = len(arr) - 1
    #using this sorted variable inside of control flow to break out when list is sorted
    sorted = False
    #while loop for infinite number of iterations
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            #run comparison
            if arr[i] > arr[i+1]:
                sorted = False
                #switch elements
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


# STRETCH: implement the Count Sort function below
#Use when you know something about the input
def counting_sort(nums):
    counts = {}
    for n in nums:
        if n not in counts:
            counts[n] = 0
        counts[n] += 1
    sorted_ = []
    for n, count in sorted(counts.items()):
        for i in range(count):
            sorted_.append(n)
    return sorted
