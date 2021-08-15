from unittest import TestCase, main

from project.pet_shop import PetShop


class TestPetShop(TestCase):

    def setUp(self):
        self.pet_shop = PetShop("test_name")

    def test_correct_initialization(self):
        self.assertEqual("test_name", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_less_then_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("food_name", -1)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ex.exception))

    def test_add_food_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("food_name", 0)
        self.assertEqual("Quantity cannot be equal to or less than 0", str(ex.exception))

    def test_added_new_food(self):
        msg = self.pet_shop.add_food("meat", 1)
        self.assertEqual({"meat": 1}, self.pet_shop.food)
        self.assertEqual("Successfully added 1.00 grams of meat.", msg)

    def test_added_more_food(self):
        msg = self.pet_shop.add_food("meat", 1)
        self.assertEqual({"meat": 1}, self.pet_shop.food)
        self.assertEqual("Successfully added 1.00 grams of meat.", msg)
        msg_2 = self.pet_shop.add_food("Granula", 100)
        self.assertEqual({"meat": 1, "Granula": 100}, self.pet_shop.food)
        self.assertEqual("Successfully added 100.00 grams of Granula.", msg_2)

    def test_increase_food(self):
        msg = self.pet_shop.add_food("meat", 1)
        msg_2 = self.pet_shop.add_food("meat", 1)
        self.assertEqual({"meat": 2}, self.pet_shop.food)
        self.assertEqual("Successfully added 1.00 grams of meat.", msg)
        self.assertEqual("Successfully added 1.00 grams of meat.", msg_2)

    def test_add_pet(self):
        msg = self.pet_shop.add_pet("Jack")
        self.assertEqual(["Jack"], self.pet_shop.pets)
        self.assertEqual("Successfully added Jack.", msg)

    def test_add_another_pet(self):
        msg = self.pet_shop.add_pet("Jack")
        self.assertEqual(["Jack"], self.pet_shop.pets)
        self.assertEqual("Successfully added Jack.", msg)
        msg_2 = self.pet_shop.add_pet("Tobi")
        self.assertEqual(["Jack", "Tobi"], self.pet_shop.pets)
        self.assertEqual("Successfully added Tobi.", msg_2)

    def test_add_existing_pet_raises(self):
        msg = self.pet_shop.add_pet("Jack")
        self.assertEqual("Successfully added Jack.", msg)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Jack")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_not_in_pets_raises(self):
        self.pet_shop.add_pet("Tobi")
        self.pet_shop.add_food("Granula", 200)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Granula", "Jack")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_wrong_food(self):
        self.pet_shop.add_pet("Jack")
        self.pet_shop.add_food("Granula", 200)
        msg = self.pet_shop.feed_pet("meat", "Jack")
        self.assertEqual("You do not have meat", msg)

    def test_feed_pet_with_less_then_100(self):
        self.pet_shop.add_food("Granula", 90)
        self.pet_shop.add_pet("Jack")
        msg = self.pet_shop.feed_pet("Granula", "Jack")
        self.assertEqual("Adding food...", msg)

    def test_feed_pet(self):
        self.pet_shop.add_food("Granula", 200)
        self.pet_shop.add_pet("Jack")
        msg = self.pet_shop.feed_pet("Granula", "Jack")
        self.assertEqual(100, self.pet_shop.food["Granula"])
        self.assertEqual("Jack was successfully fed", msg)

    def test_repr_method(self):
        self.pet_shop.add_pet("Jack")
        self.pet_shop.add_pet("Simba")
        msg = f'Shop {self.pet_shop.name}:\n' \
              f'Pets: {", ".join(self.pet_shop.pets)}'
        self.assertEqual(msg, repr(self.pet_shop))


if __name__ == "__main__":
    main()
