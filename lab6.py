# Angelina Gonzalez

def main_menu(): # prints menu
  print("Menu")
  print("-" * 13)
  print("1. Encode")
  print("2. Decode")
  print("3. Quit\n")
  

def encoder(old_password): # encodes password
  new_password = ''

  for element in old_password: # goes through each element
    new_num = int(element)
    new_num += 3 # adds 3

    if new_num > 9:
      new_num -= 10 # subtracts 10 if over 9

    new_password += str(new_num) # adds to password as string

  encoded = int(new_password) # converts entire str to int
  return encoded # returns int

if __name__ == "__main__":
  condition = True
  while condition:
    main_menu() # shows menu
    choice = int(input('Please enter an option: ')) # takes input

    if choice == 1: # if choice is 1
      password = input('Please enter your password to encode: ')
      encoded_password = encoder(password) # assigns encoded value 
      print('Your password has been encoded and stored!')

    elif choice == 2: # if choice is 2
      print(f'The encoded password is {encoded_password},', end="") # prints statement
      # put rest of sentence here for decoded    

    else: # if choice is Quit
      break
