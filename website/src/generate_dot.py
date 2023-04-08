import os
import sys
from graphviz import Digraph

requires_dict = {"aaa":{"'/bin/sh'": ['bash-5.1.4-1.uelc20.x86_64', 'bash-5.0-17.up1.uel20.x86_64'], "'/usr/bin/perl'": ['perl-interpreter-5.26.3-419.uelc20.04.x86_64', 'perl-5.28.3-7.up2.uel20.x86_64'], "'bash'": ['bash-5.1.4-1.uelc20.x86_64', 'bash-5.0-17.up1.uel20.x86_64'], "'config(mariadb) = 3:10.3.35-1.0.1.module+uelc20+878+ca5ba4de.01'": ['mariadb-10.3.35-1.0.1.module+uelc20+878+ca5ba4de.01.x86_64', 'mariadb-10.3.9-12.up1.uel20.x86_64'], "'coreutils'": ['coreutils-8.30-9.uelc20.03.x86_64', 'coreutils-8.32-2.up1.uel20.x86_64'], "'grep'": ['grep-3.1-8.uelc20.1.x86_64', 'grep-3.4-1.uel20.x86_64'], "'libc.so.6()(64bit)'": ['glibc-2.28-151.uelc20.03.x86_64', 'glibc-2.28-84.up1.uel20.x86_64'], "'libc.so.6(GLIBC_2.11)(64bit)'": ['glibc-2.28-151.uelc20.03.x86_64', 'glibc-2.28-84.up1.uel20.x86_64'], "'libc.so.6(GLIBC_2.14)(64bit)'": ['glibc-2.28-151.uelc20.03.x86_64', 'glibc-2.28-84.up1.uel20.x86_64'], "'libc.so.6(GLIBC_2.15)(64bit)'": ['glibc-2.28-151.uelc20.03.x86_64', 'glibc-2.28-84.up1.uel20.x86_64'], "'libc.so.6(GLIBC_2.17)(64bit)'": ['glibc-2.28-151.uelc20.03.x86_64', 'glibc-2.28-84.up1.uel20.x86_64'], "'libc.so.6(GLIBC_2.2.5)(64bit)'": ['glibc-2.28-151.uelc20.03.x86_64', 'glibc-2.28-84.up1.uel20.x86_64'], "'libc.so.6(GLIBC_2.28)(64bit)'": ['glibc-2.28-151.uelc20.03.x86_64', 'glibc-2.28-84.up1.uel20.x86_64'], "'libc.so.6(GLIBC_2.3)(64bit)'": ['glibc-2.28-151.uelc20.03.x86_64', 'glibc-2.28-84.up1.uel20.x86_64'], "'libc.so.6(GLIBC_2.3.4)(64bit)'": ['glibc-2.28-151.uelc20.03.x86_64', 'glibc-2.28-84.up1.uel20.x86_64'], "'libc.so.6(GLIBC_2.4)(64bit)'": ['glibc-2.28-151.uelc20.03.x86_64', 'glibc-2.28-84.up1.uel20.x86_64'], "'libc.so.6(GLIBC_2.7)(64bit)'": ['glibc-2.28-151.uelc20.03.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}}

def getMaxLeafs(myTree):
    numLeaf = len(myTree.keys())
    for key, value in myTree.items():
        if isinstance(value, dict):
            sum_numLeaf = getMaxLeafs(value)
            if sum_numLeaf > numLeaf:
                numLeaf = sum_numLeaf
    return numLeaf
 
def plot_model(tree, name):
    g = Digraph("G", filename=name, format='png', strict=False)
    first_label = list(tree.keys())[0]
    g.node("0", first_label)
    _sub_plot(g, tree, "0")
    leafs = str(getMaxLeafs(tree) // 10)
    g.attr(rankdir='LR', ranksep=leafs)
    #g.view()
    g.render()
 
root = "0"
 
 
def _sub_plot(g, tree, inc):
    global root
 
    first_label = list(tree.keys())[0]
    root = str(int(root) + 1)
    g.node(root, str(first_label))
    g.edge(inc, root)
    
    ts = tree[first_label]
    for i in ts.keys():
        print(i)
        if isinstance(tree[first_label][i], dict):
            root = str(int(root) + 1)
            g.node(root, list(tree[first_label][i].keys())[0])
            g.edge(inc, root, str(i))
            _sub_plot(g, tree[first_label][i], root)
        elif isinstance(tree[first_label][i], list):
            #count = str(int(root) + 1)
            root = str(int(root) + 1)
            g.node(root, str(i))
            g.edge(inc, root, "requires")
            count = root
            for string in tree[first_label][i]:
                root = str(int(root) + 1)
                g.node(root, string, style="filled", shape="polygon")
                g.edge(count, root)
                #count = str(int(count) + 1)
        else:
            root = str(int(root) + 1)
            #print(type(tree[first_label][i]), tree[first_label][i])
            #for string in tree[first_label][i]:
            g.node(root, str(tree[first_label][i]))
            g.edge(inc, root, str(i))

plot_model(requires_dict, "requires")
