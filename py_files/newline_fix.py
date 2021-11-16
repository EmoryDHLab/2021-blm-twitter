import pandas as pd
"""
Script if needed to flush any newlines
"""
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ")
        print("  python3 <tweet.csv> <output_filename>")
        sys.exit(0)
    
    tweet_filename = sys.argv[1]
    output_filename = sys.argv[2]
    test = pd.read_csv(tweet_filename)

    # removes any white spaces or tabs that
    test = test.replace({r'\s+$': '', r'^\s+': ''}, regex=True).replace(r'\n',  ' ', regex=True)
    test.to_csv(output_filename, header = False, index = False))
