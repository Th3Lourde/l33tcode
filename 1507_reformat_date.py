'''
Year: append
day: remove last two chars, if what is left len() == 0, put "0" + what_is_left
month: dict[str]-->str mappin

'''

class Solution:
    def reformatDate(self, date):
        months = {
        "Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06",
        "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"
        }

        date = date.split(" ")

        day = date[0][:-2]

        if len(day) < 2:
            day = "0" + day
        month = months[date[1]]
        yr = date[2]

        return "{}-{}-{}".format(yr, month, day)
