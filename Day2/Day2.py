import re

def possibleGames(file) -> int:
    gamesIdSum  = 0
    for line in file.read().splitlines():
        getIdGame = re.findall(r'Game (\d+)', line)
        gamevalue = line.replace(' ', '').split(':')[1].split(';')
        gamesIdSum += int(getIdGame[0])
    return gamesIdSum


def main():
    file = open("day2.txt", "r")
    print(possibleGames(file))
    file.close()

if __name__ == "__main__":
    main()
