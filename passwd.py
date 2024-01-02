passwd_file = "/etc/passwd"                                 # default path for passwd file
words = []                                                  # initialization
line = 0                                                    # initialization

def get_users(passwd_file):                                 # function to call passwd files and list users with userid > 1000
    with open(passwd_file) as file:                         # opens the file
        for line in file:                                   # loop through the lines
            try:
                words = line.split(':')                     # each line converted into a a set of items seperated by :
                if int(words[2]) >= 1000:                   # if third item (userid) > 1000
                    print (words[0], ":", words[2])         # print both username (first item) & userid (third item)
            except:                                         # exception to avoid lines without :'s 
                pass

get_users(passwd_file)                                      # calling the actual function, passing the file path