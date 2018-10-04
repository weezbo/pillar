class Babysitter:
    PRE_BEDTIME_RATE = 12
    POST_MIDNIGHT_RATE = 16
    POST_BEDTIME_RATE = 8
    MINIMUM_START_TIME = 17
    MAXIMUM_END_TIME = 4

    def calculate_pay(self, start_time, end_time, bed_time = False):
        total_pay = 0
        try:
            times = self.time_verifier(start_time, end_time, bed_time)
        except Exception as e:
            return str(e)
        converted_start_time = times[0]
        converted_end_time = times[1]
        converted_bed_time = times[2]
        for i in range(converted_start_time, converted_end_time):
            if i > 23:
                total_pay += self.POST_MIDNIGHT_RATE
            elif converted_bed_time and i >= converted_bed_time:
                total_pay += self.POST_BEDTIME_RATE
            else:
                total_pay += self.PRE_BEDTIME_RATE
        return total_pay

    def verify_real_time(self, candidate):
        if candidate < 0 or candidate > 24:
            return False
        else:
            return True

    def midnight_converter(self, hour):
        if hour is False or hour > self.MAXIMUM_END_TIME:
            return hour
        else:
            return hour + 24


    def time_verifier(self, start_time, end_time, bed_time = False):
        if start_time in range(self.MAXIMUM_END_TIME, self.MINIMUM_START_TIME) or not self.verify_real_time(start_time):
            raise Exception("Start time is out of bounds")
        if end_time in range(self.MAXIMUM_END_TIME + 1, self.MINIMUM_START_TIME + 1) or not self.verify_real_time(end_time):
            raise Exception("End time is out of bounds")
        if bed_time and not self.verify_real_time(bed_time):
            raise Exception("Bed time is out of bounds")
        start_time = self.midnight_converter(start_time)
        end_time = self.midnight_converter(end_time)
        bed_time = self.midnight_converter(bed_time)
        if end_time <= start_time:
            raise Exception("End time must be later than start time")
        return start_time, end_time, bed_time
