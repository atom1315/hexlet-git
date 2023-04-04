result = 5 > 4
print(result)
print('one' != 'one')


def is_infant(age):
    return age < 2
print(is_infant(1))


def is_castle(string):
    return string == 'Castle'

print(is_castle('Castle'))


def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(3))


def is_first_letter_an_(string):
    first_letter = string[1]
    return first_letter == 'p'
print(is_first_letter_an_('orange'))
print(is_first_letter_an_('apple'))