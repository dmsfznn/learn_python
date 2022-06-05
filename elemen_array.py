#  Python  program  to  demonstrate 
#  Adding  elements  to  a  Array
#  Importing  "array"  for  array  creations import array as arr
import array as arr

# Array with int type
a  =  arr.array('i',  [1,  2,  3])

print("Array  before  insertion  :  ",  end  ="  ") 
for  i  in  range  (0,  3):
    print  (a[i],  end  =  "  ") 
print()

#  Inserting  array  using #  Insert()  function a.insert(1,  4)

print  ("Array  after  insertion  :  ",  end  ="  ") 
for i in (a):
    print (i, end =" ") 
print()

#  Array  with  float  type
b  =  arr.array('d',  [2.5,  3.2,  3.3])
print ("Array before insertion : ", end =" ") 
for  i  in  range  (0,  3):
    print  (b[i],  end  ="  ") 
print()

#  Adding  an  element  using  append() b.append(4.4)

print  ("Array  after  insertion  :  ",  end  ="  ") 
for i in (b):
    print (i, end =" ")
print()

# Selesai 4.1
