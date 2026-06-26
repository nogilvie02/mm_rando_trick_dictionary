# main.py

trick_database = {
    "Bomb Hover": {
        "items_needed": ["Bombs", "a Shield"]
    },
    "Megaflip": {
        "items_needed": ["Bombs"]
    }
}


items = ["Bombs", "a Shield", "a Sword"]


def main():
    print("*Welcome to the Majora's Mask Rando Trick Dictionary!*")
    # 1: get inventory
    user_inventory = []
    for item in items:
        answer = input(f"Do you have {item}? (y/n): ").lower()
        if answer == "y":
            user_inventory.append(item)
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
        if set(needed_items).issubset(set(user_inventory)):
            possible_tricks.append(trick)

    # 3: output list of tricks from step 2
    if possible_tricks == []:
        print("\n**No tricks are possible given your inventory.**\n")
        exit(0)
    else:
        print("\nPossible tricks include:")
        for trick in possible_tricks:
            print(f" - {trick}")
        print("\n**End of possible tricks.**\n")
        exit(0)


if __name__ == "__main__":
    main()