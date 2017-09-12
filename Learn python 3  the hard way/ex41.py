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
    #print("class_names: ",class_names)
    other_names = random.sample(WORDS,snippet.count("***"))
    #print("other_names: ",other_names)

    results = []
    param_names = []

    for i in range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS,param_count)))

    for sentence in snippet,phrase:
        print(type(sentence))
        result = sentence[:]
        print(result)
        for word in class_names:
            result = result.replace("%%%",word,1)

        for word in other_names:
            result = result.replace("***",word,1)

        for word in param_names:
            result = result.replace("@@@",word,1)

        results.append(result)

    return results

try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
#            #question,answer = c
            question,answer = convert(snippet,phrase)
#            convert(snippet,phrase)
            if PHRASES_FIRST:
               question,answer = answer,question

            print(question)
            input("> ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    Print('\nBYE#')
