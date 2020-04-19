import heapq
from collections import Counter

import storm


class TopNFinderBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        storm.logInfo("Counter bolt instance starting...")
        self._topN = dict()
        self._len = len(self._topN)

        # TODO:
        # Task: set N
        pass
        # End

        # Hint: Add necessary instance variables and classes if needed

    def process(self, tup):
        '''
        TODO:
        Task: keep track of the top N words
        Hint: implement efficient algorithm so that it won't be shutdown before task finished
              the algorithm we used when we developed the auto-grader is maintaining a N size min-heap
        '''
        word = tup.values[0]
        count = tup.values[1]

        self._topN[word]=count
        self._len +=1

        if self._len>10:
            key_to_delete = max(self._topN, key=lambda k: d[k])
            del self._topN[key_to_delete]
        
        outtopN = "topN"
        values= ""

        for i in self._topN.keys():
            values = values + "," + "i"
         
        storm.emit([outtopN,values])

        pass
        # End


# Start the bolt when it's invoked
TopNFinderBolt().run()
