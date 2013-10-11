from scipy import stats
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import sys

class Compartment_fft(object):
    """
    Make compartment with single profile using FFT to convolve during calculation of concentration
    """
    def __init__(self,name):
        self.name = name
        self.successors = {}
        self.predecessors = {}
        self.concentartion = []
        self.pdf = stats.gamma.pdf
        self.time = np.arange(0,10,1)
        self.treshold = 1

        self.i=0
    def __call__(self):     
        #Calculate concentration in compartment   
        inputs = np.sum([pred.concentration*weight for pred,weight in self.predecessors.items()],axis=0)
        inputs_fft = np.fft.fft(inputs,self.fsize)
        print inputs_fft

        newconc = np.fft.ifft(inputs_fft * self.profile_fft).real[:self.time.__len__()]
        diff = np.allclose(self.concentration, newconc,rtol=0.2)
        self.concentration = newconc
        if not diff:
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
        """
        Adding successor to compartment(and compartment to successor predecessors list). 
        
        compartment should be instance of Compartment class.
        weight is the ratio compartment flow to the whole successor's income flow
        """
        if weight<0 or weight>1:
            raise ValueError
        self.successors[compartment]=weight
        compartment.predecessors[self]=weight

    def set_time(self,duration,resolution):

        self.time=np.arange(0,duration,resolution)
        self.fsize= int(2 ** np.ceil(np.log2( self.time.__len__()*2-1 )))
        print self.fsize
    def add_predecessor(self,compartment,weight=1):
        
        self.predecessors[compartment]=weight
        compartment.successors[self]=weight

    def reset_concentration(self):
        self.concentration=np.zeros(self.time.__len__())

    def make_delta(self):
        """
        attrs:
        a - amp
        loc - duration
        scale - delay
        """
        self.concentration=np.zeros(self.time.__len__())
        self.concentration[int(self.scale / self.time[1]) : int(self.loc / self.time[1]) ]=self.a

    def make_profile(self):
        # Make PDF of compartment transit times
        self.profile = self.pdf(self.time, self.a, self.loc, self.scale)
        self.profile /= np.sum(self.profile)
        self.profile_fft=np.fft.fft(self.profile,self.fsize)
        self.concentration = np.zeros( self.time.__len__() )
    def plot(self,color=''):
        plt.plot(self.time,self.concentration,'%s'%color)