class Babysitter:
    pre_bedtime_rate = 12
    post_midnight_rate = 16
    post_bedtime_rate = 8
    minimum_start_time = 17
    maximum_end_time = 4

    def calculatePay(self, start_time, end_time, bed_time = False):
        total_pay = 0
        try:
            times = self.timeVerifier(start_time, end_time, bed_time)
        except Exception as e:
            return str(e)
        converted_start_time = times[0]
        converted_end_time = times[1]
        converted_bed_time = times[2]
        for i in range(converted_start_time, converted_end_time):
            if i > 23:
                total_pay += self.post_midnight_rate
            elif converted_bed_time and i >= converted_bed_time:
                total_pay += self.post_bedtime_rate
            else:
                total_pay += self.pre_bedtime_rate
        return total_pay

    def verifyRealTime(self, candidate):
        if candidate < 0 or candidate > 24:
            return False
        else:
            return True

    def midnightConverter(self, hour):
        if hour is False or hour > 4:
            return hour
        else:
            return hour + 24


    def timeVerifier(self, start_time, end_time, bed_time = False):
        if start_time in range(self.maximum_end_time, self.minimum_start_time) or not self.verifyRealTime(start_time):
            raise Exception("Start time is out of bounds")
        if end_time in range(self.maximum_end_time + 1, self.minimum_start_time + 1) or not self.verifyRealTime(end_time):
            raise Exception("End time is out of bounds")
        if bed_time and not self.verifyRealTime(bed_time):
            raise Exception("Bed time is out of bounds")
        start_time = self.midnightConverter(start_time)
        end_time = self.midnightConverter(end_time)
        bed_time = self.midnightConverter(bed_time)
        if end_time <= start_time:
            raise Exception("End time must be later than start time")
        return start_time, end_time, bed_time
