def snake(name):
    for i in name:
        if i.isupper() == True:
            print("_", i.lower(), end="", sep="")
        else:
            print(i, end="")

camel = input("camelCase: ")
print("snake_case: ", end="")
snake(camel)
print()


