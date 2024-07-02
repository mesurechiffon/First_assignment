import random

random_number = random.randint(1, 100)

chance = 0

while True:
    guess = input("숫자를 입력하세요: ")

    if not guess.isdigit():
        print("숫자가 아닙니다. 숫자를 입력하세요")
        continue

    guess = int(guess)

    # Restart decision
    if guess == random_number:
        print("맞았습니다")
        restart = input("다시 하시겠습니까? (y/n): ")
        if restart == "y" or restart == "Y":
            print(f"이전 게임 플레이어 최고 시도 횟수: {chance}")
            random_number = random.randint(1, 100)
            chance = 0
        elif restart == "n" or restart == "N":
            print("게임을 종료합니다")
            break
        else:
            print("유효한 입력이 아닙니다.")
            continue

    # Guess the number
    else:
        if guess < 1 or guess > 100:
            print("유효한 범위 내에 숫자를 입력하세요")
        elif guess < random_number:
            print("업")
            chance += 1
        elif guess > random_number:
            print("다운")
            chance += 1