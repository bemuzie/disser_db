from scipy import stats
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(50000)
class Compartment_fft(object):
    def __init__(self,name):
        self.name = name
        self.successors = {}
        self.predecessors = {}
        self.pdf = stats.gamma.pdf
        self.treshold = 0.0000001
        

        self.i=0
    def __call__(self):
        
        inputs = np.sum([pred.concentration*weight for pred,weight in self.predecessors.items()],axis=0)
        newconc = signal.fftconvolve(self.profile, inputs)[:self.time.__len__()]
        diff = self.concentration - newconc
        self.concentration = newconc
        
        if np.sum(diff*diff)>self.treshold:
            for s in self.successors:
                s()

    def __repr__(self):
        output = self.name + '\n'
        for pred in self.predecessors:
            output += '  - ' + pred.name + " : " + str(self.predecessors[pred])+'\n'
        return output
    def set_attrs(self,*args):
        self.a, self.loc, self.scale = args
        
    def add_successor(self,compartment,weight=1):
        self.successors[compartment]=weight
        compartment.predecessors[self]=weight

    def set_time(self,duration,resolution):
        self.time=np.arange(0,duration,resolution)

    def add_predecessor(self,compartment,weight=1):
        self.predecessors[compartment]=weight
        compartment.successors[self]=weight

    def reset_concentration(self):
        self.concentration=np.zeros(self.time.__len__())

    def make_delta(self):
        #attrs:
        #a - amp
        #loc - duration
        #scale - delay
        self.concentration=np.zeros(self.time.__len__())
        self.concentration[int(self.scale / self.time[1]) : int(self.loc / self.time[1]) ]=self.a
        self.profile=np.zeros(self.time.__len__())

    def make_profile(self):
        # Make PDF of compartment transit times
        self.profile = self.pdf(self.time, self.a, self.loc, self.scale)
        self.profile /= np.sum(self.profile)
        self.concentration = np.zeros( self.time.__len__() )
    def plot(self,color=''):
        plt.plot(self.time,self.concentration,'%s'%color)