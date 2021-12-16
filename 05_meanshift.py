import json
import re
import numpy as np
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



class Point:
    def __init__(self, x) -> None:
        self.x = x

    def dist(self, anotherPoint):
        return abs(self.x - anotherPoint.x)

class Cluster:
    def __init__(self, distPolicy = min):
        self.points = []
        self.distPolicy = min

    def addPoint(self, p):
        self.points.append(p)

    def __repr__(self):
        return f"[{[p.x for p in self.points]}]"

wc = []
paragraphs = []
for index, line in enumerate(open(json_file_path, 'r')):
    if(index == 100):
        break
    paragraphs.append(json.loads(line)['text'])

#Cleaning data
paragraphs_after_cleaning = process(paragraphs)
i = 0
while i < len(paragraphs_after_cleaning):
    length_of_review = len(paragraphs_after_cleaning[i].split(' '))
    wc.append(length_of_review)
    i+=1

MODE = np.zeros((1000,1000))
BW = 4
def flatKernel(input):
    if input <= BW:
        return 1
    else:
        return 0
def shiftMode(mode, wc):
    numerator = 0
    denominator = 0
    for j in range(0, len(wc)):
         numerator += wc[j] * flatKernel(wc[j] - mode)
         denominator += flatKernel(wc[j] - mode)
    result = numerator / denominator
    return result

clusters_mass = set()
clusters = []
for i in range(0, len(wc)):
    k = 0
    MODE[i][k] = wc[i]
    while True:
        print("i: ", i)
        print("k: ", k)
        MODE[i][k+1] = shiftMode(MODE[i][k], wc)
        k += 1
        print("abs(MODE[i][k] - MODE[i][k-1]): ", abs(MODE[i][k] - MODE[i][k-1]))
        if abs(MODE[i][k] - MODE[i][k-1]) < BW:
            break
    MODE[i][0] = MODE[i][k]

    #clusters_mass.add(MODE[i][0])
    #list_key = list(clusters.keys())

    clusters.append({MODE[i][0]: wc[i]})
    
    #if(len(list_key) == 0 or MODE[i][0] not in list_key):
    #    clusters = {MODE[i][0]: []}
    #if(len(list_key) != 0 and MODE[i][0] in list_key):
    #    clusters[MODE[i][0]].append(wc[i])

key_list = set()
for i in range(0, len(clusters)):
    key_list.add(list(clusters[i].keys())[0])

clusters_dict = {key: [] for key in key_list}
CLUSTERS = [Cluster() for i in range(0, len(key_list))]

for i in range(0,len(clusters)):
    if list(clusters[i].keys())[0] in list(clusters_dict.keys()):
        clusters_dict[list(clusters[i].keys())[0]].append(list(clusters[i].values())[0])

number_of_cluster = 0
for values in clusters_dict.values():
    for val in values:
        CLUSTERS[number_of_cluster].addPoint(Point(val))
    number_of_cluster += 1

print(CLUSTERS)






