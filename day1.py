from enum import IntEnum


class Numbers(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9

    @classmethod
    def is_value(self, number):
        return number.upper() in self._member_names_


def part1():
    file = open("data/day1.txt")
    result = 0
    for line in file:
        line = line.strip()
        first_digit = None
        last_digit = None
        for character in line:
            if character.isdigit():
                last_digit = character
                if first_digit is None:
                    first_digit = character

        num = int(first_digit + last_digit)
        result += num

    print(result)


def part2():
    file = open("data/day1.txt")
    result = 0
    for line in file:
        line = line.strip()
        first = None
        last = None
        for pointer1 in range(len(line)):
            word = line[pointer1]
            if word.isdigit():
                last = word
                if first is None:
                    first = word
            for pointer2 in range(pointer1 + 1, len(line) + 1):
                if Numbers.is_value(word):
                    number = Numbers[word.upper()]
                    last = number
                    if first is None:
                        first = number
                if pointer2 < len(line):
                    word += line[pointer2]

        num = int(str(int(first)) + str(int(last)))
        result += num

    print(result)


if __name__ == "__main__":
    part2()
