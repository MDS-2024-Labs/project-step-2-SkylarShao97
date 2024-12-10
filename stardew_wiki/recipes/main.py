import pandas as pd
from pathlib import Path
from .recipe_search import list_all_recipes, search_recipe_by_name, ingredient_details
from .ingredient_search import list_all_ingredients, search_recipes_by_ingredients, suggest_missing_ingredients

# Load the data directly in main.py
def load_data():
    """Loads the data from the Excel file."""

    # Dynamically resolve the path to the data file
    base_path = Path(__file__).parent
    file_path = base_path / "data/wiki.xlsx"
    
    recipes_data = pd.read_excel(file_path, sheet_name='Recipes')
    crops_data = pd.read_excel(file_path, sheet_name='Crops')
    animals_data = pd.read_excel(file_path, sheet_name='Animals')
    return recipes_data, crops_data, animals_data

def main():
    print("Loading data...")
    recipes_data, crops_data, animals_data = load_data()

    while True:
        print("\nWhat would you like to do?")
        print("1. List all recipes")
        print("2. Search for a recipe by name")
        print("3. View details of ingredients")
        print("4. List all unique ingredients")
        print("5. Search recipes by ingredients")
        print("6. Suggest missing ingredients for a recipe")
        print("7. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            list_all_recipes(recipes_data)
        elif choice == "2":
            search_recipe_by_name(recipes_data)
        elif choice == "3":
            ingredient_details(crops_data, animals_data)
        elif choice == "4":
            list_all_ingredients(recipes_data)
        elif choice == "5":
            search_recipes_by_ingredients(recipes_data)
        elif choice == "6":
            suggest_missing_ingredients(recipes_data)
        elif choice == "7":
            print("Returning to the Menu...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




