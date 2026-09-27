print("===== Train Ticket Booking =====")

name = input("Enter your name: ")
city = input("Enter your city: ")
destination = input("Enter destination: ")

print("\nAvailable Trains:")
print("1. Bhopal Express")
print("2. Shatabdi Express")
print("3. Rajdhani Express")

choice = int(input("Select train (1-3): "))

if choice == 1:
    train = "Bhopal Express"
    fare = 500
elif choice == 2:
    train = "Shatabdi Express"
    fare = 800
elif choice == 3:
    train = "Rajdhani Express"
    fare = 1000
else:
    print("Invalid choice")
    exit()

print("\n===== Booking Details =====")
print("Passenger:", name)
print("From:", city)
print("To:", destination)
print("Train:", train)
print("Fare: Rs.", fare)

print("\nTicket booked successfully!")
