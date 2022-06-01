import community as community_louvain
import csv
import networkx as nx
import os

def convert_to_community(seedpath, edgelistpath, filepath):
     #filenames needed
    seedy = seedpath
    edgelist = edgelistpath

     #imports and creates seed
    newSeeds = dict()
    with open(seedy) as toDict:
        totoDict = csv.reader(toDict)
        for row in totoDict:
            newSeeds[row[0]] = row[1]

    convertToGraph = []
    p1 = 7
    with open(edgelist) as toFinish:
        totoFinish = csv.reader(toFinish)
        for row in totoFinish:
            convertToGraph.append(row[0] + " " + row[1])
            if(newSeeds.get(row[0]) == None):
                newSeeds[row[0]] = p1
                p1 = p1 + 1
            if(newSeeds.get(row[1]) == None):
                newSeeds[row[1]] = p1
                p1 = p1 + 1
    #print("reach")
    G = nx.read_edgelist(convertToGraph)

    # compute the best partition
    partition = community_louvain.best_partition(G, partition = newSeeds)

    print("Louvain communities generated -- total modularity of: " + str(community_louvain.modularity(partition,G)) + ".")

    output = [[]]
    index = 0
    for key, value in partition.items():
        output.append([key, value])
        index += 1
    with open(filepath, "w") as f:
        writer = csv.writer(f)
        writer.writerows(output)


def find_in_community(path, community, i = 1):
    listy = []
    commId = -1
    toRead = open(path, "r")
    totoRead = csv.reader(toRead)


    toParse = list(totoRead)
    for row in toParse:
        if (row[0] == community):
            commId = row[i]

    for row in toParse:
        if (row[i] == commId):
            listy.append(row[0])
    print(commId)
    return(listy)
    toRead.close()


def get_similarity(path1, path2, community):
    list1 = dict();
    with open(path1, "r") as toRead:
        totoRead = csv.reader(toRead)
        for row in totoRead:
            list1[row[0]] = row[1]

    list2 = dict()
    with open(path2, "r") as toReadHer:
        totoReadHer = csv.reader(toReadHer)
        for row2 in totoReadHer:
            list2[row2[0]] = row2[1]

    vennDi = dict()
    list2key = list2.get(community)
    for key, value in list2.items():
        if value == list2key:
            vennDi[key] = 1

    list1key = list1.get(community)
    for key, value in list1.items():
        if value == list1key:
            if vennDi.get(key, -1) != -1:
                vennDi[key] = 2
            else:
                vennDi[key] = 1
    similarity = (1.0 * len(vennDi)) / (1.0 * len(list2))
    return similarity



def get_common_elements(list1, list2):
    commonList = dict();
    for row in list1:
        commonList[row] = 0
    for row in list2:
        if(commonList.get(row, -1) == 0):
            commonList[row] = 1
    to_put_out = []
    for key, value in commonList.items():
        if(value == 1):
            to_put_out.append(key)
    return to_put_out


