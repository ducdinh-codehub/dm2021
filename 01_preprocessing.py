import json
import re
from collections import Counter
import math
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
def process(paragraph):
    paragraph = "".join(word for word in paragraph if word not in ("?", ".", ";", ":", "!",",","(",")")) # Removing all the punctuation
    paragraph = paragraph.lower() # Lowercase
    paragraph = paragraph.strip() # Trim remove unecessary space at the begin and the final 
    paragraph = "".join(filter(lambda x: not x.isdigit(), paragraph))
    re.sub("\s\s+", " ", paragraph) # Removing all unecessary space in the paragraph
    return paragraph

    # Removing all the duplicate word to get the keyword

documents = ["Apparently Prides Osteria had rough summer evidenced by the almost empty dining room at 6:30 on a Friday night. However new blood in the kitchen seems to have revitalized the food from other customers recent visits. Waitstaff was warm but unobtrusive. By 8 pm or so when we left the bar was full and the dining room was much more lively than it had been. Perhaps Beverly residents prefer a later seating. After reading the mixed reviews of late I was a little tentative over our choice but luckily there was nothing to worry about in the food department. We started with the fried dough, burrata and prosciutto which were all lovely. Then although they don't offer half portions of pasta we each ordered the entree size and split them. We chose the tagliatelle bolognese and a four cheese filled pasta in a creamy sauce with bacon, asparagus and grana frita. Both were very good. We split a secondi which was the special Berkshire pork secreto, which was described as a pork skirt steak with garlic potato purée and romanesco broccoli (incorrectly described as a romanesco sauce). Some tables received bread before the meal but for some reason we did not. Management also seems capable for when the tenants in the apartment above began playing basketball she intervened and also comped the tables a dessert. We ordered the apple dumpling with gelato and it was also quite tasty. Portions are not huge which I particularly like because I prefer to order courses. If you are someone who orders just a meal you may leave hungry depending on you appetite. Dining room was mostly younger crowd while the bar was definitely the over 40 set. Would recommend that the naysayers return to see the improvement although I personally don't know the former glory to be able to compare. Easy access to downtown Salem without the crowds on this month of October.",
            "Apparently Osteria had a summer evidenced the almost empty dining room at 6:30 on a Friday night. However new blood in the kitchen seems to have revitalized the food from other customers recent visits. Waitstaff was warm but unobtrusive. By 8 pm or so when we left the bar was full and the dining room was much more lively than it had been. Perhaps Beverly residents prefer a later seating. After reading the mixed reviews of late I was a little tentative over our choice but luckily there was nothing to worry about in the food department. We started with the fried dough, burrata and prosciutto which were all lovely. Then although they don't offer half portions of pasta we each ordered the entree size and split them. We chose the tagliatelle bolognese and a four cheese filled pasta in a creamy sauce with bacon, asparagus and grana frita. Both were very good. We split a secondi which was the special Berkshire pork secreto, which was described as a pork skirt steak with garlic potato purée and romanesco broccoli (incorrectly described as a romanesco sauce). Some tables received bread before the meal but for some reason we did not. Management also seems capable for when the tenants in the apartment above began playing basketball she intervened and also comped the tables a dessert. We ordered the apple dumpling with gelato and it was also quite tasty. Portions are not huge which I particularly like because I prefer to order courses. If you are someone who orders just a meal you may leave hungry depending on you appetite. Dining room was mostly younger crowd while the bar was definitely the over 40 set. Would recommend that the naysayers return to see the improvement although I personally don't know the former glory to be able to compare. Easy access to downtown Salem without the crowds on this month of October.",
            "I heard so many good things about this place so I was pretty juiced to try it. I’m from Cali and I heard Shake Shack is comparable to IN-N-OUT and I gotta say, Shake Shake wins hands down. Surprisingly, the line was short and we waited about 10 MIN. to order. I ordered a regular cheeseburger, fries and a black/white shake. So yummerz. I love the location too! It’s in the middle of the city and the view is breathtaking. Definitely one of my favorite places to eat in NYC. I’m from California and I must say, Shake Shack is better than IN-NOUT, all day, err’day. Would I pay $15+ for a burger here? No. But for the price point they are asking for, this is a definite bang for your buck (though for some,the opportunity cost of waiting in line might outweigh the cost savings)Thankfully, I came in before the lunch swarm descended and I ordered a shake shack (the special burger with the patty + fried cheese & portabella"]

#while(i < len(documents)):
paragraph = documents[0] + documents[1] + documents[2]
paragraph = process(paragraph)
not_duplicate_paragraph = ' '.join(unique_list(paragraph.split())) 
#print(not_duplicate_paragraph)

#Count occurence
#Remove all the meaningless words
keyWord_stream = not_duplicate_paragraph.split(" ")
word_list = []
no_meaning_word = [ 'a',
                    'an',
                    'the',
                    'of',
                    'with',
                    'and',
                    'in',
                    'on',
                    'at',
                    'from',
                    'then',
                    'like',
                    'get',
                    'love',
                    'hate',
                    'smile',
                    'sad',
                    'happy',
                    'angry',
                    'be',
                    'as',
                    'he',
                    'she',
                    'it',
                    'they',
                    'i',
                    'we',
                    'you',
                    'have',
                    'has',
                    'had',
                    'was',
                    'were']
#Calculate TF list
for keyWord in keyWord_stream:
    if(keyWord not in no_meaning_word):
        count_word = paragraph.count(keyWord)
        word_dict = {keyWord:count_word}
        word_list.append(word_dict) 

# D(w) Counting the number of document that contain keyword
DF = []
IDF = []
TF_IDF = []
D = len(documents)
paragraph_contain_word = []
index = 0
for wordDict in word_list:
    for keyWord, value in wordDict.items():
        count = 0
        for paragraph in documents:
            paragraph = process(paragraph)
            if(paragraph.find(keyWord) > -1):
                count += 1
        if(count != 0):
            df = count / D
            idf = math.log(1/df)
            DF.append(df)
            IDF.append(idf)
            TF_IDF.append({keyWord : idf * value})
print(DF)
print(IDF)
print(TF_IDF)
