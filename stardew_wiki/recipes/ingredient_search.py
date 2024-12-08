import pandas as pd

def list_all_ingredients(recipes_df):
    """
    Lists all unique ingredients from the 'ingredients' column.
    Removes parentheses and numbers, ensuring unique ingredient names.
    """
    try:
        # Step 1: Split the ingredients into individual items
        ingredients = (
            recipes_df['ingredients']
            .str.split(',')  # Split by comma
            .explode()  # Expand into individual rows
            .str.strip()  # Remove extra spaces
            .dropna()  # Drop any NaN values
        )
        
        # Step 2: Remove text inside parentheses (e.g., '(1)') using regex
        clean_ingredients = (
            ingredients.str.replace(r"\(.*?\)", "", regex=True)  # Remove content in parentheses
            .str.replace(r"\d+", "", regex=True)  # Remove digits
            .str.strip()  # Strip spaces again after cleanup
            .unique()  # Get unique ingredients
        )
        
        # Step 3: Print each ingredient line by line
        print("\nUnique Ingredients:")
        for ingredient in sorted(clean_ingredients):  # Sort alphabetically for better readability
            print(f"- {ingredient}")

    except KeyError as e:
        print(f"Error: The column is missing in the data. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def search_recipes_by_ingredients(recipes_df):
    """Finds recipes that use the provided ingredients."""
    ingredient_list = []  # Create the ingredient list inside the function
    print("Enter ingredients one by one (type 'STOP' to finish):")
    
    # Collect ingredients from user input
    while True:
        ingredient = input("Enter ingredient: ").strip()
        if ingredient.lower() == 'stop':
            break
        ingredient_list.append(ingredient)

    matched_recipes = []  # To store matched recipes
    for ingredient in ingredient_list:
        # Check for recipes containing the ingredient
        recipes = recipes_df[recipes_df['ingredients'].str.contains(ingredient, case=False, na=False)]
        if not recipes.empty:
            matched_recipes.extend(recipes['name_recipe'].tolist())

    # Output results
    if matched_recipes:
        print("Recipes containing the ingredients:")
        for recipe in set(matched_recipes):  # Use set to remove duplicates
            print(f"- {recipe}")
    else:
        print("No recipe found.")

def suggest_missing_ingredients(recipes_df):
    """Suggests missing ingredients for a given recipe based on partial ingredients."""
    recipe_name = input("Enter the name of the recipe: ").strip()
    recipe = recipes_df[recipes_df['name_recipe'].str.contains(recipe_name, case=False, na=False)]
    if recipe.empty:
        print("Recipe not found.")
        return

    full_ingredients = recipe['ingredients'].iloc[0].split(',')
    full_ingredients = [ingredient.split('(')[0].strip() for ingredient in full_ingredients]

    print("Enter the ingredients you already have (type 'STOP' to finish):")
    partial_ingredients = []
    while True:
        ingredient = input("Enter ingredient: ").strip()
        if ingredient.lower() == 'stop':
            break
        partial_ingredients.append(ingredient)

    missing_ingredients = [item for item in full_ingredients if item not in partial_ingredients]
    if missing_ingredients:
        print("Missing Ingredients:")
        for ingredient in missing_ingredients:
            print(f"- {ingredient}")
    else:
        print("You have all the ingredients!")