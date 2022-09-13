import json
  
# Opening JSON file
f = open('lazy-load.json')

data = json.load(f)

# List of image containing component names to check against
imageContainList = ['image', 'gallery', 'slider', 'banner']

# Making the assumption that the first content array from the page root will contain the layout components
firstNode = data['content']

# List of ids that will be loaded immediately (this list will have max 3)
loadIdList = []

def find_images(node,depth):
    # Scenarios: 
    # 1 - If an image component is found check if the loadIdList is less than 3
    # if so then add the component name and id
    # 2 - Array was found in the node so recursively check for image component
    # 3 - If the loadIdList is full (3 found already) stop searching and print out the ids that were found
    # 4 - Final case is where all nodes have been checked and no more image components have been found
    for comp in node:
        if node[comp] in imageContainList:
            if len(loadIdList) < 3:
                print("Found image containing component: {}".format(node[comp]))
                print("With id: {}".format(node['id']))
                print("This id will be added to the list of immediately loaded image components\n")
                loadIdList.append([node[comp],node['id']])
            else:
                break
        elif isinstance(node[comp], list):
            for comp in node[comp]:
                find_images(comp, depth+1)

# Making the assumption that the first content array will contain the layout components
print()
for child in firstNode:
    try:
        if len(loadIdList) < 3:
            find_images(child,0)
        else:
            print("Maximum amount of ids found stopping search\n")
            break
    # Basic error handling
    except:
        print("An error occured please refer to the readme to make sure instructions were followed")

print("The following ids correspond with image components to be loaded immediately:\n")
for nodeId in loadIdList:
    print("{}: {}".format(nodeId[0],nodeId[1]),end='\n\n')

# Closing file
f.close()