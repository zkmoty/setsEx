import school


# this function should return a list with the names of the pupils in the given grade,
# ordered by alphabetical order.
# input - a set including the names of the pupils in the grade
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
# will go to the literature trip. return a list of the pupils who are going to the trip,
# ordered by alphabetical order
# input - pupils sets.
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


# An external teacher is coming to lecture in our school, to pupils who study in
# both a technology group and a literature group.
# As 1st & 2nd grade pupils can go to none, one, or both of the first literature
# group and the first technology group,
# and 3rd & 4th grade pupils can go to none, one, or both of the second literature
# group and the second technology group,
# you are going to write a function that returns a list with the names of the pupils
# who take both literature and technology classes.
# input - sets, each one corresponding to its name.
def take_both_extra_classes(first_literature_group, second_literature_group,
                            first_technology_group, second_technology_group):
    # ----- ENTER SOME CODE HERE --------
    return sorted((first_technology_group & first_literature_group) |
                  (second_technology_group & second_literature_group))
    # -----------------------------------


assert take_both_extra_classes(school.first_literature_group,
                               school.second_literature_group,
                               school.first_technology_group,
                               school.second_technology_group) == ['Mary Warren', 'Scott Kipp']


# The principle will lecture to pupils who take no extra classes (literature, technology)
# about the importance of expanding your horizons.
# write a function that returns a sorted list of the names of the pupils who take no extra classes.
# # input - sets, each one corresponding to its name.
def take_no_extra_classes(first_grade, second_grade, third_grade, fourth_grade,
                          first_technology_group, second_technology_group,
                          first_literature_group, second_literature_group):
    # ----- ENTER SOME CODE HERE --------
    return sorted(((first_grade | second_grade) - (first_technology_group | first_literature_group)) |
                  ((third_grade | fourth_grade) - (second_technology_group | second_literature_group)))
    # -----------------------------------


assert take_no_extra_classes(school.first_grade, school.second_grade, school.third_grade, school.fourth_grade,
            school.first_technology_group, school.second_technology_group,
            school.first_literature_group, school.second_literature_group) == ['Carl Hale', 'Ronald Tucker']


# return a sorted list of the pupils who take exactly one extra class.
# input - sets, each one corresponding to its name.
def take_one_extra_class(first_literature_group, second_literature_group,
                         first_technology_group, second_technology_group):
    # ----- ENTER SOME CODE HERE --------
    return sorted((first_literature_group ^ first_technology_group) |
                  (second_literature_group ^ second_technology_group))
    # -----------------------------------


assert take_one_extra_class(school.first_literature_group, school.second_literature_group,
                            school.first_technology_group, school.second_technology_group) == \
       ['Brenda Hewitt', 'Brett Mclean', 'Brittany Clement', 'Bryan Ortiz', 'Cecil Massa', 'Charles Stone',
        'Charlie Berger', 'Danny Koehler', 'David Saldivar', 'Dennis Galicia', 'Dorothy Welton', 'Douglas Pardo',
        'Eunice Lawler', 'Gabriel Hancock', 'Helen Wilson', 'Jenifer Baldwin', 'John Sales', 'Joyce Valadez',
        'Kim Meriwether', 'Kimberly Petti', 'Larry Coffin', 'Michael Findley', 'Michele Trowbridge', 'Nancy Smith',
        'Pamela Burris', 'Rafael Dinger', 'Rafael Honkanen', 'Rhonda Moreno', 'Robin Gutkowski', 'Roger Miller',
        'Roy Moore', 'Ruth Weiss', 'Tammy Vilven', 'Tisha Britton', 'Velma Mitchell', 'Whitney Mcelyea']


# some new kids got to town and want to go to our school's 3rd grade,
# but we can only accept them if we teach the extra classes they used
# to take back in their previous schools.
# return a set of the pupils in 3rd grade, after we accept the pupils we can.
# input -
# third_grade - a set, including the names of all the pupils in the 3rd grade
# new_kids - a set of tuples, each represents a kid and consists of 2 entries: the first
# one is the name of the kid(string) and the second one is a set of
# the extra classes he takes.
# input - sets, each one corresponding to its name.
def add_new_pupils(third_grade, new_kids):
    # ----- ENTER SOME CODE HERE --------
    for name, extra_lessons in new_kids:
        if extra_lessons <= {'literature', 'technology'}:
            third_grade.add(name)
    return third_grade
    # -----------------------------------


assert add_new_pupils(school.third_grade, school.new_3rd_grade_kids) == \
       {'Kobi Cohen', 'Charlie Berger', 'Douglas Pardo', 'Brett Mclean', 'Levi Levi',
        'Danny Koehler', 'Dorothy Welton', 'Eunice Lawler', 'Dennis Galicia', 'Brenda Hewitt',
        'Larry Coffin', 'Tammy Vilven'}


# implement a function that compares two sets and prints the differences between them
def assert_set_equals(set1, set2):
    differences = []
    difference_counter = 0
    for diff in sorted(set1 - set2):
        difference_counter += 1
        differences.append('+{!r}'.format(diff))
    for diff in sorted(set2 - set1):
        difference_counter += 1
        differences.append('-{!r}'.format(diff))
    return '\n'.join(differences) if differences else 'identical sets!'


print(assert_set_equals(school.fourth_grade, school.second_literature_group))
assert assert_set_equals(school.fourth_grade, school.second_literature_group) == '\n'.join([
    "+'Gabriel Hancock'",
    "+'John Sales'",
    "+'Michele Trowbridge'",
    "+'Rafael Honkanen'",
    "+'Rhonda Moreno'",
    "-'Brett Mclean'",
    "-'Charlie Berger'",
    "-'Douglas Pardo'",
    "-'Larry Coffin'",
    "-'Tammy Vilven'",
])


print(assert_set_equals(school.fourth_grade, school.fourth_grade))
assert assert_set_equals(school.fourth_grade, school.fourth_grade) == 'identical sets!'
