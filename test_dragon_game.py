# Testing Dragon Game with pytest

import unittest
from dragon_game import check_ingred_api
from dragon_game import get_name

class TestDragonGame(unittest.TestCase):
    def test_check_ingred_api(self):
        api_return = check_ingred_api()
        code = api_return.status_code
        self.assertEqual(code, 200)
    def test_get_name(self):
        api_return = get_name(7)
        self.assertEqual(len(api_return), 7)
        self.assertEqual(type(api_return), str)

if __name__ == "__main__":
    unittest.main()

# Output
"""
..
----------------------------------------------------------------------
Ran 2 tests in 3.404s

OK
"""