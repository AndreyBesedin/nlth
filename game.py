# Stage 1: let's make a game simulator

players = {}
players['1'] = bots.smart_bot()
players['2'] = bots.human()


table = install_players(players) if len(players)>0

while len(players)>1:
  deck = mix_deck()
  table.distribute_cards(deck)
  table
