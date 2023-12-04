def count_winning_numbers(winners, my_numbers):
    num_winning_numbers = 0
    for number in my_numbers:
        if number in winners:
            num_winning_numbers += 1
    return num_winning_numbers


def add_tickets(number_of_each_card, card_id, amount=1):
    if card_id not in number_of_each_card:
        number_of_each_card[card_id] = amount
    else:
        number_of_each_card[card_id] += amount


def part1():
    total_points = 0
    number_of_each_card = {}
    file = open('data/day4.txt')
    for line in file:
        line = line.strip()
        card = line.split(":")
        card_id = int(card[0].strip().replace("  ", " ").split()[1])
        add_tickets(number_of_each_card, card_id)
        numbers = card[1].strip().split("|")
        winning_numbers = numbers[0].strip().replace("  ", " ").split(" ")
        my_numbers = numbers[1].strip().replace("  ", " ").split(" ")
        amount = number_of_each_card[card_id]
        matches = count_winning_numbers(winning_numbers, my_numbers)
        winning_tickets = [ticket for ticket in range(card_id + 1, card_id + 1 + matches)]
        for ticket in winning_tickets:
            add_tickets(number_of_each_card, ticket, amount)
        # if matches != 0:
        #     points = 2 ** (matches - 1)
        # total_points += points
    return sum(number_of_each_card.values())


print(part1())
