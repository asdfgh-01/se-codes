#thesauraus app 9574
import random
thesauraus = {'hot':['balmy','summery','scorching'],
             'cold':['chilly','cool','freezing'],
             'happy':['content','cherry','jovial'],
             'sad':['unhappy','glum','melancholy']}
print("Welcome to Thesauraus App")
print("the words in my thesauraus are :",thesauraus.keys())
word = input("what word would you like a synonym for :").lower()
i = random.randint(0,2)
if word in thesauraus:
    syn = thesauraus[word][i]
    print(syn)
else:
    print("sorry your word is not in my thesauraus")
ans = input("would you like to see my thesauraus?(y/n)")
if ans=='y':
    print(thesauraus)
else:
    print("thank you for using my thesauraus!\ngoodbye!")