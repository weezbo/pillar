class Babysitter:
    pre_bedtime_rate = 12
    post_midnight_rate = 16
    post_bedtime_rate = 8
    minimum_start_time = 17
    maximum_end_time = 4

    def babysitter_pay_calc(self, start_time, end_time, bed_time = False):
        total_pay = 0
        try:
            times = self.time_enforcer(start_time, end_time, bed_time)
        except Exception as e:
            return str(e)
        for i in range(times[0], times[1]):
            if i > 23:
                total_pay += self.post_midnight_rate
            elif times[2] and i >= times[2]:
                total_pay += self.post_bedtime_rate
            else:
                total_pay += self.pre_bedtime_rate
        return total_pay

    def real_time(self, candidate):
        if candidate < 0 or candidate > 24:
            return False
        else:
            return True

    def midnight_converter(self, hour):
        if hour is False or hour > 5:
            return hour
        else:
            return hour + 24


    def time_enforcer(self, start_time, end_time, bed_time = False):
        if start_time in range(self.maximum_end_time, self.minimum_start_time) or not self.real_time(start_time):
            raise Exception("Start time is out of bounds")
        if end_time in range(self.maximum_end_time + 1, self.minimum_start_time + 1) or not self.real_time(end_time):
            raise Exception("End time is out of bounds")
        if bed_time and not self.real_time(bed_time):
            raise Exception("Bed time is out of bounds")
        start_time = self.midnight_converter(start_time)
        end_time = self.midnight_converter(end_time)
        bed_time = self.midnight_converter(bed_time)
        if end_time <= start_time:
            raise Exception("End time must be later than start time")
        return start_time, end_time, bed_time
