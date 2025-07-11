import json
import os
from config import ROWS, SEATS_PER_ROW, SEAT_FILE

def create_initial_seat_map():
    # Creating an empty seat map with all seats set to '0' (available)
    rows = [chr(i) for i in range(ord('A'), ord('A') + ROWS)]
    return {row: ['0'] * SEATS_PER_ROW for row in rows}

 # Saving the current state of the seat map to a JSON file so it persists
def save_seat_map(seat_map):
    with open(SEAT_FILE, 'w') as f:
        json.dump(seat_map, f)

# If the seat file doesn't exist, just create a fresh map. Else, load the existing one.
def load_seat_map():
    if not os.path.exists(SEAT_FILE):
        return create_initial_seat_map()
    with open(SEAT_FILE, 'r') as f:
        return json.load(f)

#Booking logic
def book_seats(seat_map, row, start_index, count):
    if start_index < 0 or start_index + count > len(seat_map[row]):
        return "FAIL"
    # Only book if all the seats in that range are available
    if all(seat_map[row][i] == "0" for i in range(start_index, start_index + count)):
        for i in range(start_index, start_index + count):
            seat_map[row][i] = "X"
        return "SUCCESS"
    return "FAIL"

#Display seat map
def display_seat_map(seat_map):

    print("\n Current Seat Map: \n")
    for row in seat_map:
        seats = seat_map[row]
        formatted = f"| {seats[0]}{seats[1]}_{seats[2]}{seats[3]}{seats[4]}{seats[5]}_{seats[6]}{seats[7]} |"
        print(f" {row} {formatted}")


#Cancel logic
def cancel_seats(seat_map, row, start_index, count):
    # only cancel if all those seats are already booked
    if all(seat_map[row][i] == "X" for i in range(start_index, start_index + count)):
        for i in range(start_index, start_index + count):
            seat_map[row][i] = "0" #REsetting to available
        return "SUCCESS"
    return "FAIL"
