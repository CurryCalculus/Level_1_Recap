seconds = float(input("Enter the number of seconds between lightning and thunder: "))

speed_of_sound = 340
distance = seconds * speed_of_sound

print(f"The storm is approximately {distance:.2f} meters away.")
