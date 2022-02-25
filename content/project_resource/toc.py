#!/usr/bin/env python
# A program to generate various table of contents for Stephens lab resource
# 2015 by Gao Wang
'''
Usage:
python toc.py data/*.md -o toc-data.md -t "Data Resources"
python toc.py utilities/wiki/*.md -o toc-utils.md -t "Utility Resources"
'''

from collections import OrderedDict
from argparse import ArgumentParser
import re

A_TO_Z = '''
|     |     |     |     |     |     |     |     |     |
|:-:  |:-:  |:-:  |:-:  |:-:  |:-:  |:-:  |:-:  |:-:  |
| [#](#0) 	| [A](#a) 	| [B](#b) 	| [C](#c) 	| [D](#d) 	| [E](#e) 	| [F](#f) 	| [G](#g) 	| [H](#h) 	|
| [I](#i) 	| [J](#j) 	| [K](#k) 	| [L](#l) 	| [M](#m) 	| [N](#n) 	| [O](#o) 	| [P](#p) 	| [Q](#q) 	|
| [R](#r) 	| [S](#s) 	| [T](#t) 	| [U](#u) 	| [V](#v) 	| [W](#w) 	| [X](#x) 	| [Y](#y) 	| [Z](#z)  	|'''

A_TO_Z = '''
This page is automatically generated from individual Markdown files and sorted alphabetically.
You can use the **Search Bar** on the side of the wiki to look for contents of interest.
Please do not edit this page manually.
'''

class Environment:
    def __init__(self):
        self.blob = ''
        self.exclude = []
        self.remove_ext = 0

env = Environment()

def get_toc(files):
    '''Input: a list of *.md files
    Procedure: parse and get the title and description line in each file
    Output: a dictionary of data : [filename, description]'''
    res = {}
    for item in files:
        if item in env.exclude:
            continue
        lines = [x.strip() for x in open(item).readlines() if x.strip()]
        name = lines[0].strip('#').strip()
        res[name] = [item]
        for line in lines[1:]:
            if line.startswith('#'):
                continue
            else:
                # Take the 1st sentence as description
                # 2nd line as author
                res[name].append(line.split('. ')[0])
            if len(res[name]) == 3:
                break
    return OrderedDict(sorted(res.items(), key=lambda i: i[0].lower()))

def write_toc(toc, page, title):
    categories = []
    with open(page, 'w') as f:
        f.write('# {}\n'.format(title))
        f.write(A_TO_Z)
        for name in toc.keys():
            category = '0' if re.match(r"[-+]?\d+$", name[0]) is not None else name[0].upper()
            if category not in categories:
                categories.append(category)
                f.write('\n## {}\n'.format(category))
            desc_text = '. {}\n\t* **{}**'.format(toc[name][1], toc[name][2]) 
            desc_text = desc_text.rstrip('.') + '.'
            link = '{}{}'.format(env.blob, toc[name][0][:-env.remove_ext] if env.remove_ext > 0 else toc[name][0])
            f.write('* [{}]({}){}\n'.format(name, link, desc_text))

def main(args):
    if args.base_url:
        env.blob = args.base_url
    if args.exclude:
        env.exclude = args.exclude
    if not args.output.endswith('.md'):
        args.output = args.output.strip('.') + '.md'
    toc = get_toc(args.files)
    write_toc(toc, args.output, args.title)

if __name__ == '__main__':
    parser = ArgumentParser(description = 'Utility to generate toc for Stephens Lab Data Library',
                            epilog = '''2015 by Gao Wang''' )
    parser.add_argument('files', nargs = '+', help = 'Input files')
    parser.add_argument('-o', '--output', required=True, help = 'Output page name')
    parser.add_argument('-t', '--title', required=True, help = 'Output page title')
    parser.add_argument('-b', '--base_url', help = 'Base URL for pages')
    parser.add_argument('-e', '--exclude', nargs = '+', help = 'Exclude pages')
    main(parser.parse_args())
