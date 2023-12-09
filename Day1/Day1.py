import re

def getTotal(file):
    totalSum = 0
    for lines in file.read().splitlines():
        firstNumber=None
        lastNumber=None
        for index, char in enumerate(lines):
            try:
                if firstNumber==None:
                    firstNumber = int(char)
                lastNumber = int(char)
            except  ValueError:
                continue
        totalSum += firstNumber * 10 + lastNumber
    return totalSum

def getIntFromNumberInLetter(numberInLetter) -> int:
    match numberInLetter:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            return int(numberInLetter)
        

def getTotalV2(file) -> int:
    totalSum  = 0
    for lines in file.read().splitlines():
        getFirstDigit = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|[0-9]).*$', lines)
        getLastDigit = re.findall(r'.*(one|two|three|four|five|six|seven|eight|nine|[0-9]).*$', lines)
        firstDigit = getIntFromNumberInLetter(getFirstDigit[0])
        lastDigit = getIntFromNumberInLetter(getLastDigit[0])
        totalSum += firstDigit * 10 + lastDigit
    return totalSum


def main():
    file = open("day1.txt", "r")
    print(getTotalV2(file))
    file.close()

if __name__ == "__main__":
    main()
