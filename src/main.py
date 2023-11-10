import csv
import networkx as nx

def make_double_counts(listtocount, field1, field2):
    outputdict = {}
    
    for elem in listtocount:
        if not (elem[field1], elem[field2]) in outputdict:
            outputdict[(elem[field1], elem[field2])] = 0
    
    for elem in listtocount:
        outputdict[(elem[field1], elem[field2])] += 1
    
    return outputdict

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

def print_list(pl):
    counts = 0
    for elem in pl:
        counts += 1
        if elem["name"][0] == "WhatsApp":
            if counts > 100:
                return
            else:
                print(str(elem["name"][1]) + "\t" + str(elem["count"]))


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
    
    outputdict = make_counts(objlist, "channel")
    countlist = dict_to_list(outputdict)
    print_list(countlist)
    
    outputdict = make_double_counts(objlist, "channel", "subject")
    countlist = dict_to_list(outputdict)
    print_list(countlist)

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
    
    #outputdict = make_counts(objlist, "hoofdonderwerp")
    #countlist = dict_to_list(outputdict)
    
    #for elem in countlist:
    #    print(str(elem["name"]) + "\t" + str(elem["count"]))
    
    #make_counts(objlist, "time")
    #make_counts(objlist, "channel")
    #make_counts(objlist, "ministry")
    #make_counts(objlist, "subject")
    #make_counts(objlist, "contactReason")
    #make_counts(objlist, "outcome")
    #make_counts(objlist, "pageTitle")
    #make_counts(objlist, "forward")
    #make_counts(objlist, "forwardCode")
    print(len(objlist))
    
    
    nodes = {}
    
    field1 = "pw_previous_event_url"
    field2 = "pw_next_event_url"
    for elem in objlist:
        if not elem[field1] in nodes:
            nodes[elem[field1]] = 0

        if not elem[field2] in nodes:
            nodes[elem[field2]] = 0
    
    for elem in objlist:
        nodes[elem[field1]] += 1
        nodes[elem[field2]] += 1
    
    print(len(nodes))
    
    #outputdict = make_counts(objlist, "pw_previous_event_url")
    #outputdict2 = make_counts(objlist, "pw_next_event_url")
    
    #for obj in objlist:
    #    print("a")
    
    print("Constructing graph")
    
    
    G_nodes = []
    # make a node for every gene
    for node in nodes:
        G_nodes.append(node)
    
    # the #occurences of the connection should be higher than the threshold to be incorporated in the graph
    # 1 or 2
    threshold = 100
    G_edges_orig = {}
    
    for elem in objlist:
        if not (elem[field1], elem[field2]) in G_edges_orig:
            G_edges_orig[(elem[field1], elem[field2])] = 0
    
    for elem in objlist:
        G_edges_orig[(elem[field1], elem[field2])] += 1
    
    print(len(G_edges_orig))
    
    G_edges = []
    
    for elem in G_edges_orig:
        weigth =  G_edges_orig[elem]
        if weigth > threshold:
            G_edges.append((elem[0], elem[1], weigth))
    
    # create a graph from the distance matrix
    G = nx.DiGraph()
    G.add_nodes_from(G_nodes)
    G.add_weighted_edges_from(G_edges)
    print("Graph made:", len(G.nodes), len(G.edges))
    
    # remove all isolated genes
    G.remove_nodes_from(list(nx.isolates(G)))
    
    print("Graph made:", len(G.nodes), len(G.edges))
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    #contacts_1400()
    piwik_events()
    
    
    
    
    
    
    
    
    
    
    
    
    
    