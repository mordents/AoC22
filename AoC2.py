# Rock paper scissors #
#total score , sum of scores for each round#
#single round - score for shape selected (1 - Rock, 2 - Paper, 3- Scissors)
#score for the outcome of the round (0 -lose, 3 - draw,  6 win )

shapes = {'A':'Rock','B':'Paper','C':'Scissors','X':'Rock','Y':'Paper','Z':'Scissors'}
outcomes = {'lose':0,'draw':3,'win':6}
shape_points = {'Rock':1,'Paper':2,'Scissors':3}

with open('AoC2input.txt','r') as inp:
    lines=inp.readlines()
    allletters = [line.split() for line in lines]
    #allletters=[['A', 'Y'],['B','X'],['C','Z']]

print(allletters)

myscore=0
         #rounds variable#
for ours,theirs in allletters:  #for each pair#    
    
    myshape=shapes[ours]

    theirshape=shapes[theirs]

    myscore+=shape_points[myshape]      #mypoints
    print(myshape,theirshape)
    
    if myshape==theirshape:      #draw scenario
       myscore+=3
       print('draw')

    elif myshape!=theirshape:
        if myshape=='Rock' and theirshape == 'Scissors':
       #     print(myshape,theirshape)
            
            # myscore+=shape_points['Rock']
            myscore+=6
           
            print('we won')

        elif myshape=='Paper' and theirshape =='Rock':

            # myscore+=shape_points['Paper']
            myscore+=6
            print('we won')
        elif myshape=='Scissors' and theirshape=='Paper':

            # myscore+=shape_points['Scissors']
            myscore+=6
            print('we won')
        else:
            myscore+=0
            print('we lost')
            # myscore+=shape_points[myshape]
    else:
        print('got to this point')  
print(myscore)

#11945
