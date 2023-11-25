from abc import ABC, abstractmethod

class BaseNotification(ABC):

    @staticmethod
    @abstractmethod
    def send(message = None, where = None):
        pass

class PushNotification(BaseNotification):

    @staticmethod
    def send(message=None):
        print(f'{message} in push')
    
class SMSNotification(BaseNotification):
    
    @staticmethod
    def send(message=None):
        print(f'{message} in sms')

class EmailNotification(BaseNotification):

    @staticmethod
    def send(message=None):
        print(f'{message} in email')
