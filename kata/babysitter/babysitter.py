
def calculate_total_for_period(hours, rate):
    return hours*rate;

def calculate_hours_for_period(start_time, end_time):
    if start_time < 4:
        start_time += 24
    if end_time < 17:
        end_time += 24
    return end_time - start_time

def babysitter_pay_calc(start_time, end_time, bed_time = False):
    pre_bed_rate = 12
    post_midnight_rate = 16
    if(end_time < 4 and end_time != 0):
        rate = post_midnight_rate
    else:
        rate = pre_bed_rate
    hours = calculate_hours_for_period(start_time, end_time)
    return calculate_total_for_period(hours, rate)
