
def calculate_total_for_period(hours, rate):
    return hours*rate;

def calculate_hours_for_period(start_time, end_time):
    start_hour = int(start_time[0:2])
    end_hour = int(end_time[0:2])
    return end_hour - start_hour

