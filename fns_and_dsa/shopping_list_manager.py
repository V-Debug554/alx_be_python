def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter the item to add: "))

        if choice == '1':
            # Prompt for and add an item
            add_item = input("Enter the item do you want to add: ")
            shopping_list.append(add_item)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                 print("Your shopping list is empty, there is nothing to remove")
            else:
                remove_item = input("Enter the item you want to remove? ")
                if remove_item in shopping_list:
                    shopping_list.remove(remove_item)
                else:
                     print(f'The item, "{remove_item}" is not in your shopping list.')
            pass
        elif choice == '3':
            # Display the shopping list with every item in a new line
            if not shopping_list:
                    print("Your shopping list is empty!")
            else:
                    for item in shopping_list:
                         print(item)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
