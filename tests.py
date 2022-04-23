import unittest


import utils


class TestUtils(unittest.TestCase):

    def test_height_prct(self):
        self.assertEqual(utils.height_prct(25), 180.0)


    def test_width_prct(self):
        self.assertEqual(utils.width_prct(25), 360.0)
