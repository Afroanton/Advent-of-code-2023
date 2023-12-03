def create_schematic():
    schematic = []
    file = open("data/day3.txt")
    for line in file:
        row = []
        lines = line.strip()
        row.extend(lines)
        schematic.append(row)
    return schematic


def is_part(schematic, position):
    for row_nr in range(position[0] - 1, position[0] + 2):
        for column_nr in range(position[1] - 1, position[1] + 2):
            if 0 <= row_nr < len(schematic) and 0 <= column_nr < len(schematic[0]):
                if is_symbol(schematic[row_nr][column_nr]):
                    return True
    return False


def is_symbol(character):
    if not character.isnumeric() and character != ".":
        return True
    else:
        return False


def get_all_parts(schematic):
    part_numbers = []
    for row_nr, row in enumerate(schematic):
        adjacent = False
        number = ""
        for column_nr, value in enumerate(row):
            if value.isdigit():
                number += value
                adjacent = is_part(schematic, (row_nr, column_nr)) or adjacent
            elif number != "":
                if adjacent:
                    part_numbers.append(number)
                    adjacent = False
                number = ""
        if adjacent:
            part_numbers.append(number)
    return part_numbers


def sum_of_parts(parts):
    parts_sum = 0
    for part in parts:
        parts_sum += int(part)
    return parts_sum


def part1():
    schematic = create_schematic()
    parts = get_all_parts(schematic)
    print(parts)
    return sum_of_parts(parts)


if __name__ == '__main__':
    print(part1())
