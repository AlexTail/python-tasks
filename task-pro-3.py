"""

Ru: Сортировка Пузырьком 

Eng: Bubble sort

"""

oldlist = [10, 5, 92, 85, 24, 23, 8, 203, 14, 67]

def bubble_sort(mylist):
    last_item = len(mylist) - 1
    for z in range(0, last_item):
        for x in range(0, last_item-z):
            if mylist[x] > mylist[x+1]:
                mylist[x], mylist[x+1] = mylist[x+1], mylist[x]
    return mylist

print('Oldlist =', oldlist)
newlist = bubble_sort(oldlist).copy()
print('Newlist =', newlist)