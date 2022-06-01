import community as community_louvain
import csv
import networkx as nx
import main
#main.doStuff("seed.csv", "blm_edgelist_random_sample.csv", "april_20_sample.csv")

#main.convert_to_community("seed.csv", "alex_fullsize/lexsem_all_no_isolates_edgelist.csv", "alex_fullsize/alex_edgelist_python_community.csv")



#list1 = (main.find_in_community("alex_fullsize/alex_edgelist_python_community.csv", 'anonyops'))
#list2 = (main.find_in_community("alex_fullsize/lexsem_all_no_isolates_communities.csv", "anonyops"))
#print(len(list1) * 1.0 / len(list2) * 1.0)
#list2 = (main.find_in_community("alex_fullsize/lexsem_all_no_isolates_communities.csv", 'deray'))
print(main.get_similarity("alex_fullsize/alex_edgelist_python_community.csv", "alex_fullsize/lexsem_all_no_isolates_communities.csv", "larryelder"))
#print("april_20 + alex: " + str(main.getSimilarity("blm_edgelist_random_sample.csv","alex_fullsize/lexsem_all_no_isolates_communities.csv","common")))
#print("alexpython + alex: " + str(main.getSimilarity("alex_output.csv", "alex_fullsize/lexsem_all_no_isolates_communities.csv", "kanyewest")))

#main.doStuff("seed.csv", "lexsem_all_no_isolates_edgelist.csv")

