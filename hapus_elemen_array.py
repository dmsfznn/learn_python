#  Python  program  to  demonstrate 
# Removal of elements in a Array
#  Importing  "array"  for  array  operations import array
import array as arr

#  Initializing  array  with  array  values
#  Initializing  array  with  signed  integers arr  =  array.array('i',  [1,  2,  3,  1,  5])
arr = arr.array('i', [1, 2, 3, 1, 5])

#  Printing  original  array
print  ("The  new  created  array  is  :  ",  end  ="") 
for  i  in  range  (0,  5):
    print  (arr[i],  end  ="  ") 
print ("\r")
#  Using  pop()  to  remove  element  at  2nd  position print  ("The  popped  element  is  :  ",  end  ="") print  (arr.pop(2))
print ("The  popped element  is  :  ",  end  ="")
print  (arr.pop(2))

#  Printing  array  after  popping
print  ("The  after  poppimh  is  :  ",  end  ="") 
for  i  in  range  (0,  4):
    print  (arr[i],  end  ="  ") 
print ("\r")
#  Using  remove()  to  remove  1st  occurance  of  1 arr.remove(1)
arr.remove(1)

#  Printing  array  after  removing
print  ("The  array  after  removing  is  :  ",  end  ="") 
for  i  in  range  (0,3):
    print  (arr[i],  end  ="  ")
    
# Selesai 4.3
