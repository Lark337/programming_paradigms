from desk import desk
from veiw_desk import view_desk
from checker import checker
from player_switch import player_switch

class controller:
    def __init__(self):
        self.desk = desk()
        self.view_desk = view_desk(self.desk.get_list())
        self.checker = checker(self.desk.get_list())

    def current(self,n):
        switch = 0
        while switch == 0:
            curr = int(input(f'{n} игрок: '))
            if self.desk[curr - 1] != 'X' and self.desk[curr - 1] != 'O':
                switch = 1
            else:
                print('Клетка уже занята')
        if n == 1:
            self.desk[curr - 1] = 'X'
        else: 
            self.desk[curr - 1] = 'O'

    def start_game(self):
        count = 0
        self.view_desk.pole()
        while count != 9:
            player_switch.current(self.desk.get_list(),1)
            count += 1
            self.view_desk.pole()
            if self.checker.check():
                print('Победил первый игрок')
                break
            if count == 9:
                print('Ничья')
                break
            player_switch.current(self.desk.get_list(),2)
            count += 1
            self.view_desk.pole()
            if self.checker.check():
                print('Победил второй игрок')
                break
            print(count)


