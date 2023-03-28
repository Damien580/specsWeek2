from collections import Counter
mylist = [1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]

# print(Counter(mylist))

mylist = ['a','a','a','a',10,10,10,10,10]
# print(Counter(mylist))

# print(Counter('kjhswgerkwfgjnebfkrjgbnvesedfva'))

sentence = "How many times does each word show up in the sentence seeing how many times a word will show up?"
# print(Counter(sentence.split()))

letters = "aaaaabbbbcccccccccccccccdddddddddddddd"

c = Counter(letters)
# print(c)

# print(c.most_common(2))

from collections import defaultdict
d = {'a':10}

d = defaultdict(lambda: 0)
d['correct'] = 100

# print(d['correct'])
# print(d['wrong key'])

from collections import namedtuple
mytuple = (10, 20, 30)

# print(mytuple[0])

Dog = namedtuple('dog', ['age', 'breed', 'name'])
sammy = Dog( age=5, breed='Husky', name='Sam')
# print(type(sammy))
# print(sammy)
# print(sammy.age)

