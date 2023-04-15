def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':
        return 'question'
    return 'normal'

print(get_type_of_sentence('Hodor'))



def name_eltern(sentence):
    last_transcription = sentence[-1]
    if last_transcription == '?':
        return 'question'
    return 'normal'



print(name_eltern('Mariya?'))


def working_office(time):
    go_home = time
    if go_home == 17.00:
        return 'its ok'
    return 'close office'

print(working_office(19.00))


def get_type_of_sentence(sentence):
    last_char = sentence[-1]
    if last_char == '?':                     # !=
        sentence_type = ' question '
    else:
        sentence_type = ' normal '

    return "Sentence is" + sentence_type

print(get_type_of_sentence('Hodor?'))


def working_office(time):
    go_home = time
    if go_home == 17.00:
        time_type = ' it´s ok '
    else:
        time_type = ' close office '

    return 'Time type' + time_type

print(working_office(19.00))



def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = ' question '

    if last_char == '!':
        sentence_type = ' exclamation '

    else:
        sentence_type = ' normal '

    return 'Sentence is' + sentence_type

print(get_type_of_sentence('No!'))


def get_type_of_sentence(sentence):
    last_char = sentence[-1]

    if last_char == '?':
        sentence_type = 'question'
    elif last_char == '!':
        sentence_type = 'exclamation'
    else:
        sentence_type = 'normal'

    return 'Sentence is ' + sentence_type


print(get_type_of_sentence('No'))
print(get_type_of_sentence('No!'))


