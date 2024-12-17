# count the energy with the given mass

def energy(m):
    e = m * 300000000**2
    return e

# ask for input, call for energy calculation, print answer

def main():
    mass = int(input("m: "))
    print("E:", energy(mass))

main()
