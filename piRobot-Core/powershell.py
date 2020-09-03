import datetime
import sys
import time
import numpy
#import talib
import timeit
import json
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)





size = 1000
p = 100
o = numpy.random.random(size)
h = numpy.random.random(size)
l = numpy.random.random(size)
c = numpy.random.random(size)
v = numpy.random.random(size)

def get_indicators(values):
    # Return the RSI of the values sent from node.js
    #numpy_values = numpy.array(values, dtype=numpy.double) 
    return 'abc'

class HelloRPC:

  # Initializer / Instance Attributes
  def __init__(self):
     self.counter = 0
     
  def fcCall(self, input):
      self.counter=self.counter+1
      return self.counter

rpc = HelloRPC()


for line in sys.stdin:
   # l = json.loads(line)
    print(rpc.fcCall('sachs'))
    # Without this step the output may not be immediately available in node
    sys.stdout.flush()