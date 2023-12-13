from collections import Counter

input_file = 'input_files\AoC_2023_day07_input.txt'
# input_file = 'input_files\day07example.txt'

Hands = []

def parse_data():
    global Hands

    with open(input_file) as input:
        for line in input:
            hand, bid = line.split()
            Hands.append((hand, int(bid)))

def hand_strength(hand: str):
    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('J', chr(ord('9') + 2))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))

    hand_freq = Counter(hand)

    if len(hand_freq) == 5:
        return (1, hand) # 5 cards
    elif len(hand_freq) == 4:
        return (2, hand) # one pair
    elif len(hand_freq) == 3:
        if 2 in hand_freq.values():
            return (3, hand) # two pair
        elif 3 in hand_freq.values():
            return (4, hand) # three of a kind
    elif len(hand_freq) == 2:
        if 3 in hand_freq.values():
            return (5, hand) # full house
        elif 4 in hand_freq.values():
            return (6, hand) # 4 of a kind
    elif len(hand_freq) == 1:
        return (7, hand) # 5 of a kind

def hand_str_joker(hand: str):
    hand = hand.replace('J', chr(ord('1') - 1)) # transformed 'J' into '0'

    hand = hand.replace('T', chr(ord('9') + 1))
    hand = hand.replace('Q', chr(ord('9') + 3))
    hand = hand.replace('K', chr(ord('9') + 4))
    hand = hand.replace('A', chr(ord('9') + 5))

    hand_freq = Counter(hand)

    if len(hand_freq) == 5:
        if '0' in hand:
            return (2, hand)
        else:
            return (1, hand)
    
    elif len(hand_freq) == 4:
        if '0' in hand:
            return (4, hand)
        else:
            return (2, hand)
    
    elif len(hand_freq) == 3:
        if 2 in hand_freq.values():
            if ('0', 2) in hand_freq.items():
                return (6, hand)
            elif ('0', 1) in hand_freq.items():
                return (5, hand)
            else:
                return (3, hand)
        elif 3 in hand_freq.values():
            if '0' in hand:
                return (6, hand)
            else:
                return (4, hand)
    elif len(hand_freq) == 2:
        if '0' in hand:
            return (7, hand)
        elif 3 in hand_freq.values():
            return (5, hand)
        elif 4 in hand_freq.values():
            return (6, hand)
    elif len(hand_freq) == 1:
        return (7, hand)

if __name__ == "__main__":
    parse_data()

    Hands = sorted(Hands, key=lambda x: hand_str_joker(x[0]))
    print(Hands)
    total_winnings = 0
    for rank, (hand, bid) in enumerate(Hands, 1):
        total_winnings += rank * int(bid)
    print(total_winnings)
