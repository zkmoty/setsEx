# intersection of sets:
# An element is in the result set if it is in one of the two sets
# >>> set([3, 4]) & set ([4, 5])
# set([4])

import school

# An external teacher is coming to lecture in our school, to pupils who study in
# both a technology group and a literature group.
# As 1st & 2nd grade pupils can go to none, one, or both of the first literature
# group and the first technology group,
# and 3rd & 4th grade pupils can go to none, one, or both of the second literature
# group and the second technology group.

# ------------- YOUR CODE HERE ---------
take_both_extra_classes = {'I should be a set of the pupils who take both literature and technology classes. FIX ME'}
# --------------------------------------


print(take_both_extra_classes)
assert take_both_extra_classes == {
    'Mary Warren', 'Scott Kipp'
}
