
# function for compare block
# it consist on a compare unit which outputs are three wires that activates
# exclusively once at time.

# [in] number0, number1: numbers to compare
# [out] compare_var: comparison value bus

def compare_block(number0, number1):
    compare_var = 0

    if(number0 < number1):
        compare_var = 0x01            #001
    elif(number0 == number1):
        compare_var = 0x02            #010
    else:
        compare_var = 0x04            #100

    return compare_var