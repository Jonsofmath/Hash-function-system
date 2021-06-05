import numpy as np
from micro_ucr_hash import micro_ucr_hash
from compare import compare_block
from validity_reg import validity
from loop_limit import loop_limit
from nonce_gen import nonce_gen_perf

#
# @author: Jonathan Ramírez.
#

# performance optimization system
def perf_sys(block, start, target):

    # parameters definition
    delim = 0xFF
    LOOP_LIMIT = 5000
    FAIL_MESSAGE = "It is not possible to determinate the nonce output"

    loop_variable = 0
    enable_nonce = 1

    nonce_0 = np.array([0,0,0,0])
    nonce_1 = np.array([0,0,0,0])
    nonce_2 = np.array([0,0,0,0])
    nonce_final = np.array([0,0,0,0])
    nonce_string_zero = "["+hex(0)+", "+hex(0)+", "+hex(0)+", "+hex(0)+"]"
    finish = 0

    # system module start
    if(start):
        # nested "for" cycle for nonce calculation
        for i in range(0, delim):
            for j in range(0, delim):
                # nonce calculation must be enabled
                if(enable_nonce == 1):

                    # nonce generation
                    nonce_gen_perf(nonce_0, i, j, 0)
                    nonce_gen_perf(nonce_1, i, j, 1)
                    nonce_gen_perf(nonce_2, i, j, 2)

                    # hash function input generation
                    block_hash_0 = np.append(block,nonce_0)
                    block_hash_1 = np.append(block,nonce_1)
                    block_hash_2 = np.append(block,nonce_2)
            
                    # hash function module
                    hash_reg_0 = micro_ucr_hash(block_hash_0)
                    hash_reg_1 = micro_ucr_hash(block_hash_1)
                    hash_reg_2 = micro_ucr_hash(block_hash_2)

                    # validity module

                    # comparation for first hash byte
                    valid_h0_0 = compare_block(hash_reg_0[0], target & delim)
                    # comparation for second hash byte
                    valid_h1_0 = compare_block(hash_reg_0[1], target & delim)

                    # comparation for first hash byte
                    valid_h0_1 = compare_block(hash_reg_1[0], target & delim)
                    # comparation for second hash byte
                    valid_h1_1 = compare_block(hash_reg_1[1], target & delim)

                    # comparation for first hash byte
                    valid_h0_2 = compare_block(hash_reg_2[0], target & delim)
                    # comparation for second hash byte
                    valid_h1_2 = compare_block(hash_reg_2[1], target & delim)
                    
                    # register for determinate that the two bytes together are lower than target
                    validity_reg_0 = validity(valid_h0_0, valid_h1_0)
                    validity_reg_1 = validity(valid_h0_1, valid_h1_1)
                    validity_reg_2 = validity(valid_h0_2, valid_h1_2)

                    # it is just needed that at least one unit outputs a valid nonce

                    nonce_ready = 0     # set to one when a unit outputs a valid nonce
                    validity_reg = 0
                    if(validity_reg_0 == 1 and nonce_ready == 0):
                        nonce_final = nonce_0
                        nonce_ready = 1
                    elif(validity_reg_1 == 1 and nonce_ready == 0):
                        nonce_final = nonce_1
                        nonce_ready = 1
                    elif(validity_reg_2 == 1 and nonce_ready == 0):
                        nonce_final = nonce_2
                        nonce_ready = 1
   
                    if((validity_reg_0 == 1) or (validity_reg_1 == 1) or (validity_reg_2 == 1)):
                        validity_reg = 1
  
                    fail = 0
                    if(validity_reg):
                        finish = 1
                        nonce_final_string = "["+hex(nonce_final[0])+", "+hex(nonce_final[1])+", "+hex(nonce_final[2])+", "+hex(nonce_final[3])+"]"
                        return nonce_final_string, finish
                    else:
                        # limit loop module
                        loop_variable, fail = loop_limit(loop_variable, LOOP_LIMIT)
                        #print(loop_variable)
                        if(fail):
                            print(FAIL_MESSAGE, '\n')
                            return nonce_string_zero, finish
                else:
                    return nonce_string_zero, finish          
    else:
        return nonce_string_zero, finish
