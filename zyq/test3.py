#!/usr/bin/python
# -*- coding:UTF-8 -*-

array = [5,8,2,9,12,10,4,1,3]
#print len(array)
def quit_sort(array,L,R):
    i,j = L,R
    x = array[L]
    while i<j:
        while i<j and array[j]>=x:
            j = j - 1
        if i<j:
            array[i] = array[j]
        while i<j and array[i]<=x:
            i = i + 1
        if i<j:
            array[j] = array[i]
    array[j] = x
    if(L<i):
        quit_sort(array,L,i-1)
    if(R>j):
        quit_sort(array,j+1,R)

quit_sort(array,0,len(array)-1)

print array