#class for writing w3c log file
from random import randint
import datetime
import time

class GenerateLog:

  def __init__(self, logfile):
    try:
      self.logfileHandle = open(logfile, 'a')
    except IOError:
      print("Could not open file!")

    self.ips = ['127.0.0.1', '127.0.0.2', '127.0.0.3']
    self.names = ['tom', 'paul', 'pierre', '-']
    self.user = ['tom', 'paul', 'pierre', '-']
    self.methods = ['POST', 'HEAD', 'PUT', 'DELETE', 'TRACE', 'CONNECT']

    self.path = ['/', '/home','/user','/admin']
    self.protocols = ['HTTP/1.0', 'HTTP/1.1']
    self.status = ['200', '404', '403']

  def __del__(self):
    self.logfileHandle.close()

  def run(self, duration):
    start = time.time()
    while start + duration > time.time():
      self.logfileHandle.write(self.generateLine())
      self.logfileHandle.flush()
      time.sleep(1)


  def generateLine(self):
    return "{0} {1} {2} {3} \"{4} {5} {6}\" {7} {8}\n".format(
      self.generateHost(),
      self.generateName(),
      self.generateUser(),
      self.generateDate(),
      self.generateMethods(),
      self.generatePath(),
      self.generateProtocol(),
      self.generateStatus(),
      self.generateByteLen()
      )

  def generateHost(self):
    return self.ips[randint(0, len(self.ips)-1)]

  def generateName(self):
    return self.names[randint(0, len(self.names)-1)]

  def generateUser(self):
    return self.user[randint(0, len(self.user)-1)]

  def generateDate(self):
    return datetime.date.today().strftime('[%d/%b/%Y:%H:%M:%S %z]')


  def generateMethods(self):
    return self.methods[randint(0, len(self.methods)-1)]

  def generatePath(self):
    return self.path[randint(0, len(self.path)-1)]

  def generateProtocol(self):
    return self.protocols[randint(0, len(self.protocols)-1)]

  def generateStatus(self):
    return self.status[randint(0, len(self.status)-1)]

  def generateByteLen(self):
    return randint(0, 10000)