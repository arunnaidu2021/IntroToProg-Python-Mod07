# ------------------------------------------------------------------------ #
# Title: Assignment 07
# Description: Working with Exceptions and Pickling
#              Read in the user's file and display the headers.
#              Create a binary version of the input file.
# ChangeLog (Who,When,What):
# ANaidu,2.26.2023,Created initial outline.
# ANaidu,2.28.2023,Added file I/O details and functions.
# ------------------------------------------------------------------------ #
import pickle

# -- Data -- #
# declare global variables
strFileCSV = ""  # A string that represents the name of the csv database
strFileBIN = ""  # A string that represents the name of the binary database
strItemChoice = ""  # The user's choice to analyze
objFileCSV = None  # An object representing the actual database in csv format
objFileBIN = None  # An object representing the binary version
lstHeaderData = []  # A list of header data from the file - the first line
lstRow = []  # A row of data separated into elements



# -- Processing -- #


# -- Input/Output -- #
def get_file_name():
    """  Gets the filename from the user
    :param: none
    :return: filename without suffix
    """
    str_file = input("Please enter csv filename or return to exit: ")
    if '.' in str_file:  # user entered full filename
        raise Exception("Please enter the filename without the suffix.")

    return str_file


def open_file(str_file_csv):
    """ Opens the text file
    :param str_file_csv:
    :return obj_handle:
    """
    try:
        return open(str_file_csv, 'r')
    except FileNotFoundError:
        print("File not found.")
        exit(-1)


def print_header(obj_file):
    """ Show the items to the user
    :param obj_file:
    :return: list of header items
    """
    lst_header_data = obj_file.readline().split(',')  # Pull the header row from the dataset
    index = 0
    for i in lst_header_data:
        print(index, '\t', i)
        index += 1
    return lst_header_data   # return the list with the header row


def compactor(str_file_csv, str_file_bin):
    """ Compress text file into binary

    :param str_file_csv:
    :param str_file_bin:
    :return: none
    """
    lst_table = []
    obj_file_csv = open(str_file_csv, 'r')
    index = 0
    for i in lstHeaderData:  # read in data
        lstRow = obj_file_csv.readline().split()
        lst_table.append(lstRow)   # build table
    obj_file_csv.close()
    obj_file_bin = open(str_file_bin, "wb")
    pickle.dump(lst_table, obj_file_bin)
    obj_file_bin.close()

try:
    while True:
        strInput = get_file_name()
        if strInput == "":  # user has hit return to quit
            break
        strFileCSV = strInput + ".csv"  # form the input filename
        strFileBIN = strInput + ".dat"  # form the output filename
        objFileCSV = open_file(strFileCSV)   # open the csv file
        lstHeaderData = print_header(objFileCSV)
        objFileCSV.close()
        strItemChoice = int(input("Please enter the number of the parameter to process: "))  # no actual process
        while strItemChoice > len(lstHeaderData):   # error checking without using an exception
            print("Please pick from the numbered list.")
            strItemChoice = int(input("Please enter the number of the parameter to process: "))

        print("You picked: ", strItemChoice, '\t', lstHeaderData[(strItemChoice)])

        compactor(strFileCSV, strFileBIN)  # create binary file

except Exception as err:
    print("An error occurred: " + str(err))
    exit(-1)

print("All finished. Thank you.")
