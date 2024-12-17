greet = input("Greeting: ")

if greet.lower().strip().startswith("hello") == True:
    print("$0")
elif greet.lower().strip().startswith("h") == True:
    print("$20")
else:
    print("$100")
