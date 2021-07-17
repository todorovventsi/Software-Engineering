class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def get_ids(id, collection):
        for item in collection:
            if id == item.id:
                return item

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = Gym.get_ids(subscription_id, self.subscriptions)
        customer = Gym.get_ids(subscription_id, self.customers)
        trainer = Gym.get_ids(subscription_id, self.trainers)
        plan = Gym.get_ids(subscription_id, self.plans)
        equipment = Gym.get_ids(subscription_id, self.equipment)
        return f"{subscription!r}\n{customer!r}\n{trainer!r}\n{equipment!r}\n{plan!r}"
