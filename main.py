# main.py

from database import trackable_items, trick_database

def main():
    print("Welcome to the Majora's Mask Rando Trick Dictionary by nogilvie02\n")
    # 1: get inventory
    user_inventory = []
    for item in trackable_items:
        # verify response is valid from user (y/n)
        while True:
            answer = input(f"Do you have {item}? (y/n): ").lower().strip()
            if answer == "y":
                user_inventory.append(item)
                break
            elif answer == "n":
                break
            print("Invalid response. Please respond with 'y' or 'n' only.")

    if user_inventory == []:
        print("\nNO INVENTORY INPUTTED!")
    else:
        print("\nYour inventory is:")
        for item in user_inventory:
            print(f" - {item}")
    
    # 2: get list of tricks from database
    possible_tricks = []
    for trick in trick_database:
        needed_items = trick_database[trick]["items_needed"]
        # for verifying differing requirements (needed items) for tricks (ex: substituting Bombs with Bombchus)
        for requirements in needed_items:
            if set(requirements).issubset(set(user_inventory)):
                possible_tricks.append(trick)
                break

    # 3: output list of tricks from step 2 (Should never happen due to Gainer trick always being available)
    if possible_tricks == []:
        print("\n**No tricks are found given your inventory.**\n")
        exit(0)
    else:
        print("\nPossible tricks include:")
        for trick in possible_tricks:
            print(f" - {trick}")
        print("\n**End of possible tricks.**\n")
        exit(0)


if __name__ == "__main__":
    main()