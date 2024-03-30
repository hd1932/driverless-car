import util, collections

# Class: Learner
# ---------------
# This class is in charge of observing cars drive around and figuring out a
# probability distribution over transitions that cars make.
class Learner(object):
    
    # Function: Init
    # ---------------
    def __init__(self):
        self.transitions = dict() # oldTile --> counter newTile

    # Function: Note Car Mode
    # ----------------------
    # This function is called once for each car on every heart beat of the
    # program. OldPos was the old position of the car and newPos is the position
    # of the car after the heartbeat. The code takes these positions
    # and extracts the corresponding tiles. Updates any relevant variables with
    # this new datapoint.
    def noteCarMove(self, oldPos, newPos):
        oldRow, oldCol = util.yToRow(oldPos.y), util.xToCol(oldPos.x)
        newRow, newCol = util.yToRow(newPos.y), util.xToCol(newPos.x)
        oldTile = (oldRow, oldCol)
        newTile = (newRow, newCol)

        if oldTile in self.transitions:
            self.transitions[oldTile][newTile] += 1
        else:
            self.transitions[oldTile] = collections.Counter()
            self.transitions[oldTile][newTile] = 1
        
        
    # Function: Save Transition Prob
    # ------------------------------
    # After the algorithm has finished running, saveTransitionProb is called.
    # Puts any relevant data you have into the transProb dictionary and calls
    # util.saveTransProb. 
    def saveTransitionProb(self, transFile):
        transProb = {}

        # transProb is a dict {(oldTile, newTile) : prob}
        # First normalize the counters
        for oldTile in self.transitions:
            counter = self.transitions[oldTile]
            s = float(sum(counter.values()))
            for key in counter:
                counter[key] /= s
        for oldTile in self.transitions:
            for newTile in self.transitions:
                transProb[(oldTile, newTile)] = self.transitions[oldTile][newTile]
        
        util.saveTransProb(transProb, transFile) ### COMMENTED SO THAT WE DO NOT OVERRIDE ANY LEARNED PROBABILITIES
        
