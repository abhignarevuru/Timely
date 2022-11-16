# Inspired from meal.py in CS50Python

def main():
    user_time = convert(input("What time is it? "))
    if 7 <= user_time <= 8:
        print("breakfast time")
    elif 12 <= user_time <= 13:
        print("lunch time")
    elif 18 <= user_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes/60)

if __name__ == "__main__":
    main()
