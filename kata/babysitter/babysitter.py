def babysitter_pay_calc(start_time, end_time, bed_time = False):
    minimum_start_time = 17
    maximum_end_time = 4
    if start_time in range(maximum_end_time, minimum_start_time) or start_time > 24 or start_time < 0:
        return "Start time is out of bounds"
    elif end_time in range(maximum_end_time + 1, minimum_start_time + 1) or end_time > 24 or end_time < 0:
        return "End time is out of bounds"
    else:
        return "Acceptable times"
