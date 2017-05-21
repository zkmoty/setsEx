# add() adds an element to s set, if it is not already in it
# >>> s = set([3, 4])
# >>> s.add(5)
# >>> s
# set([3, 4, 5])
# >>> s.add(4)
# >>> s
# set([3, 4, 5])

# the result is True if the left set is contained in the right set
# >>> set([3, 4]) < set ([4, 5])
# False
# >>> set([3, 4]) < set ([3, 4, 5])
# True
# >>> set([3, 4]) < set ([3, 4])
# False
# >>> set([3, 4]) <= set ([3, 4])
# True

# iterating through a set
# >>> for n in set([3, 4, 5]):
# ...     print(n)
# ...
# 3
# 4
# 5

import school

# some new kids got to town and want to go to our school's 3rd grade,
# but we can only accept them if we teach the extra classes they used
# to take back in their previous schools.

# ----- ENTER SOME CODE HERE --------
third_grade_updated = {'I should be a set of the pupils in the 3rd grade, after we accept the pupils we can. FIX ME'}
# -----------------------------------


print(third_grade_updated)
assert third_grade_updated == {
    'Kobi Cohen', 'Charlie Berger', 'Douglas Pardo', 'Brett Mclean', 'Levi Levi',
    'Danny Koehler', 'Dorothy Welton', 'Eunice Lawler', 'Dennis Galicia', 'Brenda Hewitt',
    'Larry Coffin', 'Tammy Vilven'
}
