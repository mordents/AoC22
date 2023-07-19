with open('AoC6input.txt','r') as f: #cooooolll
    myinput =f.readline().strip()
    
def read_idx(myinput):
    for i in range(len(myinput)):
        if len(set(myinput[i:i+14]))==14: #go through input , find the index where set is 4 chars
            answer=i+14     # get that idx +4 - last unique idx
            return answer
