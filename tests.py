import unittest


import utils


class TestUtils(unittest.TestCase):

    def test_height_prct(self):
        self.assertEqual(utils.height_prct(25), 180.0)
