import csv
from prettytable import PrettyTable
import re
import argparse

class tunipost:
    def code(self,location):
        results=[]
        with open('codes.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                match = re.search(location, row[2].lower())
                if match:
                    results.append(row)
        return results

    def location(self,code):
        results=[]
        with open('codes.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                match = re.search(code, row[3].lower())
                if match:
                    results.append(row)
        return results
    def all(self):
        results=[]
        with open('codes.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                    results.append(row)
        return results
    def display(self,results):
        for result in results:
            print result[0]+", "+result[1]+", "+result[2]+": "+result[3]
        
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




