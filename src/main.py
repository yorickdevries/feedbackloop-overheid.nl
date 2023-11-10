import csv

def make_counts(listtocount, field):
    outputdict = {}
    
    for elem in listtocount:
        if not elem[field] in outputdict:
            outputdict[elem[field]] = 0
    
    for elem in listtocount:
        outputdict[elem[field]] += 1
    
    print(outputdict)
    

if __name__ == '__main__':
    
    objlist = []
    
    with open('../Data/contacts_1400.csv', newline='\n') as csvfile:
        header = ["date",
                    "time",
                    "channel",
                    "ministry",
                    "subject",
                    "contactReason",
                    "outcome",
                    "pageTitle",
                    "forward",
                    "forwardCode"
                    ]
        reader = csv.reader(csvfile, delimiter=';')
        headerdone = False
        
        for row in reader:
            if not headerdone:
                headerdone = True
            else:
                obj = {}
                for i in range(len(header)):
                    obj[header[i]] = row[i]
                    objlist.append(obj)
    
    #make_counts(objlist, "date")
    #make_counts(objlist, "time")
    #make_counts(objlist, "channel")
    #make_counts(objlist, "ministry")
    #make_counts(objlist, "subject")
    #make_counts(objlist, "contactReason")
    #make_counts(objlist, "outcome")
    #make_counts(objlist, "pageTitle")
    #make_counts(objlist, "forward")
    #make_counts(objlist, "forwardCode")