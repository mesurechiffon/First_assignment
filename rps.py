import random

# Number of ways to win.
winning_cases = {
    "가위": "보",
    "바위": "가위",
    "보": "바위"
}

rps = list(winning_cases.keys())

# Game result.


def rps_game(user_rps, bot_rps):
    if user_rps == bot_rps:
        return "draw"
    elif winning_cases[user_rps] == bot_rps:
        return "win"
    else:
        return "lose"


# Counting results.
cnt_win = 0
cnt_lose = 0
cnt_draw = 0

# Game start
while True:
    user_rps = input("가위, 바위, 보 중 하나를 입력하세요: ")

    if user_rps not in rps:
        print("유효한 입력이 아닙니다")
        continue

    bot_rps = random.choice(rps)

    print(f"사용자: {user_rps}, 컴퓨터: {bot_rps}")

    result = rps_game(user_rps, bot_rps)

    if result == "win":
        print("사용자 승리!")
        cnt_win += 1
    elif result == "lose":
        print("컴퓨터 승리!")
        cnt_lose += 1
    else:
        print("무승부입니다.")
        cnt_draw += 1

    # Restart decision
    while True:
        restart = input("다시 하겠습니까? (y/n): ")
        if restart == "y" or restart == "Y":
            break
        elif restart == "n" or restart == "N":
            print(f"게임을 종료합니다\n승: {cnt_win} 패: {cnt_lose} 무승부: {cnt_draw}")
            exit()
        else:
            print("유효한 입력이 아닙니다")
            continue