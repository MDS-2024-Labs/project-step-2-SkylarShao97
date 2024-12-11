import unittest
from recipes.ingredient_search import list_all_ingredients, search_recipes_by_ingredients, suggest_missing_ingredients
import pandas as pd
from unittest.mock import patch

class TestIngredientSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize data at the class level (executed once)
        cls.recipes_df = pd.DataFrame({
            'name_recipe': ['Pizza', 'Omelet', 'Glazed Yams', 'Cheese Cauliflower'],
            'ingredients': [
                'Wheat Flour (1), Tomato (1), Cheese (1)',
                'Egg (1), Milk (1)',
                'Yam (1), Sugar (1)',
                'Cauliflower (1), Cheese (1)'
            ]
        })

    def setUp(self):
        print('Set up')

    def tearDown(self):
        print('Tear down')

    def test_list_all_ingredients(self):
        all_ingredients = list_all_ingredients(self.recipes_df)

        # Assertions for expected ingredients
        self.assertIn('Tomato', all_ingredients)
        self.assertIn('Cheese', all_ingredients)

        # Assertions for unexpected ingredients
        self.assertNotIn('Garlic', all_ingredients)  
        self.assertNotIn('Pork', all_ingredients)  

    def test_search_recipes_by_ingredients(self):
        with patch('builtins.input', side_effect=['Cheese', 'STOP']):
            with patch('builtins.print') as mocked_print:
                search_recipes_by_ingredients(self.recipes_df)
                output = "\n".join([args[0] for args, _ in mocked_print.call_args_list])
                self.assertIn("Pizza", output)
                self.assertIn("Cheese Cauliflower", output)
                self.assertNotIn("Omelet", output)
                self.assertNotIn("Glazed Yams", output)

        with patch('builtins.input', side_effect=['Garlic', 'STOP']):
            with patch('builtins.print') as mocked_print:
                search_recipes_by_ingredients(self.recipes_df)
                output = "\n".join([args[0] for args, _ in mocked_print.call_args_list])
                self.assertIn("No recipe found.", output)

    def test_suggest_missing_ingredients(self):
        with patch('builtins.input', side_effect=['Pizza', 'Tomato', 'Wheat Flour', 'STOP']):
            with patch('builtins.print') as mocked_print:
                suggest_missing_ingredients(self.recipes_df)
                output = "\n".join([args[0] for args, _ in mocked_print.call_args_list])
                self.assertIn("Cheese", output)
                self.assertNotIn("Yam", output)
                self.assertNotIn("Tomato", output)
                self.assertNotIn("Milk", output)
        
        with patch('builtins.input', side_effect=['Pizza', 'Tomato', 'Wheat Flour', "Cheese", 'STOP']):
            with patch('builtins.print') as mocked_print:
                suggest_missing_ingredients(self.recipes_df)
                output = "\n".join([args[0] for args, _ in mocked_print.call_args_list])
                self.assertIn("You have all the ingredients!", output)

        with patch('builtins.input', side_effect=['Garlic', 'STOP']):
            with patch('builtins.print') as mocked_print:
                suggest_missing_ingredients(self.recipes_df)
                output = "\n".join([args[0] for args, _ in mocked_print.call_args_list])
                self.assertIn("Recipe not found.", output)
        

    @classmethod
    def tearDownClass(cls):
        # Clean up class-level resources
        cls.recipes_df = None
