from test_worker.project.worker import Worker

from unittest import TestCase, main


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker(name="Test Worker", salary=100, energy=100)

    def test_if_worker_is_initialized_correctly(self):
        self.assertEqual("Test Worker", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_if_energy_increasing_after_rest(self):
        initial_energy = self.worker.energy
        self.assertEqual(100, self.worker.energy)
        self.worker.rest()
        self.assertGreater(self.worker.energy, initial_energy)

    def test_if_worker_tries_to_work_with_negative_energy_raises(self):
        worker = Worker(name="Test Worker", salary=100, energy=0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        exception_msg = "Not enough energy."
        self.assertEqual(exception_msg, str(ex.exception))

    def test_if_worker_money_increase_after_work(self):
        self.assertEqual(0, self.worker.money)
        self.worker.work()
        self.assertEqual(100, self.worker.money)

    def test_worker_energy_decrease_after_work(self):
        self.assertEqual(100, self.worker.energy)
        self.worker.work()
        self.assertLess(self.worker.energy, 100)

    def test_get_info_method(self):
        result = self.worker.get_info()
        self.assertEqual('Test Worker has saved 0 money.', result)


if __name__ == "__main__":
    main()
