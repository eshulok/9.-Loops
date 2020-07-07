import turtle as t

#How can you print hello 5 times?
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')

#Use string multiplation (and a new line character)
print('hello\n' * 5)

#Use a for loop
for x in range(0,5):
  print('hello')

#What is the range function doing?
for x in range(0,5):
  print('hello %s' % x)

#Let's look at this example from the '4. Lists' repl
inventory = ["wood", "stone", "apple", "fishing rod"]

#How we printed the inventory in one long string
print ("Your inventory contains: %s" % inventory)

#A nicer way to print it 
print ("Your inventory contains:")
for i in inventory:
  print(i)

#What are all the combinations possible from rolling 2 dice?
for i in range(1,7):
  for j in range(1,7):
    print(i, j)

#What are all the possible outcomes of flipping 3 coins?
outcomes = ['heads', 'tails']
for i in outcomes:
  for j in outcomes:
    for k in outcomes:
      print (i,j,k)

#while loops do something as long as a value is true
coins = 100
while coins > 0:
  coins = coins-3
  print('Coins remaining = %d' % coins)

#oops! Let's try again
coins = 100
while coins > 3:
  coins = coins-3
  print('Coins remaining = %d' % coins)

#Using loops with turtle
#How we drew a square before
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

for i in range(0,4):
  t.forward(100)
  t.left(90)