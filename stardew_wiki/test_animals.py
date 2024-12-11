import unittest
from unittest.mock import patch
import pandas as pd
from pathlib import Path
from livingthings.animals import AnimalDatabase, BarnAnimal, CoopAnimal, input_animal

class TestAnimalDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Setting up class resources")
        csv_file_path = Path(__file__).parent / "livingthings" / "data" / "Animals.csv"
        cls.db = AnimalDatabase(csv_file_path)

    @classmethod
    def tearDownClass(cls):
        print("Tearing down class resources")
        del cls.db

    def setUp(self):
        print("Set up")
        self.expected_barn_animal = BarnAnimal(
            name="Cow",
            growth_time="5(night)",
            product="Milk",
            artisan="Cheese",
            product_price=125,
            artisan_price=230
        )
        self.expected_coop_animal = CoopAnimal(
            name="Chicken",
            growth_time="9000(min)",
            product="Egg",
            artisan="Mayonnaise",
            product_price=50,
            artisan_price=190
        )

    def tearDown(self):
        print("Tear down")

    def test_load_data_from_csv(self):
            """Test loading data from CSV file"""
            csv_file_path = Path(__file__).parent / "livingthings" / "data" / "Animals.csv"
            db = AnimalDatabase(csv_file_path)
            
            self.assertIn("Cow", db.animals)
            self.assertIn("Chicken", db.animals)
            self.assertIn("Duck", db.animals)
            self.assertIn("Goat", db.animals)

    def test_search_by_name_found(self):
        result = self.db.search_by_name("Cow")
        self.assertIn("Cow", result)
        self.assertIn("Milk", result)
        self.assertIn("Cheese", result)
        self.assertIn("Type: Barn", result)

    def test_search_by_name_not_found(self):
        result = self.db.search_by_name("Bird")
        self.assertEqual(result, "Animal not found.")
        self.assertNotIn("Bird", result)
        self.assertIsInstance(result, str)
        self.assertFalse("Type:" in result)

    def test_search_by_type_barn(self):
        result = self.db.search_by_type("Barn")
        self.assertIn("Cow", result)
        self.assertIn("Milk", result)
        self.assertIn("Cheese", result)
        self.assertTrue("Type: Barn" in result)

    def test_search_by_type_coop(self): 
        result = self.db.search_by_type("Coop")
        self.assertIn("Chicken", result)
        self.assertIn("Egg", result)
        self.assertIn("Mayonnaise", result)
        self.assertTrue("Type: Coop" in result)

    def test_search_by_type_invalid(self):
        result = self.db.search_by_type("Invalid")
        self.assertEqual(result, "No animals found for type 'Invalid'.")

# Class with unittest.mock for testing code asking for user's input
class TestInputAnimal(unittest.TestCase):

    def test_search_by_name_input(self):
        with patch('builtins.input', side_effect=["1", "Cow", "3"]) as mock_input:
            with patch('builtins.print') as mock_print:
                with patch('livingthings.animals.AnimalDatabase') as MockDatabase:
                    mock_db = MockDatabase.return_value
                    mock_db.search_by_name.return_value = "Cow"

                    input_animal()

                    mock_input.assert_called()  # Check if input() was called
                    mock_print.assert_any_call("\nSearch Result:")  # Print header check
                    mock_print.assert_any_call("Cow")  # Check correct search result
                    mock_db.search_by_name.assert_called_once_with("Cow")  # Ensure correct DB call


    def test_search_by_type_input(self):
        with patch('builtins.input', side_effect=["2", "Coop", "3"]) as mock_input:
            with patch('builtins.print') as mock_print:
                with patch('livingthings.animals.AnimalDatabase') as MockDatabase:
                    mock_db = MockDatabase.return_value
                    mock_db.search_by_type.return_value = "Chicken"

                    input_animal()

                    mock_input.assert_called()  # Check if input() was called
                    mock_print.assert_any_call("\nSearch Result:")  # Print header check
                    mock_print.assert_any_call("Chicken")  # Check correct search result
                    mock_db.search_by_type.assert_called_once_with("Coop")  # Ensure correct DB call

    def test_exit_menu_directly(self):
        with patch('builtins.input', side_effect=["3"]) as mock_input:
            with patch('builtins.print') as mock_print:
                input_animal()
                
                mock_input.assert_called_once()
                mock_print.assert_any_call("Exiting Animal Search...")

    def test_exit_menu(self):
        with patch('builtins.input', side_effect=["999", "3"]) as mock_input:
            with patch('builtins.print') as mock_print:
                input_animal()

                mock_input.assert_called()  # Check if input() was called
                mock_print.assert_any_call("Invalid choice. Please try again.")  # Check correct error message
                self.assertEqual(mock_input.call_count, 2)  # Ensure 2 input prompts
                mock_print.assert_any_call("Exiting Animal Search...")  # Check correct exit message