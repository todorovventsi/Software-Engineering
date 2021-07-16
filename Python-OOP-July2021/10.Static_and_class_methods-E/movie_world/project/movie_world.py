class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        tenant = None
        for customer in self.customers:
            if customer.id == customer_id:
                tenant = customer

        for dvd in self.dvds:
            if dvd.id == dvd_id:
                if dvd.is_rented:
                    if dvd not in tenant.rented_dvds:
                        return "DVD is already rented"
                    return f"{tenant.name} has already rented {dvd.name}"
                if tenant.age < dvd.age_restriction:
                    return f"{tenant.name} should be at least {dvd.age_restriction} to rent this movie"
                dvd.is_rented = True
                tenant.rented_dvds.append(dvd)
                return f"{tenant.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        tenant = None
        for customer in self.customers:
            if customer.id == customer_id:
                tenant = customer

        for dvd in self.dvds:
            if dvd.id == dvd_id:
                if dvd in tenant.rented_dvds:
                    dvd.is_rented = False
                    tenant.rented_dvds.remove(dvd)
                    return f"{tenant.name} has successfully returned {dvd.name}"
                return f"{tenant.name} does not have that DVD"

    def __repr__(self):
        customers_info = [repr(customer) for customer in self.customers]
        dvds_info = [repr(dvd) for dvd in self.dvds]
        message = customers_info + dvds_info
        nl = "\n"
        return f"{nl.join(message)}"


