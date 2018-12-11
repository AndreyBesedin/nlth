# any hand is a list of shape [[value, 'color'], [value, 'color'], ...]
def is_straight_flush(five_cards):
  if is_straight(five_cards) and is_flush(five_cards):
    return True
  return False

def is_four_of_a_kind(five_cards):
  values = list(hand[i][0] for i in range(len(hand)))

def get_combination_rank(five_cards):
  if is_straight_flush(five_cards):
    return (8, highest_card_val) #define structure 
  elif is_four_of_a_kind(five_cards):
    return (7, card_of_four, kicker)
  elif is_full_house(five_cards):
    return (6, card_of_three, card_of_two) 
  elif is_flush(five_cards):
    return (5, decreasing card values)
  elif is_straight(five_cards):
    return (4, highest_card_val - if not Ace to four)
  elif is_three_of_a_kind(five_cards):
    return (3, card_of_three, higher kicker, lower kicker) 
  elif is_two_pairs(five_cards):
    return (2, higher pair, lower pair, kicker)
  elif is_one_pair(five_cards):
    return (1, card_of_two, top_kicker, mid_kicker, low_kicker)
  return (0, sorted_values)





def run_tests():
