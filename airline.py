
import json
import os
import sys


ROWS = 20
seats_per_row = 8
seat_file = "seats.json"

def create_initial_seat_map():
    rows = [chr(i) for i in range(ord('A'), ord('A') + ROWS)]
    seat_map = {row: ['0'] * seats_per_row for row in rows}
    return seat_map

# Save the current seat map (after booking/canceling)
def save_seat_map(seat_map):
    with open(seat_file, 'w') as f:
        json.dump(seat_map, f)

# Load seat map from file or create a new one
def load_seat_map():
    if not os.path.exists(seat_file):
        return create_initial_seat_map()
    with open(seat_file, 'r') as f:
        return json.load(f)

def display_seat_map(seat_map):
    print("\n ------ Seat map ------ \n")
    for row in seat_map:
        seats=' '.join(seat_map[row])
        print(f"Row {row} : {seats}")



'''
if __name__ == "__main__":
    # Load the current seat map (from file or create fresh)
    seat_map = load_seat_map()

    # Simulate booking seat A2 (index 2 in row 'A')
    if seat_map["A"][3] == "0":
        seat_map["A"][3] = "X"
        print("Seat A2 successfully booked!")
    else:
        print("Seat A2 already occupied")

    # Save updated seat map
    save_seat_map(seat_map)'''


if __name__ == "__main__":
    seat_map = load_seat_map()


    if len(sys.argv) == 2 and sys.argv[1].upper()=='VIEW':
        display_seat_map(seat_map)
        sys.exit()

    if len(sys.argv) != 4:
        print("FAIL")  # not enough inputs
        sys.exit()

    action = sys.argv[1].upper()      # BOOK or CANCEL
    seat = sys.argv[2].upper()        # e.g., A2
    count = int(sys.argv[3])          # number of seats to book/cancel

    row = seat[0]                     # 'A'
    start_index = int(seat[1:])        # 2 (seat number)

    #To ensure that the no of seats shouldnt be 0 or a negative value
    if count <=0:
        print('FAIL')
        sys.exit()


# Booking logic

    if row not in seat_map or start_index + count > seats_per_row:
        print("FAIL")
        sys.exit()

    #print("tryna book seats:", seat_map[row][start_index:start_index + count])

    if action == "BOOK":
        if all(seat_map[row][i] == "0" for i in range(start_index, start_index + count)):
            for i in range(start_index, start_index + count):
                seat_map[row][i] = "X"
            print("SUCCESS")
        else:
            print("FAIL")

    elif action == "CANCEL":
        if all(seat_map[row][i] == "X" for i in range(start_index, start_index + count)):
            for i in range(start_index, start_index + count):
                seat_map[row][i] = "0"
            print("SUCCESS")
        else:
            print("FAIL")
    else:
        print("FAIL")



    save_seat_map(seat_map)

