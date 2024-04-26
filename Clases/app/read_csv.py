import csv

def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            data.append(dict(zip(header, row)))
        return(data)
    
def read_csv_2(path):
    with open(path,'r') as csvfile:
        reader = list(csv.DictReader(csvfile, delimiter=','))
        return reader

if __name__ == '__main__':
    data = read_csv_2(r'Python 102\Clases\app\data.csv')
    print(data)