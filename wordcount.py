from sys import argv

script, filename = argv 

f = open ("inputfile.txt", "r")
wholefile = f.read()

#print wholefile
# split by whitespace
tokens = [] 
for word in wholefile.split():
    word = word.strip(".,?")
    tokens.append(word)

dictionary = {}
for token in tokens:
    if dictionary.get(token): 
        dictionary[token] += 1
    else:
        dictionary[token] = 1

for key, value in dictionary.items():
        print key, value 

#ictionary = {}
#om collections import Counter 
#ictionary = Counter(tokens)
#rint dictionary 
   #dictionary = {i:1} 
   #print dictionary

    #if token != dict.items():
    

    
    

    


# for the first word in our list called tokens, we insert into dictionary and give it value 1
# +=1 then != any key, add key with value 1
#if == an existing key, +1 value of existing key  







