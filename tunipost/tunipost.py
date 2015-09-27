#!/usr/bin/env python
#walid.saad

import csv
import re
import argparse
from termcolor import colored
import os

class tunipost(object):


    def __init__(self):
        self.data=os.path.join(os.path.dirname(__file__),'codes.csv')
    def code(self,location):
        results=[]
        with open(self.data) as f:
            reader = csv.reader(f)
            for row in reader:
                match = re.search(location, row[2].lower())
                if match:
                    results.append(row)
        return results

    def location(self,code):
        results=[]
        with open(self.data) as f:
            reader = csv.reader(f)
            for row in reader:
                match = re.search(code, row[3].lower())
                if match:
                    results.append(row)
        return results
    def all(self):
        results=[]
        with open(self.data) as f:
            reader = csv.reader(f)
            for row in reader:
                    results.append(row)
        return results
    def display(self,results):
        for result in results:
            wilaya=colored(result[0],'red')
            motamadia=colored(result[1],'green')
            code=colored(result[3],'yellow')
            street=colored(result[2],'blue')
            print wilaya+", "+motamadia+", "+street+": "+code
        
    def main(self):
        parser = argparse.ArgumentParser(usage="-h for full usage")
        parser.add_argument('query',nargs='*', help='search query')
        args = parser.parse_args()
        query=" ".join(args.query)
        if query.isdigit():
            self.display(self.location(query))
        else:
            self.display(self.code(query))

if __name__ == '__main__':
    tunipost().main()




