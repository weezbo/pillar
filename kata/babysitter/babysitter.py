def babysitter_pay_calc(start_time, end_time, bed_time = False):
    minimum_start_time = 17
    maximum_end_time = 4
    if start_time in range(maximum_end_time, minimum_start_time) or not real_time(start_time):
        return "Start time is out of bounds"
    elif end_time in range(maximum_end_time + 1, minimum_start_time + 1) or not real_time(end_time):
        return "End time is out of bounds"

    if end_time < 5:
        end_time += 24
    if start_time < 5:
        start_time += 24

    if end_time < start_time:
        return "End time must be later than start time"
    else:
        return "Acceptable times"

def real_time(candidate):
    if candidate < 0 or candidate > 24:
        return False
    else:
        return True