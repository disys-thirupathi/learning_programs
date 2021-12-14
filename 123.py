def dinner():
    memcount = 10
    i=0
    buffet= [ {"biryani":25 , "Eggs": 25  , "chickenpiece": 50}, {"icecream":25 , "jamon":25} ]
    for i in range(memcount):
        for j in buffet:
            print (i,j)


def birthday():
    gift=[1,2,3,4,5,6,7,8,9,10]
    memcount = 10
    for i in range (memcount):
        for j in gift:
            print(i,j)

dinner()
birthday()
