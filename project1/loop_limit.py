
from compare import compare_block

# [in] current_loop: actual loop value to compare.
# [in] loop_limit: loop limit parameter.
# [out] current_loop: if no limit reached, return actualized loop value
# [out] fail: if loop limit reached set value to 1, else 0

def loop_limit(current_loop, loop_limit):

    # limit loop module
    loop_status = compare_block(current_loop, loop_limit)

    # loop exceeds limit
    if(loop_status == 0x04):    #current_loop > loop_limit
        fail = 1
    else:
        fail = 0

    # loop under limit
    if(loop_status == 0x01 or loop_status == 0x02):
        current_loop = current_loop + 1
    else:
        current_loop = 0

    return current_loop, fail
