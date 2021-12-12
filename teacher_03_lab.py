
import json
import re
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

def getDist(d):
    return d['dist']
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

    def dist(self, anotherCluster):
        d = 0
        if self.distPolicy == min:
            d = float('inf')
        else:
            d = -1
        for p1 in self.points:
            for p2 in anotherCluster.points:
                d = self.distPolicy(d, p1.dist(p2))
        return d

    def merge(self, anotherCluster):
        """
            Merge myself with another cluster, This should add all points
            from the other cluster to me. 
            The caller should delete the other cluster
        """
        self.points += anotherCluster.points
        anotherCluster.points = []
    
    def __repr__(self):
        return f"[{[p.x for p in self.points]}]"

clusters = []

wc = []

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
    wc.append(length_of_review)
    i+=1


for dataPoint in wc:
    c = Cluster()
    c.addPoint(Point(dataPoint))
    clusters.append(c)


idx = 0
while True:
    # find the smallest distance between cluster
    distances = []
    for c1 in clusters:
        for c2 in clusters:
            if c1 != c2:
                dist = c1.dist(c2)
                distances.append(
                    {
                        "c1": c1,
                        "c2": c2,
                        "dist": dist
                    }
                )
    
    # Find the smallest distance
    minDict = min(distances, key = getDist)

    # Merge c1 and c2
    minDict['c1'].merge(minDict['c2'])
    clusters.remove(minDict['c2'])
    idx = idx + 1
    print(f"Iteration {idx} {clusters}")
    if len(clusters) == 1:
        print("Only one cluster left. Stop")
        break

    
