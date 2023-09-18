class player_switch:
    @staticmethod
    def current(desk,n):
            switch = 0
            while switch == 0:
                curr = int(input(f'{n} игрок: '))
                if desk[curr - 1] != 'X' and desk[curr - 1] != 'O':
                    switch = 1
                else:
                    print('Клетка уже занята')
            if n == 1:
                desk[curr - 1] = 'X'
            else: 
                desk[curr - 1] = 'O'