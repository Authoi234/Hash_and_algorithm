import hashlib

available_algorithms = sorted(list(hashlib.algorithms_available))

print("PLEASE CHOOSE FROM BELOW")
for index, algorithm in enumerate(available_algorithms):
    print(f'{index}:{algorithm}')
print("---------------------------------------\n")

hash_value = input("Target Hash: ")
wordlist = input("File name (The Wordlist): ")

try:
    choice = int(input(f"Select algorithm index (0-{len(available_algorithms)-1}): "))
    if choice < 0 or choice >= len(available_algorithms): raise ValueError

except ValueError:
    print("Invalid selection.")
    quit()


selectedType = available_algorithms[choice]

try:
    pass_file = open(wordlist, 'r', encoding='utf-8', errors='ignore')
except:
    print("No File Found")
    quit()

for word in pass_file:
    encoded_word = word.encode('utf-8')
    digest = hashlib.new(selectedType, encoded_word).hexdigest()

    if digest.strip() == hash_value.strip():
        print("~Success: Password found")
        print(">>>PASSWORD IS: " + word)
        break
else:
        print("Password not in list")