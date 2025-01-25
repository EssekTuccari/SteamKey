import random
import requests
import os

def clearConsol ():
    os.system('cls' if os.name == 'nt' else 'clear')
    
class StringTable:
    def __init__(self):
        # Tablonun başlatılması
        self.table = []

    def add_string(self, string):
        # Yeni bir string eklenmesi
        self.table.append(string)

    def print_table(self):
        # Tabloyu alt alta yazdırma
        for item in self.table:
            print(item)

table = StringTable()

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

def check(tablo, key):
   return aranan_string in tablo.values

def generate_and_check_keys():
    clearConsol ()
    valid_count = 0
    invalid_count = 0

    try:
        while True:
            key = generate_key()
            is_valid = check_key(key)

            if is_valid:
            	valid_count += 1
            	print(f"\033[92m{"\nBir key bulundu! " + key}\033[0m")
            	table.add_string(key)
            	
            else:
                invalid_count += 1
		
            print(
    		f"\rValid: \033[92m{valid_count}\033[0m, Invalid: \033[91m{invalid_count}\033[0m - Key {key} is "
    			+ (f"\033[92mvalid\033[0m" if is_valid else f"\033[91minvalid\033[0m"),
    			end=""
	)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        print("\nBulunan Keyler:")
        table.print_table()

# Generate and check keys until interrupted by the user (CTRL+C)
generate_and_check_keys()
