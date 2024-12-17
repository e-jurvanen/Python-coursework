ans = input("What's the answer to the Great Question? ")

if ans.strip() == "42":
    print("Yes")
elif ans.lower().strip() == "forty-two":
    print("Yes")
elif ans.lower().strip() == "forty two":
    print("Yes")
else:
    print("No")
