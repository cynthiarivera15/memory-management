#-------------------------------------------------------------------------------
# Cynthia Marie Rivera Sánchez
# 801-19-5470
# CCOM4017 - 002
# Projetc 2
#-------------------------------------------------------------------------------
# Descrption:  Simulates the WSClock Page Replacement Algorithm
#-------------------------------------------------------------------------------

from sys import argv

DEBUG = 0

access_requests_list = []
N = 0
position_pointer = 0

#Class - Object: Page in Physical Memory
class PagePhysicalMemory:
    page_address = 0
    operation = ''
    reference_bit = 1
    clock = 0

    def __init__(self, page_address, operation, clock):
        self.page_address = page_address
        self.operation = operation
        self.reference_bit = 1
        self.clock = clock

    def ret_add(self):
        return self.page_address

    def ret_ope(self):
        return self.operation

    def ret_refbit(self):
        return self.reference_bit

    def ret_clock(self):
        return self.clock

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

# Function that actualizes the operation done, reference bit and clock in case
# tha page was found in Physical Memory
def UpdatingPage(page_address, operation, clock, physical_memory):
    i = 0
    found = False
    while(i < len(physical_memory) and found == False):
        if(page_address == physical_memory[i].ret_add()):
            found = True
            physical_memory[i].operation = operation
            physical_memory[i].reference_bit = 1
            physical_memory[i].clock = clock
        else:
            i += 1

# Function that checks which page isn't reference and isn't on the working set
# to return the location of the page that can be remove
def LocationRemovePage(tau, clock, physical_memory):
    global N
    global position_pointer

    smallest_time = 0
    pos_pag_smll_time = 0

    for i in range(N):
        if(physical_memory[position_pointer % N].ret_refbit() == 1):
                physical_memory[position_pointer % N].reference_bit = 0
                if(smallest_time == 0 or smallest_time > physical_memory[position_pointer % N].ret_clock()):
                    smallest_time = physical_memory[position_pointer % N].ret_clock()
                    pos_pag_smll_time = position_pointer % N
                position_pointer += 1
        else:
            age = clock - physical_memory[position_pointer % N].ret_clock()

            if(age > tau):
                position_pointer += 1
                return (position_pointer - 1) % N
            else:
                if(smallest_time == 0 or smallest_time > physical_memory[position_pointer % N].ret_clock()):
                    smallest_time = physical_memory[position_pointer % N].ret_clock()
                    pos_pag_smll_time = position_pointer % N
                position_pointer += 1

    return pos_pag_smll_time

def main():
    global N
    global position_pointer
    global access_requests_list

    physical_memory = []
    page_fault = 0
    clock = 0

    N = int(argv[1])  # Receives the number of pages the Physical Memory has room for
    tau = int(argv[2]) # Receives the interval of time used to make decisions
    input_file = argv[3]  # Receives text file

    ReadFile(input_file)

    # "Executes" all the page access requests and replace them in Physical Memory
    # if is needed
    while(len(access_requests_list) != 0):
        operation, page_address = ReadingRequests().split(':')
        clock += 1
        element = PagePhysicalMemory(page_address, operation, clock)
        present = SearchPhyMem(page_address, physical_memory)

        # If found in Physical Memory
        if(present == True):
            UpdatingPage(page_address, operation, clock, physical_memory)
            if(DEBUG == 1):
                for i in range(len(physical_memory)):
                    print(physical_memory[i].ret_add(), physical_memory[i].ret_ope(),
                    physical_memory[i].ret_clock(), physical_memory[i].ret_refbit())

        # If is not found in Physical Memory
        else:
            page_fault += 1

            # Adds page address if the Physical Memory still has room for
            # more pages
            if(len(physical_memory) != N):
                physical_memory.append(element)
                position_pointer += 1
                if(DEBUG == 1):
                    for i in range(len(physical_memory)):
                        print(physical_memory[i].ret_add(), physical_memory[i].ret_ope(),
                        physical_memory[i].ret_clock(), physical_memory[i].ret_refbit())

            # If the Physical Memory does not have room for any more pages, it
            # looks for the position where the last page was added, removes it
            # and replace it with the new one
            else:
                location = LocationRemovePage(tau, clock, physical_memory)
                physical_memory.pop(location)
                physical_memory.insert(location, element)
                if(DEBUG == 1):
                    for i in range(len(physical_memory)):
                        print(physical_memory[i].ret_add(), physical_memory[i].ret_ope(),
                        physical_memory[i].ret_clock(), physical_memory[i].ret_refbit())

    print('The number of page faults were: ' + str(page_fault))

if __name__ == "__main__":
    main()
