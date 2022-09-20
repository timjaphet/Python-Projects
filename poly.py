#Parent class Console
class Console:
    name ='system'
    user = ''
    cost = ''
    endorsed_services = 'streaming gameplay'
    size = '2 GB'
    capability = '3K Capable'
    connection = 'HDMI'
    password = 'gamer'

    def getLoginInfo(self):
        entry_user = input("Enter your name")
        entry_password = input("Enter your password")
        if(entry_user == self.user and entry_password == self.password):
            print("Enjoy your gaming experince, {}".format(entry_user))
        else:
            print("Incorrect login try again or click forgot password")

#Child Class PS5
class PS5(Console):
    D_environment = True
    cyberspace = True
    sessionID = ''

    def getLoginInfo(self):
        entry_user = input("Enter your name")
        entry_sessionID = input("Enter your sessionID")
        if(entry_user == self.user and entry_sessionID == self.sessionID):
            print("Be Moved, {}".format(entry_user))
        else:
            print("We do not recongize login info try again")

#Child Class XBOX 
class XBOX(Console):
    icloud_streaming = True
    remote_compatibility = False
    ipcheck = ''

    def getLoginInfo(self):
        entry_user = input("Enter your name")
        entry_ipcheck = input("scan ip")
        if(entry_user == self.user and entry_ipcheck == self.ipcheck):
            print("Welcome to the worlds most powerful console experince, {}".format(entry_user))
        else:
            print("ipcheck failed please check connection ")

    
    
    
    
gammer = Console()
gammer.getLoginInfo()
