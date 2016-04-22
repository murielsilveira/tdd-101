from unittest import TestCase
from add_one import add_one


class AddOneTests(TestCase):

    def test_with_zero(self):
        result = add_one(0)

        self.assertEqual(1, result)
