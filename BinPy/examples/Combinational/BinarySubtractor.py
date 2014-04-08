from __future__ import print_function
from BinPy.Combinational.combinational import *
""" Examples for BinarySubtractor class """
print ("\n---Initializing the BinarySubtractor class--- ")
print (
    "\n---Input is of the form ([Binary number 1],[ Binary number 2], Carry]")
print ("bs = BinarySubtractor([0, 1], [1, 0], 0)")
bs = BinarySubtractor([0, 1], [1, 0], 0)
print ("\n---Output of BinarySubtractor")
print ("bs.output()")
print (bs.output())
print("Output is of the form [ [Difference], Borrow]")
print ("\n---Input changes---")
print ("bs.setInput(1, [0]) #Input at index 1 is changed to 0")
bs.setInput(1, [0])
print ("\n---New Output of the BinarySubtractor---")
print (bs.output())
print ("\n---Changing the number of inputs---")
print ("No need to set the number, just change the inputs")
print ("Input length must be three")
print ("bs.setInputs(1, 0, 1)")
bs.setInputs([1], [0], 1)
print ("\n---To get the input states---")
print ("bs.getInputStates()")
print (bs.getInputStates())
print ("\n---New output of BinarySubtractor---")
print (bs.output())
print ("\n\n---Using Connectors as the input lines---")
print ("Take a Connector")
print ("conn = Connector()")
conn = Connector()
print ("\n---Set Output of Binary Subtractor to Connector conn---")
print ("bs.setOutput(0, conn) # sets the conn at index 0 ")
bs.setOutput(0, conn)
print ("\n---Put this connector as the input to gate1---")
print ("gate1 = AND(conn, 0)")
gate1 = AND(conn, 0)
print ("\n---Output of the gate1---")
print ("gate1.output()")
print (gate1.output())
print ("Information about bs instance can be found by")
print ("bs")
print (bs)
