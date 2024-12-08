import unittest
import test_recipe_search 
import test_ingredient_search 

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_recipe_search.TestRecipeSearch))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_ingredient_search.TestIngredientSearch))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
