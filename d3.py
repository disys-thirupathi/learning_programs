'''#approch 1

variable = "data"
print("------------------------------------------------------")

#approch 2

class handball:
    __game ="Handball"
    def __init__(self):
        self.ball_dia = "13.5cm"
        self.ball_weight = 1
    def court(self):
        self.__length = 30
        self.width = 20
    def display(self):
        print(handball.__game)
        print(self.__length)
ob=handball()
ob.court()
ob.display()
print("------------------------------------------------------")

#approch 3

handball=("HandBall",13.5,1,30,20)

print("Tuple approch ",handball[2])


handball=["HandBall",13.5,1,30,20]

print("List approch ",handball[3])
print("------------------------------------------------------")

#approch 4

handball1={"Game":"HandBall","ball_dia":13.5,"ball_weight":1,"court_length":30,"court_width":20}

print("Dictnary approch ",handball1["Game"])
print("------------------------------------------------------")

#approch 5

handball=["HandBall",13.5,1,30,20]

for i in handball:
    print(i)

handball1={"Game":"HandBall","ball_dia":13.5,"ball_weight":1,"court_length":30,"court_width":20}

for i in handball1.keys():
    print (i)
print("------------------------------------------------------")
#approch 6

game1=[{"Game":"HandBall",  "ball_dia":13.5,"ball_weight":1,    "court_length":30,"court_width":20},
       {"Game":"Basketball","ball_dia":16.5,"ball_weight":2.5,  "court_length":50,"court_width":40}]

print(game1[0],"\n",game1[1])

for i in game1:
    if i["Game"] == "HandBall":
        print("HandBall is a game")
print("-----------------------------------------------------")'''
#approch 7

game2=[{"Game1":[{"ballname":"HandBall",    "ball_dia":13.5,    "ball_weight":1},    {"court_length":30,  "court_width":20}]},
        {"Game2":[{"ballname":"Basketball",  "ball_dia":16.5,    "ball_weight":2.5},  {"court_length":50,  "court_width":40}]},
        {"Game3":[{"ballname":"Football",    "ball_dia":16,      "ball_weight":2},    {"court_length":50,  "court_width":40}]}]

'''for i in game2:
    if i["Game1"][0]["ballname"] =="HandBall":
        print("Its HandBall game")
    elif i["Game2"][0]["ballname"] =="Basketball":
        print("Its BasketBall game")
    elif i["Game3"][0]["ballname"] =="Football":
        print("Its FootBall game")
'''
for i in game2:
    for j in i.values():
        for k in j:
            if k["ballname"] == "HandBall":
                print ("the ball weight is 1kg")
                
#print("----------------------------------------------------")
