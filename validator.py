from config import ROWS, SEATS_PER_ROW

def parse_and_validate_args(args):
    # First check if the number of CLI arguments is exactly 3 (excluding the file name)

    if len(args) != 4:
        return None

    action = args[1].upper()
    seat = args[2].upper()

    try:
        count = int(args[3])
        start_index = int(seat[1:])
    except ValueError:
        # Happens if user passes something weird like count="two"
        return None

    # Booking/cancelling 0 or negative seats doesn’t make sense
    if count <= 0:
        return None

    row = seat[0]

    # Check if the row is within allowed range (A to T by default)
    if row < 'A' or row > chr(ord('A') + ROWS - 1):
        return None

    # Make sure seat index is valid and doesn’t go out of bounds
    if start_index < 0 or start_index + count > SEATS_PER_ROW:
        return None

    if action not in {"BOOK", "CANCEL"}:
        return None

    # If everything checks out, return the parsed values
    return action, row, start_index, count

