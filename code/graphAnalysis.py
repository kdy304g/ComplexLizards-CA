# Standard libraries
import time
import sys

# Project modules
import helpers
from view import View
from hexMap import HexMap
from constants import *

# libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import networkx as nx
import random

hexmap = HexMap(width=60, height=60)

all_vals = dict()

def create_hexmap(hexmap, show=False):
    X=nx.Graph()
    node_num = 1
    offset = 0
    colors = []
    for index, row in enumerate(hexmap.array):
        for i, cell in enumerate(row):
            if cell.state == GREEN_STATE:
                colors.append('green')
            elif cell.state == BLACK_STATE:
                colors.append('black')
            elif cell.state == BROWN_STATE:
                colors.append('brown')
            else:
                colors.append('gray')
            cell.node_num = node_num
            X.add_node(node_num, pos=(10*i+offset, 25-index))
            node_num += 1
        offset += 5
    pos = nx.get_node_attributes(X,'pos')

    for row in hexmap.array:
        for cell in row:
            cell.observe_neighbors()
            for neighbor in cell.neighbors:
                if cell.state == neighbor.state:
                    X.add_edge(cell.node_num, neighbor.node_num)
    if show:
        nx.draw(X,pos, node_size=50, node_color=colors)
        plt.show()
    return X

def convert_graph_draw(hexmap, steps=0, show=False):
    all_data = []
    for i in range(steps):
        if (i % 10) == 0:
            all_data.append(get_data(create_hexmap(hexmap)))
        hexmap.step()
    all_data.append(get_data(create_hexmap(hexmap)))
    for x in all_data:
        print(np.amin(x))
    fig, ax = plt.subplots()
    plt.yscale('log')
    ax.boxplot(all_data)
    plt.show()
    X = create_hexmap(hexmap, True)
    return X

def get_data(G):
    num_nodes = np.array([])
    for i in sorted(nx.connected_components(G), key=len, reverse=True):
        num_nodes = np.append(num_nodes, len(i))
    return num_nodes

def get_pmf_data(num_nodes):
    val, cnt = np.unique(num_nodes, return_counts=True)
    pmf = cnt / len(num_nodes)
    X = np.column_stack((val, pmf))
    return X

def plot_graph_pmf(G):
    X = get_pmf_data(get_data(G))
    plt.bar(x=X[:, 0], height=X[:, 1])
    plt.show()


G = convert_graph_draw(hexmap, steps=150, show=True)
plot_graph_pmf(G)
