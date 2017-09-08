import random
from urllib.request import urlopen
import sys

##URL
WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS=[]

##Map having Key value pair
PHRASES = {
    "class %%%(%%%):":"Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self,***)":"class %%% has-a init that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self,@@@)":"class %%% has-a function *** that taked self and @@@ params.",
    "*** = %%%()":"Set *** to a instance of class %%%.",
    "***.***(@@@)":"From *** get the *** function,and call it with param self and @@@.",
    "***.***  = \'***\'":"From *** get the *** attribute and set it to \'***\'."
}

#do you want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

##Load up the word from website
for word in urlopen(WORD_URL).readlines():
    #print(word)
    WORDS.append(str(word.strip(),encoding = 'utf-8'))

def convert(snippet,phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]
    print("class_names: ",class_names)
    other_names = random.sample(WORDS,snippet.count("***"))
    print("other_names: ",other_names)
i = 1
try:
    while i==1:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
        i+=1

        for snippet in snippets:
            phrase = PHRASES[snippet]
#            #question,answer = c
            convert(snippet,phrase)
#            convert(snippet,phrase)
            if PHRASES_FIRST:
#                question,answer = answer,question
               print(snippet)
               input("> ")
               print(f"ANSWER: {phrase}\n\n")
except EOFError:
    Print('\nBYE#')
