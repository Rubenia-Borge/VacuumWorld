import numpy as np


class Agent():
    '''Template for Agent class. Uncallable'''
    def __init__(self, start_loc, home_loc, start_face):
        self.bump = False
        self.dirty = False
        self.home = False
        self.loc = start_loc
        self.home_loc =home_loc
        self.bearing = self.__bearing__(start_face)
        self.percept_sequence = []
        self.action = 'powerup'

    def __bearing__(self, face):
        '''Converts an alphanumeric bearing into a coordinate'''
        return (np.array([-1,0]) if face=='N'
            else np.array([1,0]) if face=='S'
            else np.array([0,1]) if face=='E'
            else np.array([0,-1]))

    def get_percept(self, state):
        '''
        Sets conditions for when each of three onboard detectors should be set
        to 1
        '''
        self.bump = False
        self.dirty = False
        self.home = False
        print self.loc + self.bearing
        if (min(self.loc + self.bearing) < 0
                or min(state.shape - self.loc - self.bearing) == 0
                or state[self.loc[0] + self.bearing[0],
                            self.loc[1] + self.bearing[1]] == 2):
            self.bump = True
        if state[self.loc[0], self.loc[1]] == 1:
            self.dirty = True
        # determine if vacuum is in home loc
        if (self.loc-self.home_loc).sum() == 0:
            self.home = True
        print (self.bump, self.dirty, self.home)
        self.percept_sequence.append((self.bump, self.dirty, self.home))


class TrivialTableLookupAgent(Agent):
    ''' An Agent class that stores instructions in a table'''
    def program(self):
        if self.percept_sequence[-1][1]==True:
            self.action = 'suck'
        elif self.percept_sequence[-1][2]==True and (len(self.percept_sequence)>2):
            self.action = 'powerdown'
        elif (len(self.percept_sequence)
                - sum([percept[1] for percept in self.percept_sequence])
                )% 2 == 1:
            self.action = 'move'
        else:
            self.action = 'rturn'
        print self.action


class BasicReflexAgent(Agent):
    ''' An Agent class that responds to its immediate environment'''
    def program(self):
        if self.dirty==True:
            self.action = 'suck'
        elif self.bump==True:
            do = 100*np.random.random()
            if do < 49:
                self.action = 'rturn'
            elif do < 98:
                self.action = 'lturn'
            else:
                self.action = 'powerdown'
        else:
            do = 100*np.random.random()
            if do < 50:
                self.action = 'move'
            elif do < 74:
                self.action = 'rturn'
            elif do < 98:
                self.action = 'rturn'
            else:
                self.action = 'powerdown'
        print self.action


class InternalStateReflexAgent(Agent):
    ''' An Agent class that responds to its immediate environment'''
    def program(self):
        if self.dirty==True:
            self.action = 'suck'
        elif self.bump==True:
            do = 100*np.random.random()
            if do < 49:
                self.action = 'rturn'
            elif do < 98:
                self.action = 'lturn'
            else:
                self.action = 'powerdown'
        else:
            do = 100*np.random.random()
            if do < 50:
                self.action = 'move'
            elif do < 74:
                self.action = 'rturn'
            elif do < 98:
                self.action = 'rturn'
            else:
                self.action = 'powerdown'
        print self.action
