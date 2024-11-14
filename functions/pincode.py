import hashlib

def hash_pincode(pincode):
    """Hashes the pincode using SHA-256."""
    return hashlib.sha256(pincode.encode()).hexdigest()

def store_hashed_pincode(hashed_pincode):
    """Stores the hashed pincode. Here, we are storing it in a file."""
    with open('hashed_pincode.txt', 'w') as file:
        file.write(hashed_pincode)

def load_hashed_pincode():
    """Loads the hashed pincode from the file."""
    try:
        with open('hashed_pincode.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def verify_pincode(entered_pincode):
    """Verifies the entered pincode by comparing its hash with the stored hash."""
    hashed_pincode = load_hashed_pincode()
    if not hashed_pincode:
        print("No pincode stored.")
        return False
    
    return hash_pincode(entered_pincode) == hashed_pincode

def main():
    choice = input("Do you want to (1) set a new pincode or (2) login? Enter 1 or 2: ")
    
    if choice == '1':
        # Set a new pincode
        new_pincode = input("Enter a new pincode to store: ")
        hashed_pincode = hash_pincode(new_pincode)
        store_hashed_pincode(hashed_pincode)
        print("Pincode stored successfully.")
    
    elif choice == '2':
        # Login by verifying pincode
        entered_pincode = input("Enter your pincode: ")
        if verify_pincode(entered_pincode):
            print("Pincode is correct. Login successful.")
        else:
            print("Incorrect pincode. Please try again.")

if __name__ == "__main__":
    main()

