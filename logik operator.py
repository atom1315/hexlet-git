def is_correct_password(password):
    length = len(password)
    return length > 8 and length < 20

print(is_correct_password('qwerty'))
print(is_correct_password('qwerty1234'))




import string

def has_special_chars(str):
    return any(ch for ch in str if ch in string.punctuation)

print(has_special_chars('dfdrer1111ch'))


def is_strong_password(password):
    length = len(password)

    return(length > 8 and length < 20) and has_special_chars(password)

print(is_correct_password('ffff111dddddd'))



def is_good_apartaments(area, street):
    return area >= 100 or (area >= 80 and street == 'Main Street')

print(is_good_apartaments(91, 'Qween Street'))
print(is_good_apartaments(120, 'Main Street'))



def if_auto(number):
    length = len(number)
    return length > 8 and length < 10

print(not if_auto('w1232245k'))





print(10 / 2 == 5 and 'yes' or 'no')
print(11 / 2 == 0 and 'yes' or 'no')


