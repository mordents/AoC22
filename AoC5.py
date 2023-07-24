# Crates moved in each step - varying stacks of crates 
# crates can only be moved one at a time 
#after all steps , which crate will be on top of each stack?
# Start pos
#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# def get_instructions():
#     with open('example.txt','r') as f:
#         lines=f.readlines()
        
#         return instructions
def parse_instructions():
    with open('AoC5input.txt', 'r') as inp:
        lines=inp.readlines()           #read in lines#
        instructions = [line.split() for line in lines] #get each individual line#
        return instructions
        

def parse_instruction(instruction):
    instruction=[x for x in instruction if (x.isdigit())]
    instruction=[int(x) for x in instruction]
    instruction=tuple(instruction)
    return instruction

def move_crate(crate_stacks,instruction):
    how_many = instruction[0] #select how many ,from where, to where.
    from_where = instruction[1] - 1    #second list but 1st idx for cmp , so -1 
    to_where = instruction[2] - 1      # where it ends up in final list
    # while how_many>0:                                                                                        #minus no of boxes
    #     moving_crate=crate_stacks[from_where].pop() #currently being moved
    #     crate_stacks[to_where].extend(moving_crate) 
    #     how_many-=1
    moving_crates = []
    reversed_moving_crates = reversed(moving_crates)
    while how_many>0:
        moving_crate=crate_stacks[from_where].pop()  #crate_stacks[to_where].extend(moving_crate) 
        crate_stacks[to_where].extend(moving_crate)
        how_many-=1
    
    crate_stacks.extend(reversed_moving_crates)
    
    return crate_stacks

def move_crates(crate_stacks, instructions):
    for instruction in instructions:
        parsed_instruction = parse_instruction(instruction=instruction)
        crate_stacks=move_crate(crate_stacks=crate_stacks,instruction=parsed_instruction) 

    return  crate_stacks

def top_crates(crate_stacks):
    top_crates=[]
    for crate_stack in crate_stacks:
        top_crates.append(crate_stack[-1])
    print('\n')
    print(top_crates)
    return top_crates
    

crate_stacks = [['B','Z','T'],['V','H','T','D','N'],['B','F','M','D'],
                ['T','J','G','W','V','Q','L'],['W','D','G','P','V','F','Q','M'],
                ['V','Z','Q','G','H','F','S'],['Z','S','N','R','L','T','C','W'],
                ['Z','H','W','D','J','N','R','M'],['M','Q','L','F','D','S']
            ]

instructions = parse_instructions()
move_crates(crate_stacks=crate_stacks,instructions=instructions)
top_crates(crate_stacks)


