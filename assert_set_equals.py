import school


# implement a function that compares two sets and prints the differences between them
def assert_set_equals(set1, set2):
    # ------------- YOUR CODE HERE ---------
    return "FIX_ME"
    # --------------------------------------


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