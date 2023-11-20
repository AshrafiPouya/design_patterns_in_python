from random import randint

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

    def roll_dice_with_permission_checking(self, user):
        # checking permission here
        if not self.u_turn == user:
            return "its not your turn"
        
        self.change_turn()
        return randint(1, 6)
    

if __name__ == "__main__":
    u1 = User()
    u2 = User()

    game = DiceGame(u1=u1, u2=u2)

    print(game.roll_dice_with_permission_checking(u2))
    print(game.roll_dice_with_permission_checking(u1))
    print(game.roll_dice_with_permission_checking(u1))
    print(game.roll_dice_with_permission_checking(u2))
    print(game.roll_dice_with_permission_checking(u1))
        