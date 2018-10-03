def babysitter_pay_calc(start_time, end_time, bed_time = False):
    minimum_start_time = 17
    if start_time < minimum_start_time:
        return "Start or end time is out of bounds"

