win_scenarios = [['Rock','Scissors'],['Scissors','Paper'],['Paper','Rock']]
outcomes = {'lose':0,'draw':3,'win':6}
shapes = {'A':'Rock','B':'Paper','C':'Scissors','X':'Rock','Y':'Paper','Z':'Scissors'}
shape_points = {'Rock':1,'Paper':2,'Scissors':3}


with open('AoC2input.txt', 'r') as inp:
    lines=inp.readlines()           #read in lines#
    all_letters = [line.split() for line in lines] #get each individual line#
    myscore=0

    for ours, theirs in all_letters:
        myshape = shapes[ours]
        theirshape=shapes[theirs]
        myscore+=shape_points[myshape]

        if myshape==theirshape:
            myscore+=3
        elif myshape!=theirshape:
            for i in range(len(win_scenarios)):
                if myshape==win_scenarios[i]:
                    print('cool')

