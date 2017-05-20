__author__ = 'July'

# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html
class t1:
    def quickSort(self, alist):
       self.quickSortHelper(alist,0,len(alist)-1)

    def quickSortHelper(self, alist,first,last):
       if first<last:

           splitpoint = self.partition(alist,first,last)

           self.quickSortHelper(alist,first,splitpoint-1)
           self.quickSortHelper(alist,splitpoint+1,last)


    def partition(self, alist,first,last):
       pivotvalue = alist[first]

       leftmark = first+1
       rightmark = last

       done = False
       while not done:

           while leftmark <= rightmark and \
                   alist[leftmark] <= pivotvalue:
               leftmark = leftmark + 1

           while alist[rightmark] >= pivotvalue and \
                   rightmark >= leftmark:
               rightmark = rightmark -1

           if rightmark < leftmark:
               done = True
           else:
               temp = alist[leftmark]
               alist[leftmark] = alist[rightmark]
               alist[rightmark] = temp

       temp = alist[first]
       alist[first] = alist[rightmark]
       alist[rightmark] = temp


       return rightmark

alist = [54,26,93,17,77,31,44,55,20]
t1().quickSort(alist)
print(alist)


# http://hetland.org/coding/python/quicksort.html
class t2:
# Written by Magnus Lie Hetland
# "Everybody's favourite sorting algorithm... :)"

    def partition(self, list, start, end):
        pivot = list[end]                          # Partition around the last value
        bottom = start-1                           # Start outside the area to be partitioned
        top = end                                  # Ditto

        done = 0
        while not done:                            # Until all elements are partitioned...

            while not done:                        # Until we find an out of place element...
                bottom = bottom+1                  # ... move the bottom up.

                if bottom == top:                  # If we hit the top...
                    done = 1                       # ... we are done.
                    break

                if list[bottom] > pivot:           # Is the bottom out of place?
                    list[top] = list[bottom]       # Then put it at the top...
                    break                          # ... and start searching from the top.

            while not done:                        # Until we find an out of place element...
                top = top-1                        # ... move the top down.

                if top == bottom:                  # If we hit the bottom...
                    done = 1                       # ... we are done.
                    break

                if list[top] < pivot:              # Is the top out of place?
                    list[bottom] = list[top]       # Then put it at the bottom...
                    break                          # ...and start searching from the bottom.

        list[top] = pivot                          # Put the pivot in its place.
        return top                                 # Return the split point


    def quicksort(self, list, start, end):
        if start < end:                            # If there are two or more elements...
            split = self.partition(list, start, end)    # ... partition the sublist...
            self.quicksort(list, start, split-1)        # ... and sort both halves.
            self.quicksort(list, split+1, end)
        else:
            return


if __name__=="__main__":                       # If this script is run as a program:
    #import sys
    #list = map(int,sys.argv[1:])               # Get all the arguments
    list = [54,26,93,17,77,31,44,55,20]
    start = 0
    end = len(list)-1
    t2().quicksort(list,start,end)                  # Sort the entire list of arguments
    import string
    print string.join(map(str,list))           # Print out the sorted list