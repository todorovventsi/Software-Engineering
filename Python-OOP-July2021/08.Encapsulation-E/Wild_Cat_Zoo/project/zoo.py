from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):  # animal: instance of Lion/Tiger/Cheetah/
        if price <= self.__budget and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif price > self.__budget and self.__animal_capacity > 0:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):  # worker: instance of Keeper/Caretaker/Vat
        if self.__workers_capacity > 0:
            self.workers.append(worker)
            # self.__workers_capacity -= 1
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        worker = [worker for worker in self.workers if worker.name == worker_name]
        if worker:
            worker = worker[0]
            self.workers.remove(worker)
            self.__workers_capacity += 1
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = sum(worker.salary for worker in self.workers)
        if needed_money <= self.__budget:
            self.__budget -= needed_money
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money = sum(animal.money_for_care for animal in self.animals)
        if needed_money <= self.__budget:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount
        return

    def animals_status(self):
        lions = [f"{animal.__repr__()}" for animal in self.animals if isinstance(animal, Lion)]
        tigers = [f"{animal.__repr__()}" for animal in self.animals if isinstance(animal, Tiger)]
        cheetahs = [f"{animal.__repr__()}" for animal in self.animals if isinstance(animal, Cheetah)]
        separator = "\n"
        return f"You have {len(self.animals)} animals\n" \
               f"----- {len(lions)} Lions:\n" \
               f"{separator.join(lions)}\n" \
               f"----- {len(tigers)} Tigers:\n" \
               f"{separator.join(tigers)}\n" \
               f"----- {len(cheetahs)} Cheetahs:\n" \
               f"{separator.join(cheetahs)}"

    def workers_status(self):
        keepers = [f"{worker.__repr__()}" for worker in self.workers if isinstance(worker, Keeper)]
        caretakers = [f"{worker.__repr__()}" for worker in self.workers if isinstance(worker, Caretaker)]
        vets = [f"{worker.__repr__()}" for worker in self.workers if isinstance(worker, Vet)]
        separator = "\n"
        return f"You have {len(self.workers)} workers\n" \
               f"----- {len(keepers)} Keepers:\n" \
               f"{separator.join(keepers)}\n" \
               f"----- {len(caretakers)} Caretakers:\n" \
               f"{separator.join(caretakers)}\n" \
               f"----- {len(vets)} Vets:\n" \
               f"{separator.join(vets)}"
