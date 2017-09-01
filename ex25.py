def break_words(suffs):
    #this function will split the string provided and by the space delemeter
    #split on string returns a List
    words = suffs.split(' ')
    return words

def sort_word(words):
    #it will sort the string or list provided
    return sorted(words)

def print_first_world(words):
    #It takes a list and return first element of the lsit
     return words.pop(0)

def print_last_world(words):
    #it takes a list and return the last element of the list
    return words.pop(-1)

def sort_sentence(sentence):
    #it takes a full sentence and return the sorted words of the string
    words = beeak_words(sentence)
    return sort_word(words)

def print_first_and_last(sentence):
    """prints the first and last words of the sentence"""
    words = break_words(sentence)
    print_first_world(words)
    print_last_world(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_world(words)
    print_last_world(words)
