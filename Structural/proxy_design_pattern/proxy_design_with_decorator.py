from random import randint

# implement proxy design pattern with decoration
def permission_checking(func):

    def internal_func(obj, user):
        if obj.u_turn != user:
            return "sorry it not your turn"

        return func(obj, user)

    return internal_func


class User:
    def __init__(self) -> None:
        pass

class DiceGame:
    def __init__(self, u1, u2) -> None:
        self.u1 = u1
        self.u2 = u2
        self.u_turn = u1

    def change_turn(self):
        self.u_turn = self.u2 if self.u_turn == self.u1 else self.u1


    @permission_checking
    def roll_dice(self, user):
        self.change_turn()
        return randint(1, 6)
    

if __name__ == "__main__":
    u1 = User()
    u2 = User()

    game = DiceGame(u1=u1, u2=u2)

    print(game.roll_dice(u2))
    print(game.roll_dice(u1))
    print(game.roll_dice(u1))
    print(game.roll_dice(u2))
    print(game.roll_dice(u1))
        