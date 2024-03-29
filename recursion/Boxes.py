# Description: This program determines the largest nestable set of boxes given n number of box dimensions.
# It utilizes a recursive subsets function, and outputs the nestable subsets that match the maximum length.
# The program reads a file called boxes.txt which consists of the number of boxes and the dimension of each box


# checks if box1 fits in box2
# returns bool
def does_fit(box1, box2):
    return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]

# checks if list of boxes nest
# returns False if does_fit fails
def nested_list(lst):
    for i in range(len(lst) - 1):
        if does_fit(lst[i], lst[i + 1]) == False:
            return False

# finds subsets of nested boxes 
def sub_sets(a, b, nested, idx):
    if idx  == len(a):
        nested.append(b)
    else:
        c = b[:]
        b.append(a[idx])
        if nested_list(b) == None:
            sub_sets(a, b, nested, idx + 1)
        if nested_list(c) == None: # not elif because these are not mutually excl.
            sub_sets(a, c, nested, idx + 1)
        else: # both False, move on to next idx
            idx += 1
      
# reads file and prints largest subsets
def main():
  
    inf = open("boxes.txt", "r")

    # first line is num of boxes
    line = inf.readline()
    line = line.strip()
    num_boxes = int(line)

    # create box list
    box_list = []
    for i in range(num_boxes):
        line = inf.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)
  
    box_list.sort()
    inf.close()
    
    basket = []
    nesting = [] 
    sub_sets(box_list, basket, nesting, 0)
    if len(nesting) <= 2: # min size for nesting boxes
        print('No Nesting Boxes')
    else:
        print('Largest Subset of Nesting Boxes')

        # determine largest set
        largest = 0
        for i in range(len(nesting)):
            if len(nesting[i]) > largest:
                largest = len(nesting[i])
                
        # print all subsets of the largest size
        for i in range(len(nesting)):
            if len(nesting[i]) == largest: # if same size then print
                for j in range(len(nesting[i])):
                    print(nesting[i][j], end = '\n')
                print()


main()
