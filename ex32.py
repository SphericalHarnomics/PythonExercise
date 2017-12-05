the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','qpricots']
change = [1,'Pennis',2,'dimes',3,'quarters']

for number in the_count:
    print "This is count : %d" % (number)

for fruit in fruits:
    print "A fruit of type : %s" % (fruit)
    # if using %r as output format, we will get 'apples' etc...

 # print mixed list
for i in change:
    print "I got : %r" % (i)

# We can also build lists, first start with an empty one.
elements = []

# Then se the range function to do 0-5 counts:
for i in range(0,6):
    print "Adding %d to the list." % (i)
    # append is a function that list understand
    elements.append(i) # append element in tail position

#Now we can print them out too
for i in elements:
    print "Element was: %d" % (i)

print "Element are : %s " % elements


element2 = range(0,6)
print "Element2 are : %s " % element2


