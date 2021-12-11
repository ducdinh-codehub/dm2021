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
    if(index == 5000):
        break
    paragraphs.append(json.loads(line)['text'])

#Cleaning data
paragraphs_after_cleaning = process(paragraphs)
i = 0
while i < len(paragraphs_after_cleaning):
    length_of_review = len(paragraphs_after_cleaning[i].split(' '))
    x.append(length_of_review)
    i+=1

x_max = max(x)
x_min = min(x)

#Calculate mean
i = 0
total = 0
for i in range(0, len(x)):
    total += x[i]
mean = total/len(x)

#Calculate standard deviation
deviation = [(val-mean)**2 for val in x]
variance = sum(deviation) / len(x)
std = math.sqrt(variance)

#Calculate ditribution value
PDF = []

for i in range(x_min, x_max):
    pdf = (1/(std*math.sqrt(2*math.pi))) * math.exp(-0.5*(((i-mean)/std)**2))
    PDF.append(pdf)

normax = max(PDF)
PDF = [normax * (700/ normax) for normax in PDF]
plt.plot(range(x_min, x_max), PDF)
n, bins, _ = plt.hist(x)
plt.show()


