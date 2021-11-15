print("testing if this python script ran by a print statement")

#import markdown
import re
import os

# Get the current working
# directory (CWD)
cwd = os.getcwd()
# Print the current working
# directory (CWD)
print("Current working directory:", cwd)

path_back_to_repo_home = "../"
#### Directory of directory with markdown files imported from elsewhere
assets_directory = "assets"

markdown_subdirectory = "markdownFiles/"
#### Filename
markdown_test_file = "awesome-open-geoscience_README.md"

# Path
path_to_markdown_test_file = os.path.join(path_back_to_repo_home ,assets_directory, markdown_subdirectory, markdown_test_file)

#### Open and read the file at the path established above
f = open(path_to_markdown_test_file, 'r') 
text = f.read() 

#### Commenting out this line to print the entire markdown for now but it might be useful later!
# print("text is:",text)

#### Finds all the strings that match the expression below looking for https://github.com/ and then some characters then / then characters then / before end of word.
found_in_search = re.findall(r'https://github.com/\w+/\w+',text)

#### Printing for testing right now but will likely remove or comment out or make only print in verbose mode later?
#print("found_in_search",found_in_search,"which is ",len(found_in_search)," items.")
#print(type(found_in_search))

#### Take out duplicates
found_in_search_no_duplicates = list(dict.fromkeys(found_in_search))
#print(len(found_in_search_no_duplicates))

print("found ",len(found_in_search_no_duplicates), "different URLs to github of the form https://github.com/ ... / ... / in the markdown file",markdown_test_file)
print("They are:",found_in_search_no_duplicates)

#### Function to strip out https://github.com/

#### Function to get the orgs and/or usernames as a list with a count of how many repos from each orgname/username

#### Function to get results in form username/reponame