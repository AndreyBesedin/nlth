#TODO 7-cards hand evaluation
#TODO more border cases in tests
#TODO or not: acelerate computations, remove unnecesairy checks
# any hand is a list of shape [[value, 'color'], [value, 'color'], ...]
def is_straight_flush(values, colors):
  return is_straight(values) and is_flush(colors)

def is_four_of_a_kind(values):
  return max([values.count(x) for x in set(values)])==4

def is_full_house(values):
  return len(set(values))==2 and max([values.count(x) for x in set(values)])==3

def is_flush(colors):
  return len(set(colors))==1

def is_straight(values):
  return list(range(values[-1], values[-1] + 5))==list(reversed(values)) or (values[0]==14 and values[1:]==[5, 4, 3, 2])

def is_three_of_a_kind(values):
  return len(set(values))==3 and max([values.count(x) for x in set(values)])==3

def is_two_pairs(values):
  return not is_three_of_a_kind(values) and len(set(values))==3

def is_one_pair(values):
  return len(set(values))==4

def five_card_rank(five_cards):
  five_cards.sort(reverse=True)
  values = [five_cards[i][0] for i in range(len(five_cards))]
  colors = [five_cards[i][1] for i in range(len(five_cards))]
  S = set(values)
  if is_straight_flush(values, colors):
    if values == [14, 5, 4, 3, 2]:
      return [[8], [5, 4, 3, 2, 1]]
    return [[8], values]  
  elif is_four_of_a_kind(values):
    quad_val = [x for x in S if values.count(x)==4]
    single_val = [x for x in S if values.count(x)==1]
    return [[7], quad_val, single_val]
  elif is_full_house(values):
    tripled_val = [x for x in S if values.count(x)==3]
    doubled_val = [x for x in S if values.count(x)==2]
    return [[6], tripled_val, doubled_val] 
  elif is_flush(colors):
    return [[5], values] 
  elif is_straight(values):
    if values == [14, 5, 4, 3, 2]:
      return [[4], [5, 4, 3, 2, 1]]
    return [[4], values] 
  elif is_three_of_a_kind(values):
    tripled_val = [x for x in S if values.count(x)==3]
    return [[3], tripled_val, values]  
  elif is_two_pairs(values):
    doubled_vals = [x for x in S if values.count(x)==2]
    return [[2], list(reversed(doubled_vals)), values] 
  elif is_one_pair(values):
    doubled_val = [x for x in S if values.count(x)==2]
    return [[1], doubled_val, values]
  return [[0], values]

def full_hand_rank(full_hand):
  rank = [[0]]
  for idx_first in range(6):
    six_cards = full_hand[:idx_first] +  full_hand[idx_first+1:]
    for idx_second in range(idx_first+1, 7):
      five_cards = six_cards[:idx_second-1] +  six_cards[idx_second:]
      rank = max(rank, five_card_rank(five_cards))
  return rank

def run_tests():
  test_count = 0
  # One pair tests
  print('Test 1 ' + str(five_card_rank([[2, 'c'], [3, 'd'], [10, 'h'], [3, 's'], [14, 's']]) == [[1], [3], [14, 10, 3, 3, 2]]))
  # Two pairs tests
  print('Test 2 ' + str(five_card_rank([[2, 'c'], [3, 'd'], [10, 'h'], [3, 's'], [2, 's']]) == [[2], [3, 2], [10, 3, 3, 2, 2]]))
  # Three of a kind tests
  print('Test 3 ' + str(five_card_rank([[2, 'c'], [3, 'd'], [10, 'h'], [3, 's'], [3, 's']]) == [[3], [3], [10, 3, 3, 3, 2]]))
  # Straight tests
  print('Test 4 ' + str(five_card_rank([[2, 'c'], [3, 'd'], [6, 'h'], [4, 's'], [5, 's']]) == [[4], [6, 5, 4, 3, 2]]))
  print('Test 5 ' + str(five_card_rank([[2, 'c'], [4, 'd'], [3, 'h'], [5, 's'], [14, 's']]) == [[4], [5, 4, 3, 2, 1]]))
  print('Test 6 ' + str(five_card_rank([[12, 'c'], [11, 'd'], [13, 'h'], [10, 's'], [14, 's']]) == [[4], [14, 13, 12, 11, 10]]))
  # Flush tests
  print('Test 7 ' + str(five_card_rank([[2, 'c'], [3, 'c'], [6, 'c'], [4, 'c'], [9, 'c']]) == [[5], [9, 6, 4, 3, 2]]))
  # Full-house tests
  print('Test 8 ' + str(five_card_rank([[2, 'c'], [3, 'c'], [3, 's'], [2, 's'], [2, 'h']]) == [[6], [2], [3]]))
  # Four of a kind tests
  print('Test 9 ' + str(five_card_rank([[2, 'c'], [2, 'd'], [3, 's'], [2, 's'], [2, 'h']]) == [[7], [2], [3]]))
  print('Test 10 ' + str(five_card_rank([[3, 'c'], [3, 'd'], [3, 's'], [2, 's'], [3, 'h']]) == [[7], [3], [2]]))
    # Straight flush tests
  print('Test 11 ' + str(five_card_rank([[2, 'c'], [3, 'c'], [6, 'c'], [4, 'c'], [5, 'c']]) == [[8], [6, 5, 4, 3, 2]]))
  print('Test 12 ' + str(five_card_rank([[2, 'c'], [4, 'c'], [3, 'c'], [5, 'c'], [14, 'c']]) == [[8], [5, 4, 3, 2, 1]]))
  print('Test 13 ' + str(five_card_rank([[12, 's'], [11, 's'], [13, 's'], [10, 's'], [14, 's']]) == [[8], [14, 13, 12, 11, 10]]))
  
  