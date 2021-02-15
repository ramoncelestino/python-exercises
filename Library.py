# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

word_title = {}

class Book:

    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description

def gettitle(x):


    words = re.findall(r'\w+', x)
    words = set(words)

    a = x.split("TITLE")
    books = []
    for i in range(len(a)):
        if(len(a[i]) > 0):
            books.append(Book(extract_title(a[i]), extract_author(a[i]), extract_desc(a[i])))


    for w in words:
        for b in books:
            if ((w in b.title) or (w in b.author) or (w in b.description)):
                if w in word_title:
                    word_title[w].append(b.title)
                else: word_title[w] = [b.title]



def search(s):
    return word_title[s]

def extract_author(str):
    return str[str.index("AUTHOR") + 8: str.index("DESCRIPTION")]

def extract_title(str):
    s = str[2: str.index("AUTHOR")]
    return s[:s.index("\n")]

def extract_desc(str):
    return str[str.index("DESCRIPTION") + 12:]

s = """TITLE: Hitchhiker's Guide to the Galaxy\n
    AUTHOR: Douglas Adams\n
    DESCRIPTION: Seconds before the Earth is demolished to make way for a galactic freeway,\n
    Arthur Dent is plucked off the planet by his friend Ford Prefect and a researcher for the\n
    revised edition of The Hitchhiker's Guide to the Galaxy who, for the last fifteen years,\n
    has been posing as an out-of-work actor.\n
    \n
    TITLE: Dune\n 
    AUTHOR: Frank Herbert\n 
    DESCRIPTION: The troubles begin when stewardship of Arrakis is transferred by the\n 
    Emperor from the Harkonnen Noble House to House Atreides. The Harkonnens don't want to\n
    give up their privilege, though, and through sabotage and treachery they cast young\n
    Duke Paul Atreides out into the planet's harsh environment to die. There he falls in\n
    with the Fremen, a tribe of desert dwellers who become the basis of the army with which \n
    he will reclaim what's rightfully his. Paul Atreides, though, is far more than just a\n
    usurped duke. He might be the end product of a very long-term genetic experiment\n
    designed to breed a super human; he might be a messiah. His struggle is at the center\n
    of a nexus of powerful people and events, and the repercussions will be felt throughout\n 
    the Imperium.\n 
    \n 
    TITLE: A Song Of Ice And Fire Series\n 
    AUTHOR: George R.R. Martin\n 
    DESCRIPTION: As the Seven Kingdoms face a generation-long winter, the noble Stark family\n 
    confronts the poisonous plots of the rival Lannisters, the emergence of the\n 
    White Walkers, the arrival of barbarian hordes, and other threats.\n"""

gettitle(s)

print(search("before"))

