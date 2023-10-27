
import statistics as stats

from code.StockData import StockData

class StockMetrics(StockData):
    def __init__(self, path):
        # call the parent method's constructor
        super(StockMetrics, self).__init__(path)

        # now that we've ran self.load(), we can interact with "self.data" as a
        # list of lists
        self.load()

    def average01(self):
        
        averages = []
        for row in self.data:
            data_row=row[1:]
            y = []
            for x in data_row:
                try:
                    y.append(float(x))
    
                except ValueError:
                    continue
            average = stats.mean(y)
            rounded_average = round(average,3)
            averages.append(round(stats.mean(y),3))
        return averages

    def median02(self):

        medians = []
        for row in self.data:
            data_row=row[1:]
            m = []
            for t in data_row:
                try:
                    m.append(float(t))
                except ValueError:
                    continue
            if m:
                median = stats.median(m)       
                medians.append(median)
        return medians
        

    def stddev03(self):
        sdev = []

        for row in self.data:
            data_row = row[1:]

            s = []
            for t in data_row:
                try:
                    s.append(float(t))
                except ValueError:  
                    continue

            new_sd = stats.stdev(s)
            new_sd2= round(new_sd, 3)
            sdev.append(new_sd2)
        return sdev