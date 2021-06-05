import numpy as np
from micro_ucr_hash import micro_ucr_hash
from compare import compare_block
from validity_reg import validity
from loop_limit import loop_limit
from nonce_gen import nonce_gen_area

#
# @author: Jonathan Ramírez.
#

# area optimization system
def area_sys(block, start, target):

    #parameters definition
    delim = 0xFF
    LOOP_LIMIT = 5000
    FAIL_MESSAGE = "It is not possible to determinate the nonce output"

    hash_reg = np.array([0,0,0])
    loop_variable = 0
    enable_nonce = 1

    nonce = np.array([0,0,0,0])
    nonce_string_zero = "["+hex(nonce[0])+", "+hex(nonce[1])+", "+hex(nonce[2])+", "+hex(nonce[3])+"]"
    finish = 0

    #system module start
    if(start):
        #nested "for" cycle for nonce calculation
        for i in range(0, delim):
            for j in range(0, delim):
                #nonce calculation must be enabled
                if(enable_nonce == 1):

                    #nonce generation
                    nonce_gen_area(nonce, i, j)

                    nonce_string = "["+hex(nonce[0])+", "+hex(nonce[1])+", "+hex(nonce[2])+", "+hex(nonce[3])+"]"

                    # hash function input generation
                    block_hash = np.append(block,nonce)
            
                    # hash function module
                    hash_reg = micro_ucr_hash(block_hash)

                    # validity module

                    #comparation for first hash byte
                    valid_h0 = compare_block(hash_reg[0], target & delim)

                    #comparation for second hash byte
                    valid_h1 = compare_block(hash_reg[1], target & delim)
                    
                    #register for determinate that the two bytes together are lower than target
                    validity_reg = validity(valid_h0, valid_h1)

                    fail = 0

                    if(validity_reg):
                        finish = 1
                        
                        print("------ Number of iterations used:------", '\n')
                        print("          ",loop_variable, '\n')
                        
                        return nonce_string, finish
                    else:
                        # limit loop module
                        loop_variable, fail = loop_limit(loop_variable, LOOP_LIMIT)
                        #print(loop_variable)
                        if(fail):
                            print(FAIL_MESSAGE, '\n')
                            return nonce_string_zero, finish
                else:
                    return nonce_string, finish          
    else:
        return nonce_string_zero, finish
