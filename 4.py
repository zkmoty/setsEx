# An element is in the result set if it is in the left set and not in the right set, or
# in the right set and not in the left set
# >>> set([3, 4]) ^ set ([4, 5])
# set([3, 5])

import school


# ----- ENTER SOME CODE HERE --------
take_one_extra_class = {'I should be a set of the pupils who take exactly one extra class. FIX ME'}
# -----------------------------------


print(take_one_extra_class)
assert take_one_extra_class == {
    'Brenda Hewitt', 'Brett Mclean', 'Brittany Clement', 'Bryan Ortiz', 'Cecil Massa', 'Charles Stone',
    'Charlie Berger', 'Danny Koehler', 'David Saldivar', 'Dennis Galicia', 'Dorothy Welton', 'Douglas Pardo',
    'Eunice Lawler', 'Gabriel Hancock', 'Helen Wilson', 'Jenifer Baldwin', 'John Sales', 'Joyce Valadez',
    'Kim Meriwether', 'Kimberly Petti', 'Larry Coffin', 'Michael Findley', 'Michele Trowbridge', 'Nancy Smith',
    'Pamela Burris', 'Rafael Dinger', 'Rafael Honkanen', 'Rhonda Moreno', 'Robin Gutkowski', 'Roger Miller',
    'Roy Moore', 'Ruth Weiss', 'Tammy Vilven', 'Tisha Britton', 'Velma Mitchell', 'Whitney Mcelyea'
}
