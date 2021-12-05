import json
import re
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist
'''
f = open('../yelp_academic_dataset_review.json')

data = json.load(f)

for text in data['text']:
    print(text)
    break

f.close()
'''
number_of_loop = 1
count = 0
paragraph = "Apparently Prides Osteria had a rough summer as evidenced by the almost empty dining room at 6:30 on a Friday night. However new blood in the kitchen seems to have revitalized the food from other customers recent visits. Waitstaff was warm but unobtrusive. By 8 pm or so when we left the bar was full and the dining room was much more lively than it had been. Perhaps Beverly residents prefer a later seating. After reading the mixed reviews of late I was a little tentative over our choice but luckily there was nothing to worry about in the food department. We started with the fried dough, burrata and prosciutto which were all lovely. Then although they don't offer half portions of pasta we each ordered the entree size and split them. We chose the tagliatelle bolognese and a four cheese filled pasta in a creamy sauce with bacon, asparagus and grana frita. Both were very good. We split a secondi which was the special Berkshire pork secreto, which was described as a pork skirt steak with garlic potato purée and romanesco broccoli (incorrectly described as a romanesco sauce). Some tables received bread before the meal but for some reason we did not. Management also seems capable for when the tenants in the apartment above began playing basketball she intervened and also comped the tables a dessert. We ordered the apple dumpling with gelato and it was also quite tasty. Portions are not huge which I particularly like because I prefer to order courses. If you are someone who orders just a meal you may leave hungry depending on you appetite. Dining room was mostly younger crowd while the bar was definitely the over 40 set. Would recommend that the naysayers return to see the improvement although I personally don't know the former glory to be able to compare. Easy access to downtown Salem without the crowds on this month of October."
paragraph = "".join(word for word in paragraph if word not in ("?", ".", ";", ":", "!",",")) # Removing all the punctuation
paragraph = paragraph.lower() # Lowercase
paragraph = paragraph.strip() # Trim remove unecessary space at the begin and the final
not_duplicate_paragraph = ' '.join(unique_list(paragraph.split())) # Removing all the duplicate word to get the keyword
re.sub("\s\s+", " ", paragraph) # Removing all unecessary space in the paragraph

keyWord_stream = not_duplicate_paragraph.split(" ")
word_list = []
for keyWord in keyWord_stream:
    #print(keyWord)
    count_word = paragraph.count(keyWord);
    word_dict = {keyWord:count_word}
    word_list.append(word_dict) 

print(word_list)