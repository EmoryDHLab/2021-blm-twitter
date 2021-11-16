import datetime
import pandas as pd
import tsm
import sys

"""
Generate an edgelist from a csv with rows 
cols are index, username, tweet text, datetime 
"""
if __name__ == "__main__":
    # make the edge list
    if len(sys.argv) < 3:
        print("Usage: ")
        print("  python3 <tweet.csv> <output_filename>")
        sys.exit(0)

    edge_list_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    tsm.t2e(edge_list_filename, "ALL_NO_ISOLATES", save_prefix='{}_{}'.format(output_filename, date.today()))