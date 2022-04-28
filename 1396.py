'''
So we are going to have a dictionary
(startionStart, startionEnd) --> (sumOfTimes, #trips)
We are going to also have a trip log for the trips that
haven't been resolved.

CheckIn:


'''

class UndergroundSystem:
    def __init__(self):
        self.finishedTrips = {}
        self.currentTrips = {}

    def checkIn(self, id, startStation, t):
        self.currentTrips[id] = (t, startStation)

    def checkOut(self, id, endStation, t):
        if id not in self.currentTrips:
            print("No match found for trip: {}".format(id))
            return

        startTime, startStation = self.currentTrips[id]
        elapsedTime = t - startTime
        tripKey = (startStation, endStation)

        if tripKey not in self.finishedTrips:
            self.finishedTrips[tripKey] = [elapsedTime, 1]
        else:
            self.finishedTrips[tripKey][0] += elapsedTime
            self.finishedTrips[tripKey][1] += 1

    def getAverageTime(self, startStation, endStation):
        if (startStation, endStation) not in self.finishedTrips:
            print("no record for trip: {}".format((startStation, endStation)))

        totalTime, totalTrips = self.finishedTrips[(startStation, endStation)]

        return totalTime/totalTrips

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
