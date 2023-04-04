age = 5

def generate():
    return age + 3
result = generate()
print(result)




age = 5

def generate():
    age = 10
    return age + 3
result = generate()
print(result)


age = 5

def generate():
    age = 8
    generate()

result = age

print(result)



