class Subscription:
    __next_id = 1

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = __class__.__next_id
        __class__.__next_id += 1

    @staticmethod
    def get_next_id():
        return __class__.__next_id

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
