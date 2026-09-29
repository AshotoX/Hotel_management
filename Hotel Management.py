rooms = [
    [101, 0, "", ""],
    [102, 0, "", ""],
    [103, 0, "", ""],
    [104, 0, "", ""],
    [105, 0, "", ""],
    [106, 0, "", ""],
    [107, 0, "", ""],
    [108, 0, "", ""]
]


def read_number(message):
    text = input(message)

    if text == "":
        return -1

    number = 0
    index = 0

    while index < len(text):
        character = text[index]

        if character in "0123456789":
            number = number * 10 + int(character)
            index = index + 1
        else:
            return -1

    return number


def find_room(room_table, room_number):
    index = 0

    while index < len(room_table):
        if room_table[index][0] == room_number:
            return index
        index = index + 1

    return -1


def show_rooms(room_table):
    print("")
    print("ROOM STATUS")
    print("-----------")

    index = 0
    while index < len(room_table):
        room = room_table[index]

        if room[1] == 0:
            status = "Available"
        elif room[1] == 1:
            status = "Reserved"
        else:
            status = "Checked in"

        print("Room " + str(room[0]) + ": " + status)
        index = index + 1


def show_guest_details(room_table):
    print("")
    print("GUEST DETAILS")
    print("-------------")

    found_guest = False
    index = 0

    while index < len(room_table):
        room = room_table[index]

        if room[1] == 1 or room[1] == 2:
            if room[1] == 1:
                status = "Reserved"
            else:
                status = "Checked in"

            print("Room number: " + str(room[0]))
            print("Guest name: " + room[2])
            print("Phone number: " + room[3])
            print("Status: " + status)
            print("")
            found_guest = True

        index = index + 1

    if not found_guest:
        print("There are no current reservations or checked-in guests.")


def reserve_room(room_table):
    show_rooms(room_table)
    room_number = read_number("Enter room number to reserve: ")
    room_position = find_room(room_table, room_number)

    if room_position == -1:
        print("That room number does not exist.")
        return

    if room_table[room_position][1] != 0:
        print("That room is not available.")
        return

    guest_name = input("Enter guest name: ")
    phone_number = input("Enter phone number: ")

    if guest_name == "":
        print("Guest name cannot be empty.")
        return

    room_table[room_position][1] = 1
    room_table[room_position][2] = guest_name
    room_table[room_position][3] = phone_number

    print("Reservation created for room " + str(room_number) + ".")


def check_in(room_table):
    room_number = read_number("Enter reserved room number: ")
    room_position = find_room(room_table, room_number)

    if room_position == -1:
        print("That room number does not exist.")
        return

    if room_table[room_position][1] != 1:
        print("That room does not have an active reservation.")
        return

    room_table[room_position][1] = 2
    print(room_table[room_position][2] + " checked in to room " + str(room_number) + ".")


def check_out(room_table):
    room_number = read_number("Enter room number to check out: ")
    room_position = find_room(room_table, room_number)

    if room_position == -1:
        print("That room number does not exist.")
        return

    if room_table[room_position][1] != 2:
        print("That room is not currently checked in.")
        return

    guest_name = room_table[room_position][2]
    room_table[room_position][1] = 0
    room_table[room_position][2] = ""
    room_table[room_position][3] = ""

    print(guest_name + " checked out of room " + str(room_number) + ".")


def cancel_reservation(room_table):
    room_number = read_number("Enter room number to cancel: ")
    room_position = find_room(room_table, room_number)

    if room_position == -1:
        print("That room number does not exist.")
        return

    if room_table[room_position][1] != 1:
        print("That room does not have a reservation to cancel.")
        return

    room_table[room_position][1] = 0
    room_table[room_position][2] = ""
    room_table[room_position][3] = ""

    print("Reservation cancelled for room " + str(room_number) + ".")


def show_menu():
    print("")
    print("HOTEL MANAGEMENT SYSTEM")
    print("1. View rooms")
    print("2. Reserve a room")
    print("3. Check in")
    print("4. Check out")
    print("5. Cancel reservation")
    print("6. View guest details")
    print("7. Exit")


def main():
    running = True

    while running:
        show_menu()
        choice = read_number("Choose an option: ")

        if choice == 1:
            show_rooms(rooms)
        elif choice == 2:
            reserve_room(rooms)
        elif choice == 3:
            check_in(rooms)
        elif choice == 4:
            check_out(rooms)
        elif choice == 5:
            cancel_reservation(rooms)
        elif choice == 6:
            show_guest_details(rooms)
        elif choice == 7:
            running = False
            print("Goodbye.")
        else:
            print("Invalid option. Enter a number from 1 to 7.")


main()