from test_cat.cat_class.cat import Cat

from unittest import TestCase, main


class CatTests(TestCase):

    def setUp(self) -> None:
        self.cat = Cat("TestName")

    def test_initialization(self):
        self.assertEqual("TestName", self.cat.name)
        self.assertFalse(self.cat.sleepy)
        self.assertFalse(self.cat.fed)
        self.assertEqual(0, self.cat.size)

    def test_if_cat_size_increasing_after_eat_methode(self):
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        self.assertGreater(self.cat.size, 0)

    def test_if_cat_is_fed_after_eating_methode(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_if_cat_cannot_eat_after_already_fed(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_if_cat_cannot_sleep_if_not_fed(self):
        self.assertFalse(self.cat.fed)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_if_cat_is_not_sleepy_after_sleep(self):
        self.assertFalse(self.cat.sleepy)
        self.cat.sleepy = True
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
