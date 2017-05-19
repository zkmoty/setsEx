import school


# this function should return a list with the names of the pupils in the given grade, ordered by alphabetical order
def grade_in_alphabetical_order(grade):
    # ----- ENTER SOME CODE HERE --------
    return sorted(grade)
    # -----------------------------------

assert grade_in_alphabetical_order(school.first_grade) == \
       ['Bryan Ortiz', 'David Saldivar', 'Helen Wilson', 'Jenifer Baldwin', 'Kim Meriwether',
     'Michael Findley', 'Pamela Burris', 'Roger Miller', 'Roy Moore', 'Whitney Mcelyea']

assert grade_in_alphabetical_order(school.fourth_grade) == \
       ['Brittany Clement', 'Charles Stone', 'Gabriel Hancock', 'John Sales', 'Mary Warren',
        'Michele Trowbridge','Rafael Honkanen', 'Rhonda Moreno', 'Scott Kipp', 'Velma Mitchell']


# This year, pupils who are either in the fourth grade or study in one of the two literature classes,
# will go to the literature trip. return a list list of the pupils who are going to the trip,
# ordered by alphabetical order
def going_to_the_trip(fourth_grade, first_literature_group, second_literature_group):
    # ----- ENTER SOME CODE HERE --------
    return sorted(fourth_grade | first_literature_group | second_literature_group)
    # -----------------------------------


assert going_to_the_trip(school.fourth_grade, school.first_literature_group, school.second_literature_group) == \
       ['Brett Mclean', 'Brittany Clement', 'Bryan Ortiz', 'Cecil Massa', 'Charles Stone',
        'Charlie Berger', 'David Saldivar', 'Douglas Pardo', 'Gabriel Hancock', 'Helen Wilson',
        'John Sales', 'Joyce Valadez', 'Kim Meriwether', 'Larry Coffin', 'Mary Warren',
        'Michele Trowbridge', 'Rafael Dinger', 'Rafael Honkanen', 'Rhonda Moreno', 'Robin Gutkowski',
        'Roy Moore', 'Ruth Weiss', 'Scott Kipp', 'Tammy Vilven', 'Velma Mitchell']

