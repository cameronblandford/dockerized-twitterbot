import random
import pronouncing as p
import nltk
import sys

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

def not_quite(inp):
    synset = wn.synsets(inp)[0]
    r = random.choice(p.rhymes(inp))
    print("What's the name for " + synset.definition() + "? Is it " + r + "?" )
    for _ in range(10):
        print("No, that's " + wn.synsets(r)[0].definition())
        r = random.choice(p.rhymes(r))
        while not wn.synsets(r):
            r = random.choice(p.rhymes(r))
        print("You're thinking of " + r + ".")
        print("")

# i love eating twinks
# i think you meant a twinky - a twink is a facial expression where blah blah blah
def not_quite2(inp):

    if not wn.synsets(inp):
        print("This word is undefined!")
        sys.exit(0)
    if not wn.synsets(inp)[0].examples():
        print("This word has no example sentence!")
        sys.exit(0)

    w1plain = inp
    w1 = wn.synsets(inp)[0]

    w2plain = random.choice(p.rhymes(inp))
    while not wn.synsets(w2plain):
        print(w2plain)
        w2plain = random.choice(p.rhymes(inp))
    w2 = wn.synsets(w2plain)[0]

    w3plain = random.choice(p.rhymes(w2plain))
    while not wn.synsets(w3plain):
        print(w3plain)
        w3plain = random.choice(p.rhymes(w2plain))
    w3 = wn.synsets(w3plain)[0]
    # print an example sentence where the word is replaced with a word it rhymes with
    # i think you meant <original_word>. a <rhyming word> is <definition of a word that rhymes with that word>.
    example_sentence = w1.examples()[0]
    example_sentence = example_sentence.replace(inp, w2plain)
    print(example_sentence)

    for _ in range(5):
        if _ == 0:
            print("No, you're thinking of " + w1plain + ". " + w2plain + " means \"" + w3.definition() + "\".")
        else:
            print("No, that's " + w2plain + ". " + w1plain + " means \"" + w3.definition() + "\".")
        w1plain = w2plain
        w1 = w2
        w2plain = w3plain
        w2 = w3
        w3plain = random.choice(p.rhymes(w2plain))
        while not wn.synsets(w3plain):
            w3plain = random.choice(p.rhymes(w2plain))
        w3 = wn.synsets(w3plain)[0]



if __name__ == "__main__":
    # group_name()
    # print(rhyme_name())
    print(not_quite('cry'))
