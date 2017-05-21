# is that kind of what you meant by "בנוסף - העבודה העלתה לי רעיון - לתת לתלמידים לממש משהו כמו
# assert_set_equals שעבור שתי קבוצות מדפיסות יפה מה ההבדל ביניהן.???" ?


def assert_set_equals(set1, set2):
    difference = ''
    for i, d1 in enumerate(set1 - set2):
        difference += 'difference number {}: '.format(i + 1)
        difference += '{} is in first set, not in second set\n'.format(d1)
    for j, d2 in enumerate(set2 - set1):
        # As someone who writes Python often, does the usage of i is totally ugly in
        # this context/scope? (by using something 'broken' in the language - that i is
        # recognized out of scope) or does it count OK style-wise?
        difference += 'difference number {}: '.format(j + i + 2)
        difference += '{} is in second set, not in first set\n'.format(d2)
    return difference if difference else 'identical sets!'
