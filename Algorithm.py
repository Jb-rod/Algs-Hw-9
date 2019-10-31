import sys

global block_arr
global num_blocks
block_arr = []


# returns the maximum height of a valid stack with block i at the top
# valid means each block is smaller in width and length than the blocks below it
def stack(idx, table):
    if idx == 0:
        return (0, 0)
    else:
        if(table[idx] is None):  # you need to fill in the entry
            block_length = block_arr[idx][0]
            block_width = block_arr[idx][1]
            block_height = block_arr[idx][2]
            max_height = 0
            last_block = 0
            # find the max height of a stack with this block on top, keep this height,
            # as well as the location in the array of the block below
            for i in range(0, idx):
                # if you can place here
                if(block_arr[i][0] > block_length and block_arr[i][1] > block_width):
                    (stack_height, temp) = stack(i, table)
                    if(stack_height >= max_height):
                        # stack height becomes the new max, keep a pointer to this block
                        max_height = stack_height
                        place = i
            # return the max height of all legal stacks with this block on top, as well as the block
            # directly below it in the stack
            max_height += block_height
            table[idx] = (max_height, place)
            return (max_height, place)
        else:  # you already did that! nice! return it
            return table[idx]


def read_arr(file):

    f = open(file)
    for line in f:
        dimensionStrs = line.strip().split(' ')
        if len(dimensionStrs) == 1:
            num_blocks = int(dimensionStrs[0])
        else:
            block = []
            for dimension in dimensionStrs:
                block.append(int(dimension))
            # add all possible orientations of this block to your list
            block_arr.append([block[0], block[1], block[2]])
            block_arr.append([block[0], block[2], block[1]])
            block_arr.append([block[1], block[0], block[2]])
            block_arr.append([block[1], block[2], block[0]])
            block_arr.append([block[2], block[0], block[1]])
            block_arr.append([block[2], block[1], block[0]])
    f.close()



# recursively constructs the solution from the table and index of max


def reconstruct(table, k):
    reconstruction = []
    while(k > 0):
        reconstruction.append(block_arr[k])
        k = table[k][1]
    return(reconstruction)


def main():
    print(0)
    read_arr(sys.argv[1])
    block_arr.sort()
    block_arr.reverse()
    # put a block that can always be a base at the beginning of the list for recursion reasons
    block_arr.insert(0, (float("inf"), float("inf"), float("inf")))
    print(block_arr)
    # instantiate the DP table of length k+1 with Nones
    table = [None] * (len(block_arr))
    table[0] = (0,0)

    for i in range(0, len(block_arr)):
        stack(i, table)
    (height, prev) = max(table)
    index = table.index((height, prev))
    print(index)
    solution = reconstruct(table, index)
    print(solution)
    print('The tallest tower has ' + str(len(solution)) +
          ' blocks and a height of ' + str(height))
    with open(sys.argv[2], 'w') as outfile:
        outfile.write(str(len(solution)) + '\n')
        for elt in reversed(solution):
            outfile.write(str(elt[0]) + ' ' +
                          str(elt[1]) + ' ' + str(elt[2]) + '\n')


if __name__ == "__main__":
    main()
