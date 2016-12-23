from .reader import Reader
from .data import Data
from .reporting import Reporting
import time

class Cli:
  def __init__(self, args):
    self.reader = Reader(args['logfile'])
    self.data = Data()
    self.reporter = Reporting()

  def run(self):
    while True:
      self.data.clean_10s()
      for log_data in self.reader.getData():
        self.data.insert_data(log_data)
      self.reporter.print_report(self.data)
      time.sleep(10)