from os import system



bidings = {}

other_bid = True
while other_bid == True:
 name = input("What's your name ?")
 bid = input("What's your bid? $")
 bidings[name] = bid
 someone_more = input("There's someone else to give a bid? y/n").lower()
 if someone_more != 'y':
  other_bid = False

num_test = 0
winner_bid = 0
winner_person = ''
for key in bidings:
 if int(bidings[key]) > num_test:
  num_test = int(bidings[key])
  winner_bid = num_test
  winner_person = key

print(f'{winner_person} wins with a ${winner_bid} bid')




