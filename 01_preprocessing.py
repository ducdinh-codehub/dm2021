import json
import re
import math
from operator import itemgetter
def unique_list(paragraph):
    ulist = []
    [ulist.append(x) for x in paragraph if x not in ulist]
    return ulist

def process(paragraphs):
    i = 0
    len_paragraphs_array = len(paragraphs)
    while(i < len_paragraphs_array):
        if (i >= len_paragraphs_array):
            break
        paragraphs[i] = "".join(word for word in paragraphs[i] if word not in ("?", ".", ";", ":", "!",",","(",")","\'","\"","\n","\\","/","+","-","*")) # Removing all the punctuation
        paragraphs[i] = paragraphs[i].lower() # Lowercase
        paragraphs[i] = paragraphs[i].strip() # Trim remove unecessary space at the begin and the final 
        paragraphs[i] = re.sub(r'\d+', '',paragraphs[i])
        paragraphs[i] = re.sub(r"\s\s+", ' ', paragraphs[i]) # Removing all unecessary space in the paragraph
        i+=1
    return paragraphs

json_file_path = './samples.json'
paragraphs = []

for index, line in enumerate(open(json_file_path, 'r')):
    #if(index == 10):
    #    break
    paragraphs.append(json.loads(line)['text'])

# Cleaning data remove punctuation, special character, standarlized etc etc ....    
paragraphs_after_cleaning = []
paragraphs_after_cleaning = process(paragraphs)
D = len(paragraphs_after_cleaning)
# Word counter
'''
    * Finding the list of non duplicate word in each paragraph
    * Getting all the non duplicate word and storing it inside one list
    * Using the non duplicate keyword list to count the occurence number of each word
'''
not_duplicate_paragraphs = [] # array contains non duplicate words
i = 0

while i < D:
    if(i >= D):
        break
    not_duplicate_paragraphs.append(' '.join(unique_list(paragraphs_after_cleaning[i].split())))
    i+=1

key_word_to_count = [] # Storage all the non duplicate key words in each paragraph
i = 0
while i < D:
    if(i >= D):
        break
    key_word_to_count.append(not_duplicate_paragraphs[i].split(' '))
    i+=1

count_occurence_result = [] # Storing all the occurence time of each word in each paragraph
i = 0
while i < D:
    if(i >= D):
        break
    j = 0
    count_occurence_result_each_paragraph = []
    d = len(key_word_to_count[i])
    while j < d:
        if(j >= d):
            break
        count_occurence_result_each_paragraph.append({key_word_to_count[i][j] : paragraphs_after_cleaning[i].count(key_word_to_count[i][j])})
        j+=1
    count_occurence_result.append(count_occurence_result_each_paragraph)
    i+=1
# Removing stop words
stop_word_list_path = open('./stop_word.txt','r')
stop_word_list = stop_word_list_path.read().split('\n')
i = 0
_d = len(stop_word_list)
while i < _d:
    if(i >= _d):
        break
    j = 0
    len_occurence_list = len(count_occurence_result)
    while j < len_occurence_list:
        if(j >= len_occurence_list):
            break
        k = 0
        len_each_occurence_list = len(count_occurence_result[j])
        while(k < len_each_occurence_list):
            if(k >= len_each_occurence_list):
                break
            key = list(count_occurence_result[j][k].keys())[0]
            if(key == stop_word_list[i]):
                count_occurence_result[j].pop(k)
                break
            k+=1
        j+=1
    i+=1
# Removing common words
stop_word_list_path = open('./common_word.txt','r')
stop_word_list = stop_word_list_path.read().split('\n')
i = 0
_d = len(stop_word_list)
while i < _d:
    if(i >= _d):
        break
    j = 0
    len_occurence_list = len(count_occurence_result)
    while j < len_occurence_list:
        if(j >= len_occurence_list):
            break
        k = 0
        len_each_occurence_list = len(count_occurence_result[j])
        while(k < len_each_occurence_list):
            if(k >= len_each_occurence_list):
                break
            key = list(count_occurence_result[j][k].keys())[0]
            if(key == stop_word_list[i]):
                count_occurence_result[j].pop(k)
                break
            k+=1
        j+=1
    i+=1
# Calculate TF_IDF
DF = []
IDF = []
TF_IDF = []
i = 0
while i < D:
    if(i >= D):
        break
    j = 0
    d = len(count_occurence_result[i])
    df = []
    idf = []
    tf_idf = []
    while j < d:
        if(j >= d):
            break
        k = 0
        occurence_time_in_paragraph = 1
        while k < D:
            if(k != i):
                if(k >= D):
                    break
                h = 0
                _d2 = len(count_occurence_result[k])
                while h < _d2:
                    if(h >= _d2):
                        break
                    key1 = list(count_occurence_result[i][j].keys())[0]
                    key2 = list(count_occurence_result[k][h].keys())[0]
                    if(key1 == key2):
                        occurence_time_in_paragraph += 1
                        break
                    h+=1
            k+=1 
        df.append(occurence_time_in_paragraph/D)
        idf.append(math.log(1 / (occurence_time_in_paragraph/D)))    
        tf_idf.append({'key_word' : key1, 'tf_idf' : list(count_occurence_result[i][j].values())[0] * math.log(1 / (occurence_time_in_paragraph/D)), 'occurence_time' : list(count_occurence_result[i][j].values())[0]})    
        j+=1
    DF.append(df)
    IDF.append(idf)
    TF_IDF.append(tf_idf)
    i+=1

# Sorted
i = 0
newlist = []
while i < D:
    if(i >= D):
        break
    newlist.append(sorted(TF_IDF[i], key=itemgetter('tf_idf'), reverse=True))
    i+=1

""" print(len(count_occurence_result[2]))
print(len(DF[2]))
print(len(IDF[2]))
print(len(newlist[2])) """
FINAL_RESULT = []
i = 0
while i < D:
    if(i >= D):
        break
    j = 0
    d = len(newlist[i])
    final_result = []
    while j < d:
        if(j >= d):
            break
        key_word = newlist[i][j].get('key_word')
        occurence_time = newlist[i][j].get('occurence_time')
        final_result.append(str(key_word + ": " + str(occurence_time)))
        j+=1
    FINAL_RESULT.append(final_result)
    i+=1
print(FINAL_RESULT[0])


