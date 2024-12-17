import random

level = 5
no = "hey"
while level > 0:
    no = no + str(random.randint(0, 9))
    level -= 1
print(no)
