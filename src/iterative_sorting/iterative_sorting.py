# # TO-DO: Complete the selection_sort() function below

def selection_sort(list_to_sort):
    # the first element is already in the "sorted side"
    # (abstract idea, no code required)
    # for all other items, do something
    # starting at the second item, interate unit we hit the end of the list
    for i in range(1, len(list_to_sort)):
        # the current number represents the value currently being sorted
        current_num = list_to_sort[i]
        # move the current number back through the array (to the "sorted side")
        j = i
        # Keep moving unitl: it's greter than then number before it OR  we reach the start of array (index is zero)
        while j > 0 and current_num < list_to_sort[j-1]:
            # replace the current value with the one to the left of it (swap them)
            list_to_sort[j] = list_to_sort[j-1]
            j -= 1
        # set the value at the current index to the current number
        # at this moment, J rperesents the new location for the current numbert
        list_to_sort[j] = current_num

    return list_to_sort

# print(selection_sort([8,4,2,5,1,3]))

nums = [2,6,8,3,4,1,9,5,7]
def insert_sort(nums):
    # 1st element is  a sorted list of '1'
    # loop through 'unsorted' elelemnts
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i
        # while 'n' > LHS OR index of 'n' is NOT 0
        # while we're not at the begining AND
        while j > 0 and temp < nums[j-1]:
            nums[j] = nums[j-1]
:

            j -= 1
        nums[j] = temp

    return nums
print(nums)
sorted_nums = insert_sort(nums[:])
print(nums)
print(sorted_nums)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    list_length = len(arr)

    # traverse the elements in the list
    for i in range(list_length - 1):
        for j in range(0, list_length-i-1):
            # if the element at arr[j] is greater than the next, swap their values
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]


    return arr


# # NOT MY SOLUTION
# def bubble_sort(arr):
#     isSorted = False  # assume the arr is not sorted
#     counter = 0 #set a counter to reduce traversing the entire array on each pass. 
#     while not isSorted:
#         isSorted = True #temporarly assume the array is sorted until for loop runs
#         for i in range(len(arr) - 1 - counter):
#             if arr[i] > arr[i + 1]: #check to see if positon before is greater than next position if so 
#                 swap(i, i + 1, arr) #run swap helper function to switch index of i with index of i +1 
#                 isSorted = False #set isSorted back to false due to making a swap
#         counter += 1 #increment counter by one so that the second pass does not go over the entire array again
#     return arr
# def swap(i, j, arr):
#     arr[i], arr[j] = arr[j], arr[i]

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''

# def counting_sort(arr):
#     """in-place counting sort"""
#     # sort according to keys
#     # counting the elements having distinc key values

#     # first case all elemnts 0 <= a[?] <= k
#     total_indexes = len(arr)-1
#     max_val = max(arr)
#     return arr


# counting_sort([1,2,3,5])




        self.set_light_on()
        
        # so robot will be in while loop until it finishes off the sorting
        while self.light_is_on():
            # robot will swipe with his NONE card, with first card as starter and this will be back, NONE card will sequencely  
            self.swap_item()
            # check if there is right first 
            while self.can_move_right():
                #move the robot next to right
                self.move_right()
                # if robot's card atm is bigger than a card in current place then swipe.  
                if self.compare_item() == 1:
                    self.swap_item()
            # after robot picks change the chard then turn it off so it will go to other while loop.
            self.set_light_off()

            # robot will go left while its light is off
            while not self.light_is_on():
                #keep moving left until it's None
                while self.compare_item() is not None:
                    self.move_left()
                #if robot meets NONE card then swap a current position's card.
                self.swap_item()
                # turn the light on again so it will go back to first top while loop. 
                self.set_light_on()
            #before going to the first while loop, make sure to move the robot to right once so NONE card will shift to next position place. 
            self.move_right()
            # so if robot hits dead end of right and robot has NONE card it will finish off the task
            if self.compare_item() is None and not self.can_move_right():
                #used return here on purpose so it wont return NONE and the light will be off as well. 
                return self.set_light_off()