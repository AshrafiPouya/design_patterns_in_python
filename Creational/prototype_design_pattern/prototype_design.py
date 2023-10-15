class Saloon:
    def __init__(self, name, capacity) -> None:
        self.name = name
        self.capacity = capacity

class Customer:
    def __init__(self, name) -> None:
        self.name = name

class Reservation:
    def __init__(self, date_time, customer) -> None:
        self.date_time = date_time
        self.customer = customer


class Seat:
    def __init__(self, number, reservation) -> None:
        self.number = number
        self.reservation = reservation


class Day:
    def __init__(self, saloon, reservation, customer) -> None:
        self.saloon = saloon
        self.reservation = reservation
        self.customer = customer
        self.seats = list()
        self.prototype_seats()

    def prototype_seats(self):
        for number in range(self.saloon.capacity):
            self.seats.append(Seat(number=number, reservation=self.reservation))

if __name__ == "__main__":
    saloon1 = Saloon("saloon_1", 5)
    customer1 = Customer("customer1")
    reservation1 = Reservation("20230101", customer1)
    
    day1 = Day(saloon=saloon1, reservation=reservation1, customer=customer1)
    print(len(day1.seats))
    print(day1.seats[0].reservation.date_time)


    saloon2 = Saloon("saloon_2", 200)
    customer2 = Customer("customer2")
    reservation2 = Reservation("20230101", customer2)
    
    day2 = Day(saloon=saloon2, reservation=reservation2, customer=customer2)
    print(len(day2.seats))
    print(day2.seats[0].reservation.customer.name)

