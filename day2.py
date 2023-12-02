AMOUNT_COLOR_CUBES = {
    "RED": 12,
    "GREEN": 13,
    "BLUE": 14
}

def possible_game(cube_subsets):
    for cube_subset in cube_subsets:
        color_set = cube_subset.split(",")
        color_count = {"RED": 0, "GREEN": 0, "BLUE": 0}
        for col in color_set:
            color_list = col.strip().split(" ")
            color = color_list[1].upper()
            amount = int(color_list[0])
            color_count[color] += amount
            if color_count[color] > AMOUNT_COLOR_CUBES[color]:
                return False
    return True

def possible_game2(cube_subsets):
    min_color_cubes = {"RED": 0, "GREEN": 0, "BLUE": 0}
    for cube_subset in cube_subsets:
        color_set = cube_subset.split(",")
        color_count = {"RED": 0, "GREEN": 0, "BLUE": 0}
        for col in color_set:
            color_list = col.strip().split(" ")
            color = color_list[1].upper()
            amount = int(color_list[0])
            color_count[color] += amount
        for color in color_count:
            if color_count[color] > min_color_cubes[color]:
                min_color_cubes[color] = color_count[color]
    return min_color_cubes

def cube_power(color_cubes):
    power = 1
    for color in color_cubes:
        power *= color_cubes[color]
    return power

def parse_games():
    games = []
    file = open("data/day2.txt")
    for line in file:
        game = line.strip().split(":")
        game_id = int(game[0].split(" ")[1])
        cube_subsets = game[1].strip().split(";")
        games.append({"game_id": game_id, "cube_subsets": cube_subsets})
    return games

def part1():
    id_sum = 0
    games = parse_games()
    for game in games:
        if possible_game(game['cube_subsets']):
            id_sum += game['game_id']
    return id_sum

def part2():
    power_sum = 0
    games = parse_games()
    for game in games:
        min_color_cubes = possible_game2(game['cube_subsets'])
        power = cube_power(min_color_cubes)
        power_sum += power
    return power_sum


if __name__ == "__main__":
    print(part1())
    print(part2())