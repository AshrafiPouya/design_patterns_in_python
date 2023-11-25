from abc import abstractmethod, ABC


class User(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @property
    @abstractmethod
    def allowed():
        pass

class Manager(User):
    allowed = []

    def __init__(self, name) -> None:
        super().__init__(name)


class Operator(User):
    allowed = [Manager]

    def __init__(self, name) -> None:
        super().__init__(name)

class Client(User):
    allowed = [Operator]

    def __init__(self, name) -> None:
        super().__init__(name)


class Message:
    def __init__(self, message="", *, sender) -> None:
        self.message = message
        self.flow = [sender]
        self.sender = sender

    @property
    def current_user(self):
        return self.flow[-1]

    def send(self, receiver: User):
        if receiver.__class__ not in self.current_user.allowed:
            print(f"You dont have permission to send message to {receiver.name}")
            return
        print(f"{self.message} is received from {self.current_user.name} you are {receiver.name}")
        self.flow.append(receiver)



if __name__ == "__main__":
    client = Client('client')
    operator = Operator('operator')
    manager = Manager('manager')

    m1 = Message("message 1", sender=client)
    m2 = Message("message 2", sender=operator)

    m1.send(manager)
    m1.send(operator)
    print(m1.current_user)

    m1.send(manager)
    print(m1.current_user)
    
