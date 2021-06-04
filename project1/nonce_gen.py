
# [in] array: input array to calcule it's elements values (nonce)
# [in] source0, source1: given iterators to determinate elements 
#                        of nonce arrays
# [out]: void function

def nonce_gen_area(array,source0, source1):
    delim = 0xFF
    array[0] = (source0) & delim 
    array[1] = (source0) & delim 
    array[2] = (array[0] + source1) & delim 
    array[3] = (array[1] + source1) & delim 


# [in] array: input array to calcule it's elements values (nonce)
# [in] source0, source1: given iterators to determinate elements 
#                        of nonce arrays
# [in] type: identifies the nonce unit that will calculate the nonce array
# [out]: void function

def nonce_gen_perf(array, source0, source1, type):
    delim = 0xFF
    if(type == 0):
        array[0] = (source0) & delim 
        array[1] = (source0) & delim 
        array[2] = (array[0] + source1) & delim 
        array[3] = (array[1] + source1) & delim 
    elif(type == 1):
        array[0] = (source0) & delim 
        array[1] = (array[0] + source1) & delim  
        array[2] = (source0) & delim
        array[3] = (array[2] + source1) & delim   
    elif(type == 2):
        array[0] = (array[1] + source1) & delim 
        array[1] = (source0) & delim   
        array[2] = (array[3] + source1) & delim
        array[3] = (source0) & delim         