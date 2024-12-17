def main():
    time = input("What time is it? ")
    new_time = convert(time)

    if 7.0 <= new_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= new_time <= 13.0:
        print("lunch time")
    elif 18.0 <= new_time <= 19.0:
        print("dinner time")

def convert(x):
    hours, minutes = x.split(":")
    minutes = float(minutes) / 60
    n_t = float(int(hours) + float(minutes))
    return n_t

if __name__ == "__main__":
   main()

