def get_last_char(text):

    return text[-1]

text = 'Sommer is comming'
print(get_last_char(text))


def name_1():
    return 'Alexander'

name_1 = name_1()
print(name_1)


def marke_auto():

    marke = 'Mersedes, Land Rover'
    return marke.upper()

print(marke_auto())


def pow(x, base = 2):
    return x ** base

print(pow(3, 3))


def f(a=1, b=2, c=None, d=4):
    print(a, b, c, d)

f(1, 2, None, 8)
f(d=8)
f(3, d=3)