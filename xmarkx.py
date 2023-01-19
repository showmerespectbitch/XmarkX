board = list(range(1, 10)) #Глобальная переменная

winner_combinations = [(1, 2, 3,), (4, 5, 6), (7, 8, 9), (1, 4, 7,), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)] # Комбинации для победы


def draw_board(): #функция для создания игрового поля
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
    print("------------")


def take_input(player_token):
    while True:
        value = input("Куда вы хотите поставить" + player_token + " ?")
        if value not in "123456789":
            print("Ошибочный ввод! Повторите еще раз!")
            continue
        value = int(value)
        if str(board[value - 1]) not in "XO":
            board[value - 1] = player_token
            break
        print("Эта клетка уже занята!")


def chek_winner():
    for each in winner_combinations:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    count = 0
    while True:
        draw_board()
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if count > 3:
            winner = chek_winner()
            if winner:
                draw_board()
                print(winner,"Вы победили!!!")
            count += 1
            if count > 8:
                draw_board()
                print("Победила дружба!!!")
                break


main()






