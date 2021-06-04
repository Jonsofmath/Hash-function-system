
# [in] input0, input1: numbers to "validate"
# [out] validity_reg: 1 if input0 and input1 are 1.

# in system, inputs representate wire who holds a 0 if the given hash byte
# is greather than target of zero if opposite.
# then we need to validate if the two bytes are lower than target:
# validity_reg holds 0 if no and 1 if yes.

def validity(input0, input1):
    validity_reg = 0
    if(input0 == 1 and input1 == 1): 
        validity_reg = 1
    else:
        validity_reg = 0           

    return validity_reg
