from collections import defaultdict
import pandas as pd
import os

def get_graph_from_data_source():
    print(os.getcwd())  # Prints the current working directory
    df = pd.read_csv("data/data.csv")
    # build a relationship then:

    graph = df.to_dict()

    print(graph)

def main():
    get_graph_from_data_source()

if __name__ == "__main__":
    main()