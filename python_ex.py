import random;
from urllib import urlopen;
import sys;

word_url="http://learncodethehardway.org/words.txt";
WORDS=[];

PHRASES={
    "class %%%(%%%):":
        "make a class named %%% that is_a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)":
        "class %%% has_a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\t def***(self,@@@)":
        "class %%% has_a function named *** that takes self and @@@ parameters.",
    "*** =%%%()":
        "Set *** get the *** function , and call it with paramaters self,@@@",
    "***.***='***'":
        "From *** get the *** attribute and set it to '***' ."
}

PHRASE_FIRST=False;
if len(sys.argv)==2 and sys.argv[1]=="english":
    PHRASE_FIRST=True;

for word in urlopen(word_url).readlines():
    WORDS.append(word.strip());

def convert(snippet,phrase):
    class_names=[w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]
    other_names=random.sample(WORDS,snippet.count("***"));
    results=[];
    param_names=[];


    for i in range(0,snippet.count("@@@")):
        param_count=random.randint(1,3);
        param_names.append(",".join(random.sample(WORDS,param_count)));

    for sentence in snippet,phrase:
        result=sentence[:];

        for word in class_names:
            result=result.replace("%%%",word,1);

        for word in other_names:
            result=result.replace("***",word,1);
        
        for word in param_names:
            result=result.replace("@@@",word,1);

        results.append(result);

    return results;

try :
    while True:
        snipppets=PHRASES.keys();
        random.shuffle(snipppets);

        for snippet in snipppets:
            phrase=PHRASES[snippet]
            question,answer=convert(snippet,phrase);
            if PHRASE_FIRST:
                question,answer=answer,question;

            print question

            raw_input(">")
            print "ANSWER : %s \n\n"%answer;

except EOFError:
    print "\nBYE";
