class disys:
    def __init__(self,vacc):
        self.vac=[]
        self.vac.append(vacc)
        self.count = 0
    def logic(self):
        for i in self.vac:
            if i["vaccine"] == None:
                self.count = self.count+1
            else:
                continue
        print(self.vac)
jb = disys({"name":"jamesbond","empid":"007","vaccine":None})
jb = disys({"name":"thirupathi","empid":"005","vaccine":"1st dose"})
jb.logic
