# find all directories with a total size 
#of at most 100000 , calculate sum of total sizes 

#example - directories a and e - total sum 95437 (94853+584)
#Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

#sample input #
#$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k

#expected output#
# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)
from AoC7 import read_file,get_items,order_items, find_total
import pytest
def test_read_file():

    file = 'AoC7input.txt'      #Given
    expected_file = ('AoC7input.txt')  #When 
    actual_file = read_file(file=file)    #Then#
    assert expected_file == actual_file

def test_get_items():
    items = read_file(file=file)
    expected_items = ['cd /','ls','dir a','14848514 b.txt','8504156 c.dat','dir d','cd a','ls','dir e','29116 f','2557 g','62596 h.lst'
                         'cd e','ls','584 i','cd ..','cd ..','cd d','ls','4060174 j','8033020 d.log','5626152 d.ext','7214296 k']
    actual_items = get_items(items=items)
    assert expected_items==actual_items

def test_order_items():
    command = get_items(file=file)    #Given
    expected_order = ['
    
                    #When
    actual_order=                       #Then
    assert expected_command==actual_command

def test_find_total():          #function to find total of each direct. #
    find_total = find_total(total=total)
    expected_total = 94853
    actual_total = find_total(total=total)
    assert expected_total==actual_total

   