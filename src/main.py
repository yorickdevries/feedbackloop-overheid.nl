import csv

if __name__ == '__main__':
    
    with open('../Data/contacts_1400.csv', newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            obj = {
                "date": row[0],
                "time": row[1],
                "channel": row[2],
                "ministry": row[3],
                "subject": row[4],
                "contactReason": row[5],
                "outcome": row[6],
                "pageTitle": row[7],
                "forward": row[8],
                "forwardCode": row[9]
                }
            print(obj)
    