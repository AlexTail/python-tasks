"""

Ru: Двоичный (бинарный) поиск

Eng: Binary Search

"""


def binarysearch(mylist, iskat, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if iskat == mylist[mid]:
            return mid
        elif iskat < mylist[mid]:
            return binarysearch(mylist, iskat, start, mid - 1)
        else:
            return binarysearch(mylist, iskat, mid + 1, stop)

mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]
iskat = 77
start = 0
stop =len(mylist)

x = binarysearch(mylist, iskat, start, stop)

if x == False:
    print("Item", iskat, "Not Found!")
else:
    print("Item", iskat, "Found at index:", x)