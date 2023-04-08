import os
import sys
from graphviz import Digraph

requires_dict = {"aaa":[{'require': "'/bin/sh'", 'packages': ['bash-4.2.46-31.el7.x86_64', 'bash-5.0-17.up1.uel20.x86_64']}, {'require': "'/usr/bin/perl'", 'packages': ['perl-5.16.3-299.el7_9.x86_64', 'perl-5.28.3-7.up2.uel20.x86_64']}, {'require': "'/usr/sbin/update-alternatives'", 'packages': ['chkconfig-1.7.4-1.el7.x86_64', 'chkconfig-1.14-1.uel20.x86_64']}, {'require': "'bash'", 'packages': ['bash-4.2.46-31.el7.x86_64', 'bash-5.0-17.up1.uel20.x86_64']}, {'require': "'config(mariadb) = 1:5.5.68-1.el7'", 'packages': ['mariadb-5.5.68-1.el7.x86_64', 'mariadb-10.3.9-12.up1.uel20.x86_64']}, {'require': "'fileutils'", 'packages': ['coreutils-8.22-23.el7.x86_64', 'coreutils-8.32-2.up1.uel20.x86_64']}, {'require': "'grep'", 'packages': ['grep-2.20-3.el7.x86_64', 'grep-3.4-1.uel20.x86_64']}, {'require': "'libc.so.6()(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libc.so.6(GLIBC_2.11)(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libc.so.6(GLIBC_2.14)(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libc.so.6(GLIBC_2.15)(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libc.so.6(GLIBC_2.17)(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libc.so.6(GLIBC_2.2.5)(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libc.so.6(GLIBC_2.3)(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libc.so.6(GLIBC_2.3.4)(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libc.so.6(GLIBC_2.4)(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libcrypto.so.10()(64bit)'", 'packages': ['openssl-libs-1.0.2k-16.el7.x86_64', 'openssl-libs-1.1.1f-13.uel20.x86_64']}, {'require': "'libcrypto.so.10(libcrypto.so.10)(64bit)'", 'packages': ['openssl-libs-1.0.2k-16.el7.x86_64', 'openssl-libs-1.1.1f-13.uel20.x86_64']}, {'require': "'libdl.so.2()(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libdl.so.2(GLIBC_2.2.5)(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libm.so.6()(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libm.so.6(GLIBC_2.2.5)(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libncurses.so.5()(64bit)'", 'packages': ['ncurses-libs-5.9-14.20130511.el7_4.x86_64', 'ncurses-libs-6.2-2.uel20.x86_64']}, {'require': "'libpthread.so.0()(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libpthread.so.0(GLIBC_2.2.5)(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libpthread.so.0(GLIBC_2.3.2)(64bit)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'libssl.so.10()(64bit)'", 'packages': ['openssl-libs-1.0.2k-16.el7.x86_64', 'openssl-libs-1.1.1f-13.uel20.x86_64']}, {'require': "'libssl.so.10(libssl.so.10)(64bit)'", 'packages': ['openssl-libs-1.0.2k-16.el7.x86_64', 'openssl-libs-1.1.1f-13.uel20.x86_64']}, {'require': "'libstdc++.so.6()(64bit)'", 'packages': ['libstdc++-4.8.5-36.el7.x86_64', 'libstdc++-7.3.0-20211123.43.uel20.x86_64']}, {'require': "'libstdc++.so.6(CXXABI_1.3)(64bit)'", 'packages': ['libstdc++-4.8.5-36.el7.x86_64', 'libstdc++-7.3.0-20211123.43.uel20.x86_64']}, {'require': "'libstdc++.so.6(GLIBCXX_3.4)(64bit)'", 'packages': ['libstdc++-4.8.5-36.el7.x86_64', 'libstdc++-7.3.0-20211123.43.uel20.x86_64']}, {'require': "'libtinfo.so.5()(64bit)'", 'packages': ['ncurses-libs-5.9-14.20130511.el7_4.x86_64', 'ncurses-libs-6.2-2.uel20.x86_64']}, {'require': "'libz.so.1()(64bit)'", 'packages': ['zlib-1.2.7-18.el7.x86_64', 'zlib-1.2.11-18.uel20.x86_64']}, {'require': "'mariadb-libs(x86-64) = 1:5.5.68-1.el7'", 'packages': ['mariadb-libs-5.5.68-1.el7.x86_64', '-']}, {'require': "'perl(Exporter)'", 'packages': ['perl-Exporter-5.68-3.el7.noarch', 'perl-Exporter-5.74-1.uel20.noarch']}, {'require': "'perl(Fcntl)'", 'packages': ['perl-5.16.3-299.el7_9.x86_64', 'perl-5.28.3-7.up2.uel20.x86_64']}, {'require': "'perl(File::Temp)'", 'packages': ['perl-File-Temp-0.23.01-3.el7.noarch', 'perl-File-Temp-0.230.900-1.uel20.noarch']}, {'require': "'perl(Getopt::Long)'", 'packages': ['perl-Getopt-Long-2.40-3.el7.noarch', 'perl-Getopt-Long-2.51-1.uel20.noarch']}, {'require': "'perl(IPC::Open3)'", 'packages': ['perl-5.16.3-299.el7_9.x86_64', 'perl-5.28.3-7.up2.uel20.x86_64']}, {'require': "'perl(Sys::Hostname)'", 'packages': ['perl-5.16.3-299.el7_9.x86_64', 'perl-5.28.3-7.up2.uel20.x86_64']}, {'require': "'rtld(GNU_HASH)'", 'packages': ['glibc-2.17-317.uelc20.01.x86_64', 'glibc-2.28-84.up1.uel20.x86_64']}, {'require': "'systemd'", 'packages': ['systemd-219-62.el7.x86_64', 'systemd-243-50.up7.uel20.x86_64']}]}

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
    for i in tree[first_label]:
        _sub_plot(g, i, "0")
    leafs = str(getMaxLeafs(tree) // 10)
    g.attr(rankdir='LR', ranksep=leafs)
    g.render()
 
root = "0"
 
def _sub_plot(g, tree, inc):
    global root
    if isinstance(tree, list):
        for i in tree:
            _sub_plot(g, i, root)
    else:
        lists = tree.keys()
        for i in lists:
            if isinstance(tree[i], dict):
                root = str(int(root) + 1)
                g.node(root, list(tree[i].keys())[0])
                g.edge(inc, root, str(i))
                _sub_plot(g, tree[i], root)
            elif isinstance(tree[i], list):
                count = root
                for string in tree[i]:
                    root = str(int(root) + 1)
                    g.node(root, string)
                    if string == '-':
                        g.edge(count, root, str(i), color='red')
                    else:
                        g.edge(count, root, str(i))
            else:
                root = str(int(root) + 1)
                g.node(root, str(tree[i]))
                g.edge(inc, root, str(i))

def get_json():
    plot_model(requires_dict, "requires")
    with open("./requires.png", "rb") as f:
        byte_data = f.read()
    return byte_data
plot_model(requires_dict, "requires")
