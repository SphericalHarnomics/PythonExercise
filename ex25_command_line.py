import ex25  # no need to add .py
print("Hello World!")

sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)
print "(variable)word is now %s:" % (words) # see ['All', 'Good.....]

sorted_words = ex25.sort_words(words) # remember to add words
print "(variable)sorted_words is now %s:"% (sorted_words)

ex25.print_first_word(words)
ex25.print_last_word(words)
print "after pop twice, (variable)word is now : %s" % (words)

ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
print "after pop twice (variable)sorted_words is now: %s" % (sorted_words)

ex25.print_first_and_last(sentence)
ex25.print_first_and_last_sorted(sentence)


