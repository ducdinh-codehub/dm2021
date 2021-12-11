import matplotlib.pyplot as plt
import numpy as np
import math
import re
import json
import scipy.stats as stats
import matplotlib.mlab as mlab
from scipy.stats import norm
json_file_path = '../yelp_academic_dataset_review.json'

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

x = []
paragraphs = []
for index, line in enumerate(open(json_file_path, 'r')):
    if(index == 10):
        break
    paragraphs.append(json.loads(line)['text'])

#Cleaning data
paragraphs_after_cleaning = process(paragraphs)
i = 0
while i < len(paragraphs_after_cleaning):
    length_of_review = len(paragraphs_after_cleaning[i].split(' '))
    x.append(length_of_review)
    i+=1


# Creating a proximity matrix
proximity_list = []
for i in range(0, len(x)):
    row = []
    for j in range(0, len(x)):
        if x[j] > x[i]:
            row.append(x[j] - x[i])
        else:
            row.append(x[i] - x[j])
    proximity_list.append(row)
print(proximity_list)

# Finding the smallest distance
for i in range(0, len(proximity_list)):
    min_index = 0
    min = proximity_list[i][0]
    j = 0
    while j < len(proximity_list[i]):
        if(j >= len(proximity_list[i])):
            break
        if(min != 0 and proximity_list[i][j] != 0):
            if(min > proximity_list[i][j]):
                min = proximity_list[i][j]
                min_index = j
        else:
            j += 1
            if(j >= len(proximity_list[i])):
                break
            min = proximity_list[i][j]
            min_index = j
        j += 1

proximity_list.pop(0)


print(len(proximity_list))