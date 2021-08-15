from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self):
        self.factory = PaintFactory("Test_name", 100)

    def test_correct_initialization(self):
        self.assertEqual("Test_name", self.factory.name)
        self.assertEqual(100, self.factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)
        self.assertEqual({}, self.factory.ingredients)




if __name__ == "main":
    main()