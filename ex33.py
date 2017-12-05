def new_function(maxNumber):
    number_list = []

    return maxNumber, number_list

maxNumber, number_list = new_function(5)

print "maxNumber is %d, number_list is %r" % (maxNumber, number_list)

print "(A new way)maxNumber is %d, number_list is %r" % new_function(5)