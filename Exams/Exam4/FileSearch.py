#   FileSearch
#   - Enter in a word and we will search all .txt files in the local directory
#   for that word!
#   - If you want more files to search, simply put them in the same
#   directory as this program.
#   - Written by Nate Steward for Python class Fall 2017

import os
import Epic

################################################################################
#   main() - takes no arguments, returns nothing
#   - Gets a list of all files in the local directory.
#   - All non-text files are removed from the list (such as this .py file)
#   - We prompt the user for a term to search the text files for.
#   - Finally, we check all of the files for the search term.
################################################################################
def main():
    files = os.listdir(".")
    files = cleanUpFileList(files)
    searchTerm = Epic.userString("Enter a search term: ").upper()
    readFiles(files, searchTerm)

################################################################################
#   readFiles() - takes 2 arguments, returns nothing.
#   - Arguments:
#       - [] files, a list of filenames from the local directory.
#       - str searchTerm, the word the user chose to search the files for.
#   - readFiles will search every line in the list of files for the search term.
#   - Whenever it finds a search term, it prints the filename and then the line.
################################################################################
def readFiles(files, searchTerm):
    for filename in files:
        file = open(filename, 'r')
        for line in file:
            wordInLine = False
            words = line.upper().split(' ')
            for word in words:
                if searchTerm in word:
                    wordInLine = True
            if wordInLine == True:
                print "%s: %s" % (filename, line.upper()),

################################################################################
#   cleanUpFileList() - takes one argument, returns a list of .txt files.
#   - Arguments:
#       - [] files, a list of filenames from the local directory.
#   - Removes all files from the list that don't have the '.txt' extension.
################################################################################
def cleanUpFileList(files):
    filesToBeRemoved = []
    for file in files:
        if file[-3:] != "txt":
            filesToBeRemoved.append(file)
    for file in filesToBeRemoved:
        files.remove(file)
    return files
    
main()