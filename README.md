# Hotel Management System

A console-based Python application for managing hotel room bookings, guest check-ins, check-outs, and reservations.

## Project Overview

This project demonstrates a simple hotel management workflow using Python. It allows a hotel receptionist to manage room availability, reserve rooms, check guests in and out, and cancel reservations from a text-based menu.

The system uses a nested list to store room details, including:

- Room number
- Status (available, reserved, checked in)
- Guest name
- Phone number

## Features

- View all rooms and their current status
- Reserve an available room
- Check in a guest with an active reservation
- Check out a guest from a checked-in room
- Cancel a reservation
- View guest details for all current bookings
- Input validation for room numbers and menu options

## Room Status Codes

Each room record follows this structure:

```python
[room_number, status, guest_name, phone_number]
```

Status values:

- `0` = Available
- `1` = Reserved
- `2` = Checked in

## Files

- `Hotel Management.py` - Main Python application containing all logic
- `README.md` - Project documentation

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:

```bash
python "Hotel Management.py"
```

## Example Menu

```text
HOTEL MANAGEMENT SYSTEM
1. View rooms
2. Reserve a room
3. Check in
4. Check out
5. Cancel reservation
6. View guest details
7. Exit
```

## Workflow Example

- View rooms to see which are available
- Reserve a room by entering the room number
- Enter the guest name and phone number
- Confirm the guest check-in
- Check out the guest when they leave
- Cancel reservation if needed

## Learning Objectives

This project helps practice:

- Python functions
- Nested lists and data manipulation
- Basic input validation
- Menu-driven console applications
- Hotel booking logic and status tracking

## Author

AshotoX

## License

This project is intended for educational and demonstration purposes.
