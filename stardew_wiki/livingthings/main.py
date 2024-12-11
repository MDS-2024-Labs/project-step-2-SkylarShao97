from .animals import input_animal
from .crops import input_crop

def main():
    print("Loading data...")
    while True:
        print("\nWhat would you like to do?")
        print("1. Search for Animals")
        print("2. Search for Crops")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            input_animal()
        elif choice == "2":
            input_crop()
        elif choice == "3":
            print("Returning to the Menu...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()