import recipes.main as recipes_main
import livingthings.main as livingthings_main

def main():
    print("Welcome to the Stardew Valley Wiki System!")
    while True:
        print("\nMain Menu:")
        print("1. Access Living Things Database")
        print("2. Access Recipes Database")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            livingthings_main.main()  # Calls the main function of livingthings
        elif choice == "2":
            recipes_main.main()  # Calls the main function of recipes
        elif choice == "3":
            print("Thank you for using the Stardew Valley Wiki System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()