#  Python  program  to  demonstrate 
# # Silicing of elemts in a Array

#  Importing  array  module import array as arr
import array as arr


# Creating a list
l  =  [1,  2,  3,  4,  5,  6,  7,  8,  9,  10]

a  =  arr.array('i',  l) 
print("Intial Array : ") 
for i in (a):
    print(i, end =" ")

#  Print  elements  of  a  range 
# #  Using  slice  operation Sliced_array  =  a[3:8]
print("\nSlincing  elements  in  a  range  3-8:  ") 
print((a[3:8]))

#  Print  elements  from  a
# Pre-defined point to end Sliced_array  =  a[5:] 
# print("\nElements  sliced  from  5th  ""element  till  the  end:  ") 
print(a[5:])

#  Printing  elements  from # beginning till end Sliced_array = a[:]
print("\nPrinting  all  elements  using  slice  operation:  ")
print(a[:])

# Selesai 4.4
