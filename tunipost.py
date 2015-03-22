import csv

class tunipost:
    def get_code(self,location):
        results=[]
        with open('codes.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if location in row[2].lower():
                    results.append(row)
        return results

    def get_location(self,code):
        results=[]
        with open('codes.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if str(code) in row[3].lower():
                    results.append(row)
        return results

