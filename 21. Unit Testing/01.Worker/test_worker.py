from unittest import TestCase, main
from Worker_Folder.worker import Worker


class WorkerTests(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Test_name", 25_000, 100)

    def test_class_initialization(self):
        self.assertEqual("Test_name", self.worker.name)
        self.assertEqual(25_000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_method_if_enough_energy_to_work(self):
        expected_energy = self.worker.energy - 1
        expected_money = self.worker.salary

        self.worker.work()
        self.assertEqual(expected_energy, self.worker.energy)
        self.assertEqual(expected_money, self.worker.money)

    def test_work_method_if_NOT_enough_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_energy_after_rest(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_get_info_return_valid_string(self):
        self.assertEqual(
            f"{self.worker.name} has saved {self.worker.money} money.",
            self.worker.get_info()
        )


if __name__ == '__main__':
    main()
