# https://medium.com/quick-code/understanding-self-in-python-a3704319e5f0

class house_blueprint():
    cfloorname = "class default floor"
    cfloornumber = 100
    cfloorlevel = "default level"
    
    def __init__(self, mfloorname, mfloornumber, mfloorlevel):
        self.instance_floorname = mfloorname
        self.ifloornumber = mfloornumber
        self.ifloorlevel = mfloorlevel
    
    def get_floor(self):
        print("+=====================+ ")
        print("This is the ", self.instance_floorname)
        print("its number is ", self.ifloornumber)
        print("and the level is ", self.ifloorlevel)
        print("-=====================- ")
        print(" ")
        
erdgeschoss = house_blueprint("Erdgeschoss",0,"ground level")
erdgeschoss.get_floor()
erdgeschoss.name = "erdgeschoss"

erstesgeschoss = house_blueprint("Erstes Geschoss",1,"first level")
erstesgeschoss.get_floor()
erstesgeschoss.name = "erstesgeschoss"

print("class variable is accessible in every child object of this class")
print("The default floor of ", erdgeschoss.name, " is named: ", erdgeschoss.cfloorname)
print("The default floor of ", erstesgeschoss.name, " is named: ", erstesgeschoss.cfloorname)


#print(erstesgeschoss.mfloorname)
