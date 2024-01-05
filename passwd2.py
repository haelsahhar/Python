import os.path
from pprint import pprint


passwd_file = "/etc/passwd"                                 # default path for passwd file
words = []                                                  # initialization
line = 0                                                    # initialization
username = ""                                               # initialization
userid = ""                                                 # initialization
user=[]                                                     # initialization


#### Check if passwd file exists
def filecheck(passwrd_file):
    file_exist = os.path.isfile(passwd_file)
    if file_exist is False:
        print ("Passwd file does not exit")
        exit()





#### List users in passwd file 
def get_users(passwd_file):
    filecheck(passwd_file)
    with open(passwd_file) as file:                         # opens the file
        for line in file:                                   # loop through the lines
                if line.__contains__(':'):
                    words = line.split(':')                     # each line converted into a a set of items seperated by :
                    if int(words[2]) >= 100:                   # if third item (userid) > 1000
                        global username
                        global userid
                        global user
                        username = words[0]
                        userid = words[3]
                        user=[username,userid]
                        passwd_printer(user)
                        #print ("Username:", username, "\n", "   User ID:",userid, "\n")         # print both username (first item) & userid (third item)





#### Printing results
def passwd_printer(user):
    print ("Username:", username, "\n", "   User ID:", userid, "\n")
    #pprint(user, depth =1)   

get_users(passwd_file)                                      # calling the actual function, passing the file path