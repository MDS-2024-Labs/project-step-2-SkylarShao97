import pandas as pd

# Functions for recipe_search
def list_all_recipes(recipes_df):
    """Lists all recipe names from the Recipes data."""
    recipes = recipes_df['name_recipe'].tolist()
    print("Available Recipes:")
    for recipe in recipes:
        print(f"- {recipe}")

def search_recipe_by_name(recipes_df):
    """Searches for a recipe by name and displays its ingredients."""
    name = input("Enter the name of the recipe to search: ").strip()
    recipe = recipes_df[recipes_df['name_recipe'].str.contains(name, case=False, na=False)]
    if not recipe.empty:
        print(f"Recipe: {recipe.iloc[0]['name_recipe']}")
        print(f"Ingredients: {recipe.iloc[0]['ingredients']}")
    else:
        print("Recipe not found.")

def ingredient_details(crops_df, animals_df):
    """Interactively fetches details of ingredients from the Crops data."""
    while True:
        user_input = input("Enter the ingredient name to see details (or type 'STOP' to quit): ").strip()
        if user_input.lower() == 'stop':
            break
        
        # Search in crops (name_crop and craft_crop)
        crop_detail = crops_df[
            (crops_df['name_crop'] == user_input) | (crops_df['craft_crop'] == user_input)
        ]
        
        # Search in animals (product_animal)
        animal_detail = animals_df[animals_df['product_animal'] == user_input]

        # Print results
        if not crop_detail.empty:
            print("\nIngredient found in Crops:")
            for index, row in crop_detail.iterrows():
                print(f"Name: {row['name_crop']}")
                print(f"Craft Name: {row.get('craft_crop', 'N/A')}")
                print(f"Season: {row['season']}")
                print(f"Growth Time: {row['growth_crop']} days")
                print(f"Regrowth Time: {row.get('regrowth_crop', 'N/A')} days")
                print(f"Price: {row['crop_price']}")
                print(f"Craft Price: {row.get('craft_crop_price', 'N/A')}")
                print("-" * 40)

        elif not animal_detail.empty:
            print("\nIngredient found in Animals:")
            for index, row in animal_detail.iterrows():
                print(f"Animal: {row['name_animal']}")
                print(f"Type: {row['type']}")
                print(f"Growth Time: {row['growth_animal']}")
                print(f"Product: {row['product_animal']}")
                print(f"Product Price: {row['product_animal_price']}")
                print(f"Artisan Product: {row.get('artisan_animal', 'N/A')}")
                print(f"Artisan Product Price: {row.get('artisan_animal_price', 'N/A')}")
                print("-" * 40)

        else:
            print("\nIngredient not found in Crops or Animals.")

