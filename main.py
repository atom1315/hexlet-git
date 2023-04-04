def parameter_man():
    name = 'Alexander Hirsch'
    old_time = 43
    function_all = f"{name}, I am  {old_time} years old."

    print(function_all)

def parameter_man2(old_time,name="tom"):


    function_all = f"{name}, I am  {old_time} years old."

    print(function_all)


#parameter_man2(20,"Mark")
#parameter_man2(24,"maxi")
#parameter_man2(78)

def wahl(alter):
    if(alter>=18):
        print("Sie sind wahlberechtigt")
    elif(alter<18 and alter>0):
        print("nicht wahlberechtigt :Sie müssen",(18-alter)," jahre warten")
    else:
        print("fehler")
wahl(20)
wahl(24)



def begrüssung(name,geschlecht):
    if(geschlecht == "w"):
        print('Hallo Frau ',name)
    elif(geschlecht == 'm'):
        print('Hello Herr', name)
    else:
        print('fehler')
begrüssung('Marija', 'm')
#begrüssung('Alexandr', 'w')

def wahl_2(name,alter,geschlecht):
    begrüssung(name,geschlecht)
    wahl(alter)

wahl_2('Peter' ,2, 'm')