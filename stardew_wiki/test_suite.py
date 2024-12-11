import unittest
import test_recipe_search 
import test_ingredient_search 
import test_animals
import test_crops

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_recipe_search.TestRecipeSearch))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_ingredient_search.TestIngredientSearch))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_animals.TestAnimalDatabase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_animals.TestInputAnimal))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_crops.TestCropDatabase))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_crops.TestInputCrop))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    print(runner.run(suite()))
