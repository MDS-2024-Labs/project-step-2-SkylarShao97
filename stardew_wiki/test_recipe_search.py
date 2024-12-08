import unittest
from unittest.mock import patch
import pandas as pd
from recipes.recipe_search import list_all_recipes, search_recipe_by_name, ingredient_details


class TestRecipeSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Sample dataframes for testing
        cls.recipes_df = pd.DataFrame({
            'name_recipe': ['Pizza', 'Omelet', 'Glazed Yams', 'Cheese Cauliflower'],
            'ingredients': [
                'Wheat Flour (1), Tomato (1), Cheese (1)',
                'Egg (1), Milk (1)',
                'Yam (1), Sugar (1)',
                'Cauliflower (1), Cheese (1)'
            ]
        })
        cls.crops_df = pd.DataFrame({
            'name_crop': ['Wheat', 'Tomato', 'Yam'],
            'craft_crop': ['Wheat Flour', None, None],
            'season': ['Summer', 'Summer', 'Fall'],
            'growth_crop': [10, 15, 12],
            'regrowth_crop': [None, None, None],
            'crop_price': [50, 80, 120],
            'craft_crop_price': [100, None, None],
        })
        cls.animals_df = pd.DataFrame({
            'name_animal': ['Cow', 'Chicken'],
            'type': ['Livestock', 'Poultry'],
            'growth_animal': [10, 5],
            'product_animal': ['Milk', 'Egg'],
            'product_animal_price': [50, 10],
            'artisan_animal': ['Cheese', 'Mayo'],
            'artisan_animal_price': [150, 50],
        })

    def setUp(self):
        print('Set up')

    def tearDown(self):
        print('Tear down')
        
    def test_list_all_recipes(self):
        with patch('builtins.print') as mocked_print:
            list_all_recipes(self.recipes_df)
            output = "\n".join([args[0] for args, _ in mocked_print.call_args_list])
            self.assertIn("Available Recipes:", output)
            self.assertIn("- Pizza", output)
            self.assertIn("- Omelet", output)
            self.assertNotIn("- Garlic Bread", output)

    def test_search_recipe_by_name(self):
        with patch('builtins.input', side_effect=['Pizza']):
            with patch('builtins.print') as mocked_print:
                search_recipe_by_name(self.recipes_df)
                output = "\n".join([args[0] for args, _ in mocked_print.call_args_list])
                self.assertIn("Recipe: Pizza", output)
                self.assertIn("Ingredients: Wheat Flour (1), Tomato (1), Cheese (1)", output)

        with patch('builtins.input', side_effect=['Garlic Bread']):
            with patch('builtins.print') as mocked_print:
                search_recipe_by_name(self.recipes_df)
                output = "\n".join([args[0] for args, _ in mocked_print.call_args_list])
                self.assertIn("Recipe not found.", output)

    def test_ingredient_details(self):
        # Test for crops
        with patch('builtins.input', side_effect=['Tomato', 'STOP']):
            with patch('builtins.print') as mocked_print:
                ingredient_details(self.crops_df, self.animals_df)
                output = "\n".join([args[0] for args, _ in mocked_print.call_args_list])
                self.assertIn("Ingredient found in Crops:", output)
                self.assertIn("Name: Tomato", output)
                self.assertIn("Season: Summer", output)

        # Test for animals
        with patch('builtins.input', side_effect=['Milk', 'STOP']):
            with patch('builtins.print') as mocked_print:
                ingredient_details(self.crops_df, self.animals_df)
                output = "\n".join([args[0] for args, _ in mocked_print.call_args_list])
                self.assertIn("Ingredient found in Animals:", output)
                self.assertIn("Animal: Cow", output)
                self.assertIn("Product: Milk", output)

        # Test for not found
        with patch('builtins.input', side_effect=['Garlic', 'STOP']):
            with patch('builtins.print') as mocked_print:
                ingredient_details(self.crops_df, self.animals_df)
                output = "\n".join([args[0] for args, _ in mocked_print.call_args_list])
                self.assertIn("Ingredient not found in Crops or Animals.", output)


    @classmethod
    def tearDownClass(cls):
        # Clean up class-level resources
        cls.recipes_df = None
        cls.crops_df = None
        cls.animals_df = None

