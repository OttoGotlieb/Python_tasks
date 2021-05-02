import random 
import sys

# /////////////////////////////////////////////////////////////////////////////////////

articles = ['a', 'the', 'this', 'her', 'his']
nouns = ['cat', 'dog', 'man', 'woman', 'boy', 'girl', 'astronaut', 'author', 'hero']
verbs = ['brought', 'become', 'caught', 'fallen', 'had', 'known', 'left', 'lost', 
         'made', 'put', 'spoiled', 'understood', 'won', 'written']
adverbs = ['loudly', 'already', 'yet', 'soon', 'accurately', 'badly', 'anxiously',
          'extremely', 'quite', 'remarkably', 'especially', 'particularly', 'only', 
          'generally', 'enough', 'rather', 'awfully', 'completely', 'pretty']

# /////////////////////////////////////////////////////////////////////////////////////

rows = sys.argv[1]

try:
    rows = int(rows)
except ValueError:
    print('incorect input')

# /////////////////////////////////////////////////////////////////////////////////////

for i in range(0, rows):
    x = random.randint(0, 1)
    if(x == 0):
        print(random.choice(articles), random.choice(nouns), random.choice(verbs),
              random.choice(adverbs))
    else:
        print(random.choice(articles), random.choice(nouns), random.choice(verbs))

# /////////////////////////////////////////////////////////////////////////////////////