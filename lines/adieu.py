import inflect

p = inflect.engine()

def main():
    names = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break
    print("Adieu, adieu, to " + p.join(names, final_sep=","))

main()
