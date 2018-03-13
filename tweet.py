import random
import pronouncing as p
import nltk


nltk.download('wordnet')
from nltk.corpus import wordnet as wn


def all_synonyms(inp):
    synsets = wn.synsets(inp)
    # combine hypernyms and hyponyms
    flat_list = []
    for synset in synsets:
        for hyper in synset.hypernyms():
            flat_list.append(hyper.lemmas()[0].name())
        for hypo in synset.hyponyms():
            flat_list.append(hypo.lemmas()[0].name())

    # remove instances containing input word
    flat_list = [i.replace("_", " ") for i in flat_list if inp not in i]
    return flat_list

def synonym(inp):
    syns = all_synonyms(inp)
    return random.choice(syns) if syns else None


def group_name():
    with open("./nouns.txt") as f:
        nouns = f.readlines()
        n1 = random.choice(nouns).strip()
        if n1[-1] in ["s", "x"] or n1[-2:] in ["sh", "ss", "ch", "zz"]:
            n1 = n1 + "es"
        elif n1[-1] in ["y"] and n1[-2] not in ["a", "e", "i", "o", "u"]:
            n1 = n1[0:-1] + "es"
        else:
            n1 = n1 + "s"
        n2 = random.choice(nouns).strip()
        if n2[0] in ["a", "e", "i", "o", "u"]:
            n2 = "an " + n2
        else:
            n2 = "a " + n2
        print("A group of {} is called {}.".format(n1, n2))

def rhyme_name():
    with open("./nouns.txt") as f:
        nouns = f.readlines()
        rhymes = []
        rsyn = ""
        nsyn = ""
        r = ""
        brk = False
        while (not rhymes or not rsyn) and not brk:
            n = random.choice(nouns).strip()
            rhymes = p.rhymes(n)
            if not rhymes:
                print("no rhymes for " + n + " :(")
                continue
            if not all_synonyms(n):
                print("no synonyms for " + n + " D:")
                continue
            nsyn = synonym(n)
            for rhyme in rhymes:  # for each rhyme
                if all_synonyms(rhyme):  # if it has a synonym, yay! break loop
                    r = rhyme
                    rsyn = synonym(rhyme)
                    brk = True
                    break
            if not brk:
                print("no synonyms for the rhyme: " + r + " :'(")

        # return "broke: " + n + ". woke: " + r
        print(rsyn)
        print(nsyn)
        return "broke: " + rsyn + " " + nsyn + ". woke: " + r + " " + n

if __name__ == "__main__":
    # group_name()
    print(rhyme_name())
    # print(synonym('rabbit'))