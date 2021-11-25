# Gabriel Alexandru - ACSAI Optional Homework 1 - A.Y. 2021-2022

def ex1(int_seq, subtotal):
    # Instantiate the variables. They are all in the same line so that i can be a little more efficient.
    # For values, split the string at the comma, then convert it in integer.
    values = list(map(int, int_seq.split(',')))
    total_sublist = 0
    partial_total = 0 
    dictionary = {}
    
    # Iterate through every element of the list.
    for elt in values:
        partial_total += elt
        # Check if my sum equals the subtotal I need to find.
        if partial_total == subtotal:
            total_sublist += 1

        # Find the difference between the sum and the subtotal
        difference = partial_total - subtotal

        # If I had already a sum with the same difference then add the count to the number of sublist.
        if difference in dictionary:
            total_sublist += dictionary[difference]
        
        # If I have already found this sum then increase the counter, otherwise set it to 1
        if partial_total in dictionary:
            dictionary[partial_total] += 1
        else:
            dictionary[partial_total] = 1

    # Return the final number of sublist
    return total_sublist

if __name__ == '__main__':
    pass
