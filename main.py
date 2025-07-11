import sys
import logging
from seats_utils import load_seat_map, save_seat_map, book_seats, display_seat_map, cancel_seats

# To push the erros to a file with timestamps
logging.basicConfig(
    filename = 'error.log',
    level = logging.WARNING,  # Log warnings and errors
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

if __name__ == "__main__":

    # Just to view if needed
    if len(sys.argv) == 2 and sys.argv[1].upper() == "VIEW":
        seat_map = load_seat_map()
        display_seat_map(seat_map)
        sys.exit()

    try:
        # Load existing seat data or create a new one if it doesn’t exist
        seat_map = load_seat_map()

        # Check for correct number of CLI inputs
        if len(sys.argv) != 4:
            logging.warning(
                "Invalid number of arguments. Expected 3 CLI arguments, got %d",
                len(sys.argv) - 1
            )
            print("FAIL")
            sys.exit()

        action = sys.argv[1].upper()
        seat = sys.argv[2].upper()
        try:
            # Try converting seat number nd count from string to integer
            count = int(sys.argv[3])
            start_index = int(seat[1:])
        except ValueError:
            # Happens if someone passes a word like "two" instead of 2
            logging.warning("Invalid seat or count format. seat=%s, count=%s", sys.argv[2], sys.argv[3])
            print("FAIL")
            sys.exit()

        row = seat[0]

        # Basic validations

        # Validate action and count (only BOOK or CANCEL are allowed, and count must be positive)
        if action not in {"BOOK", "CANCEL"} or count <= 0:
            logging.warning(
                "Invalid action or non-positive count. action=%s, count=%d",
                action,
                count
            )
            print("FAIL")
            sys.exit()

        # Check if the row exists and seat range doesn’t go beyond 0–7
        if row not in seat_map or start_index < 0 or start_index + count > len(seat_map[row]):
            logging.warning(
                "Invalid row or seat range. row=%s, start_index=%d, count=%d",
                row,
                start_index,
                count
            )
            print("FAIL")
            sys.exit()

        # Perform the actual action
        result = book_seats(seat_map, row, start_index, count)\
            if action == "BOOK" else cancel_seats(seat_map, row, start_index, count)

        # if action == "BOOK":
        #     result = book_seats(seat_map, row, start_index, count)
        # else:
        #     result = cancel_seats(seat_map, row, start_index, count)

        print(result)

        #If the operation was successful, save the updated seat data
        if result == "SUCCESS":
            save_seat_map(seat_map)

    except Exception as e:
        # Any unexpected crash will be logged into the error.log file
        logging.error("Unhandled exception occurred", exc_info=True)
        sys.exit(1)
