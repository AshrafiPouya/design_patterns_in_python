from notify import PushNotification, SMSNotification
from decorators import notify_observers

class Product:
    pass


class Purchase:
    observers = [PushNotification, SMSNotification]

    def __init__(self, products_list) -> None:      
        self.products = products_list
        self.is_paid = False

    @notify_observers(message="chekout is done")
    def checkout(self):
        self.is_paid = True
