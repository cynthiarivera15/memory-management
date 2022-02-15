#-------------------------------------------------------------------------------
# Cynthia Marie Rivera Sánchez
# 801-19-5470
# CCOM4017 - 002
# Projetc 2
#-------------------------------------------------------------------------------
# Descrption:  Simulates the Optimal Page Replacement Algorithm
#-------------------------------------------------------------------------------

from sys import argv

DEBUG = 0

access_requests_list = []
N = 0

#Class - Object: Page in Physical Memory
class PagePhysicalMemory:
    page_address = 0
    operation = ''

    def __init__(self, page_address, operation):
        self.page_address = page_address
        self.operation = operation

    def ret_add(self):
        return self.page_address

    def ret_ope(self):
        return self.operation

# Funtion that reads the text file
def ReadFile(input):
    global access_requests_list

    file = open(input, "r")

    access_requests = file.read()
    access_requests_list = access_requests.split()

    file.close()

# Function will remove in order the page requests one at a time so it can be
# evaluated
def ReadingRequests():
    global access_requests_list

    return access_requests_list.pop(0)

# Function that checks if the page requested is already in the Physical Memory
# (counts page faults)
def SearchPhyMem(page_address, physical_memory):
    i = 0
    present = False
    while(i < len(physical_memory) and present == False):
        if(page_address == physical_memory[i].ret_add()):
            present = True
        else:
            i += 1

    return present

# Function that changes the operation done in the page in case it was found
# in Physical Memory
def ChangingOperation(page_address, operation, physical_memory):
    i = 0
    found = False
    while(i < len(physical_memory) and found == False):
        if(page_address == physical_memory[i].ret_add()):
            found = True
            physical_memory[i].operation = operation
        else:
            i += 1

# Function that looks through the access request which page will never be used
# again or is the furthest away to be used
def LocationRemovePage(physical_memory):
    location_requests = 0
    location_phy_mem = 0
    found = ""
    for i in range(len(physical_memory)):
        for j in range(len(access_requests_list)):
            ope, pg = access_requests_list[j].split(':')
            if(physical_memory[i].ret_add() != pg):
                found = False
            else:
                found = True
                if(j > location_requests):
                    location_requests = j
                    location_phy_mem = i
                break
        if(found == False):
            return i
    return location_phy_mem

def main():
    global N
    global access_requests_list

    physical_memory = []
    page_fault = 0

    N = int(argv[1])  # Receives number of pages the Physical Memory has room for
    input_file = argv[2]  # Receives text file

    ReadFile(input_file)

    # "Executes" all the page access requests and replace them in Physical Memory
    # if is needed
    while(len(access_requests_list) != 0):
        operation, page_address = ReadingRequests().split(':')
        element = PagePhysicalMemory(page_address, operation)
        present = SearchPhyMem(page_address, physical_memory)

        # If found in Physical Memory
        if(present == True):
            ChangingOperation(page_address, operation, physical_memory)
            if(DEBUG == 1):
                for i in range(len(physical_memory)):
                    print(physical_memory[i].ret_add(), physical_memory[i].ret_ope())

        # If is not found in Physical Memory
        else:
            page_fault += 1

            # Adds page address if the Physical Memory still has room for
            # more pages
            if(len(physical_memory) != N):
                physical_memory.append(element)
                if(DEBUG == 1):
                    for i in range(len(physical_memory)):
                        print(physical_memory[i].ret_add(), physical_memory[i].ret_ope())

            # If the Physical Memory does not have room for any more pages, it
            # looks for the position where the last page was added, removes it
            # and replace it with the new one
            else:
                location = LocationRemovePage(physical_memory)
                physical_memory.pop(location)
                physical_memory.insert(location, element)
                if(DEBUG == 1):
                    for i in range(len(physical_memory)):
                        print(physical_memory[i].ret_add(), physical_memory[i].ret_ope())

    print('The number of page faults were: ' + str(page_fault))

if __name__ == "__main__":
    main()
