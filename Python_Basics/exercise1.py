import time

current_hour = time.localtime().tm_hour

if 5 <= current_hour < 12:
    print(f"good morning".title())
elif 12 <= current_hour < 17:
    print(f"good afternoon".title())
elif 17 <= current_hour < 21:
    print(f"good evening".title())
else:
    print("Good Night!")

timestamp = time.strftime('%H:%M:%S')
print(timestamp)