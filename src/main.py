import csv

def make_counts(listtocount, field):
    outputdict = {}
    
    for elem in listtocount:
        if not elem[field] in outputdict:
            outputdict[elem[field]] = 0
    
    for elem in listtocount:
        outputdict[elem[field]] += 1
    
    return outputdict

def dict_to_list(outputdict):
    outputlist = []
    for elem in outputdict:
        outputlist.append({"name": elem, "count": outputdict[elem]})
    outputlist.sort(key=lambda x: x["count"], reverse=True)
    return outputlist
    
def contacts_1400():
    
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

def piwik_events():
    
    objlist = []
    
    with open('../Data/piwik_events.csv', newline='\n', encoding="utf8") as csvfile:
        header = ["pw_session_id",
                    "pw_event_id",
                    "pw_visitor_id",
                    "pw_timestamp",
                    "pw_local_hour",
                    "pw_is_exit",
                    "pw_is_entry",
                    "pw_event_type",
                    "pw_event_url",
                    "pw_event_title",
                    "pw_outlink_url",
                    "pw_download_url",
                    "pw_search_keyword",
                    "pw_search_category",
                    "pw_search_results_count",
                    "pw_custom_event_category",
                    "pw_custom_event_action",
                    "pw_custom_event_name",
                    "pw_custom_event_value",
                    "pw_previous_event_url",
                    "pw_previous_event_title",
                    "pw_next_event_url",
                    "pw_next_event_title",
                    "pw_event_index",
                    "pw_page_view_index",
                    "pw_time_on_page",
                    "pw_date",
                    "page_type",
                    "ministerie",
                    "hoofdonderwerp"
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
    
    outputdict = make_counts(objlist, "hoofdonderwerp")
    countlist = dict_to_list(outputdict)
    
    for elem in countlist:
        print(str(elem["name"]) + "\t" + str(elem["count"]))
    
    #make_counts(objlist, "time")
    #make_counts(objlist, "channel")
    #make_counts(objlist, "ministry")
    #make_counts(objlist, "subject")
    #make_counts(objlist, "contactReason")
    #make_counts(objlist, "outcome")
    #make_counts(objlist, "pageTitle")
    #make_counts(objlist, "forward")
    #make_counts(objlist, "forwardCode")

if __name__ == '__main__':
    #contacts_1400()
    piwik_events()
    
    
    
    
    
    
    
    
    
    
    
    
    
    