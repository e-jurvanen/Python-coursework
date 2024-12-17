groceries = {}

def main():
    while True:
        try:
            item = input().upper().strip()
            if item in groceries:
                groceries[item] = groceries[item] + 1
            else:
                groceries[item] = 1
        except KeyError:
            pass
        except EOFError:
            break
    for item in sorted(groceries):
        print(groceries[item], item)


main()

