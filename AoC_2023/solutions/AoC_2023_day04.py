import re

input_file = 'input_files\AoC_2023_day04_input.txt'

def winningcards(line: str):
    game = re.split(r':|\|', line)
    winning_nums = game[1].split()
    hand = game[2].split()
    
    points = 0 
    for num in hand:
        if num in winning_nums:
            if points == 0:
                points += 1
            else:
                points *= 2
    return points

def totalpoint():
    total = 0
    with open(input_file) as input:
        for line in input:
            val = winningcards(line)
            total += val
    print(total)

def winningcards2(line: str):
    """ Part Two. Find how many extra cards are won per card """
    game = re.split(r':|\|', line)
    card = int(game[0].split()[1])
    winning_nums = game[1].split()
    hand = game[2].split()
    
    points = 0 
    for num in hand:
        if num in winning_nums:
            points += 1
    return points, card

def totalcards():
    total_cards = {
        1: 1,
    }

    with open(input_file) as input:
        for line in input:
            copies, card_id, = winningcards2(line)
            next_card = card_id + 1
            
            if card_id not in total_cards:
                total_cards[card_id] = total_cards.get(card_id, 1)

            for _ in range(copies):
                if next_card in total_cards:
                    total_cards[next_card] += total_cards[card_id]
                else:
                    total_cards[next_card] = total_cards.get(next_card, 1) * total_cards[card_id] + 1
                next_card += 1
    
    print(sum(total_cards.values()))

if __name__ == "__main__":
    totalpoint()
    totalcards()