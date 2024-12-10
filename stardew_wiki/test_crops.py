import unittest
from unittest.mock import patch
from pathlib import Path
from livingthings.crops import CropDatabase, Crop, input_crop

class TestCropDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Setting up class resources")
        csv_file_path = Path(__file__).parent / "livingthings" / "data" / "Crops.csv"
        cls.db = CropDatabase(csv_file_path)

    @classmethod
    def tearDownClass(cls):
        print("Tearing down class resources")
        del cls.db

    def setUp(self):
        print("Set up")
        self.corn = Crop(
            name="Corn",
            season="Summer/Fall",
            growth_time=14,
            regrowth_time=4,
            price=50,
            craft_product="Oil",
            craft_price=100
        )
        self.starfruit = Crop(
            name="Starfruit",
            season="Summer",
            growth_time=13,
            regrowth_time=None,
            price=750,
            craft_product=None,
            craft_price=None
        )

    def tearDown(self):
        print("Tear down")

    def test_load_data_from_csv(self):
        self.assertIn("Corn", self.db.crops)  
        self.assertIn("Starfruit", self.db.crops)  
        self.assertIsInstance(self.db.crops["Corn"], Crop)  
        self.assertGreater(len(self.db.crops), 0) 

    def test_search_by_name_found(self):
        result = self.db.search_by_name("Corn")
        self.assertIn("Name: Corn", result)  
        self.assertIn("Growth Time: 14", result)  
        self.assertIn("Price: 50", result)  
        self.assertIn("Crafting Product: Oil (Price: 100.0)", result)

    def test_search_by_name_not_found(self):
        result = self.db.search_by_name("Lemon")
        self.assertEqual(result, "Crop not found.")  
        self.assertNotIn("Corn", result)  # Ensure irrelevant data is excluded
        self.assertIsInstance(result, str) 
        self.assertTrue(len(result) > 0) 

    def test_search_by_season_found(self):
        result = self.db.search_by_season("Summer")
        self.assertIn("Corn", result)  
        self.assertIn("Starfruit", result)  
        self.assertNotIn("Lemon", result) 
        self.assertTrue(len(result.splitlines()) > 0)

    def test_search_by_season_not_found(self):
        result = self.db.search_by_season("Winter")
        self.assertEqual(result, "No crops found for Winter.") 
        self.assertNotIn("Corn", result)  
        self.assertIsInstance(result, str)  
        self.assertTrue(len(result) > 0)

    def test_crop_str(self):
        corn_str = str(self.corn)
        star_str = str(self.starfruit)

        self.assertIn("Name: Corn", corn_str)
        self.assertIn("Season: Summer/Fall", corn_str)
        self.assertIn("Price: 50", corn_str)
        self.assertNotIn("No crafting product", corn_str)

        self.assertIn("Name: Starfruit", star_str)
        self.assertIn("Season: Summer", star_str)
        self.assertIn("Growth Time: 13", star_str)
        self.assertIn("No crafting product", star_str)

# Class with unittest.mock for testing code asking for user's input
class TestInputCrop(unittest.TestCase):

    def test_search_by_name_input(self):
        with patch('builtins.input', side_effect=["1", "Corn", "3"]) as mock_input:
            with patch('builtins.print') as mock_print:
                with patch('livingthings.crops.CropDatabase') as MockDatabase:
                    mock_db = MockDatabase.return_value
                    mock_db.search_by_name.return_value = "Name: Corn\nSeason: Summer/Fall"

                    input_crop()

                    mock_input.assert_called()
                    mock_print.assert_any_call("\nSearch Result:")
                    mock_print.assert_any_call("Name: Corn\nSeason: Summer/Fall")
                    mock_db.search_by_name.assert_called_once_with("Corn")

    def test_search_by_season_input(self):
        with patch('builtins.input', side_effect=["2", "Summer", "3"]) as mock_input:
            with patch('builtins.print') as mock_print:
                with patch('livingthings.crops.CropDatabase') as MockDatabase:
                    mock_db = MockDatabase.return_value
                    mock_db.search_by_season.return_value = "Wheat\nBlueberry"

                    input_crop()

                    mock_input.assert_called()
                    mock_print.assert_any_call("\nSearch Result:")
                    mock_print.assert_any_call("Wheat\nBlueberry")
                    mock_db.search_by_season.assert_called_once_with("Summer")

    def test_exit_menu(self):
        with patch('builtins.input', side_effect=["999", "3"]) as mock_input:
            with patch('builtins.print') as mock_print:
                input_crop()

                mock_input.assert_called() 
                mock_print.assert_any_call("Invalid choice. Please try again.")  
                self.assertEqual(mock_input.call_count, 2)  
                mock_print.assert_any_call("Exiting Crop Search...")

    def test_exit_menu_directly(self):
        with patch('builtins.input', side_effect=["3"]) as mock_input:
            with patch('builtins.print') as mock_print:
                input_crop()

                mock_input.assert_called_once()
                mock_print.assert_any_call("Exiting Crop Search...")


