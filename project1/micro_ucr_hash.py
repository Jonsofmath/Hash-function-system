
# [in] 16-bit block to which the hash array will be calculated. 
# [out] H: hash array of 16-bit block
def micro_ucr_hash(array_numbers):

    #32 variable length array initialize.
    delim = 0xFF
    w_length = 32
    W = [0] * (w_length&delim)
  
    for W_index in range(0, len(W)):
        if(W_index <= 15):
            W[W_index] = (array_numbers[W_index]) & delim
        else:
            W[W_index] = (W[W_index - 3] | (W[W_index - 9] ^ W[W_index - 14])) & delim

    #micro_ucr_hash result array initialize.
    h_length = 3
    H = [0] * (h_length&delim)
    
    for h_index in range(0, len(H)):
        if(h_index == 0):
            H[h_index] = 0x01
        elif(h_index == 1):
            H[h_index] = 0x89
        else:
            H[h_index] = 0xfe

    #output result loop.
    for iter in range(0, len(W)):
        #hash variables initialize.
        if(iter == 0):
            for h_index in range(0, len(H)):
                if(h_index == 0):
                    a = H[h_index]
                elif(h_index == 1):
                    b = H[h_index] 
                else:
                    c = H[h_index]
        #k and x assignment according to iter value.
        if(0 <= iter <= 16):
            k = 0x99
            x = (a ^ b) & delim
        else:
            k = 0xa1
            x = (a | b) & delim
        #a, b, c reassignments.
        a = (b ^ c) & delim
        b = (c << 4) & delim
        c = (x + k + W[iter]) & delim
        #hash output assignment.
        if(iter == 31):
            for h_index in range(0, len(H)):
                if(h_index == 0):
                    H[h_index] = (H[h_index] + a) & delim
                    #print(hex(H[h_index]))
                elif(h_index == 1):
                    H[h_index] = (H[h_index] + b) & delim
                    #print(hex(H[h_index]))
                else:
                    H[h_index] = (H[h_index] + c) & delim     
                    #print(hex(H[h_index]))
        else:
            continue
        return H