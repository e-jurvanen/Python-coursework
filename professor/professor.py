import random

def main():
    lev = get_level()
    tries = 3
    correct = 0

    for i in range(0,10):
        x = generate_integer(lev)
        y = generate_integer(lev)
        tries = 3
        while tries > 0:
            user_ans = input(f"{x} + {y} = ")
            ans = int(x + y)
            try:
                if int(user_ans) != ans:
                    print("EEE")
                    tries -= 1
                    if tries == 0:
                        print(f"{x} + {y} = {ans}")
                else:
                    correct += 1
                    break
            except ValueError:
                print("EEE")
                tries -= 1
                if tries == 0:
                    print(f"{x} + {y} = {ans}")

    print(correct)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError
    else:
        no = ""
        if level == 1:
            no = no + str(random.randint(0, 9))
        if level == 2:
            no = no + str(random.randint(10, 99))
        if level == 3:
            no = no + str(random.randint(100, 999))



        return int(no)

if __name__ == "__main__":
    main()
