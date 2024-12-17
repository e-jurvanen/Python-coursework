#make a function to promt for input, call convert and print

def main():
    inp = input("What would you like to say? ")
    new_inp = convert(inp)
    print(new_inp)

#make a function to convert emoticons to emoji

def convert(emoji):
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    return emoji

main()

