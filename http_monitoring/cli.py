from .reader import Reader
from .data import Data
import time

class Cli:
  def __init__(self, args):
    self.reader = Reader(args['logfile'])
    self.data = Data()

  def run(self):
    while True:
      self.data.clean_10s()
      for log_data in self.reader.getData():
        self.data.insert_data(log_data)
      time.sleep(10)