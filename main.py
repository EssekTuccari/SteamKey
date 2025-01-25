import random
import requests

def generate_key():
    key = ""
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for _ in range(5):
        key += random.choice(characters)
    key += "-"
    for _ in range(5):
        key += random.choice(characters)
    key += "-"
    for _ in range(5):
        key += random.choice(characters)
    return key

def check_key(key):
    url = f"https://store.steampowered.com/account/registerkey?key={key}"
    response = requests.get(url)
    if "This product key is already registered" in response.text:
        return True  # Key is valid
    else:
        return False  # Key is invalid

def save_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

def generate_and_check_keys():
    valid_count = 0
    invalid_count = 0

    try:
        while True:
            key = generate_key()
            is_valid = check_key(key)

            if is_valid:
                valid_count += 1
                print("Bir key bulundu! " + key)
                save_to_file("valid_keys.txt", key)
            else:
                invalid_count += 1

            print(f"\rValid: {valid_count}, Invalid: {invalid_count} - Key {key} is {'valid' if is_valid else 'invalid'}", end="")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

# Generate and check keys until interrupted by the user (CTRL+C)
generate_and_check_keys()