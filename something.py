######IDEA GENERATOR#######
import os, random

def getList(file):
    getList.list = []
    with open(file, 'r') as f:
        for line in f:
            getList.list.append(line)

def idea(verb, noun, adverb, thing):
    randomVerb = random.randint(0, len(verb))
    randomNoun = random.randint(0, len(noun))
    randomAdverb = random.randint(0, len(adverb))
    randomThing = random.randint(0, len(thing))

    print(adverb[randomAdverb] + ' will make a ' + noun[randomNoun] + ' that is ' + verb[randomVerb] + ' ' + thing[randomThing])






while True:
    getList('Grammer/adverbs.txt')
    adverb = getList.list
    getList('Grammer/verbs.txt')
    verb = getList.list
    getList('Grammer/nouns.txt')
    noun = getList.list
    getList('Grammer/things.txt')
    thing = getList.list
    idea(adverb, verb, noun, thing)
    break