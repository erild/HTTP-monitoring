from .reader import Reader
from .data import Data
from .reporting import Reporting
import datetime, time
import sys, argparse

# launch the event loop and the programm
class Cli:
  def __init__(self, argv):
    # Get command line argument
    parser = argparse.ArgumentParser(description='Display monitoring alert for web traffic')
    parser.add_argument("-i", dest="logfile", required=True,)
    parser.add_argument("-l", dest="limit", required=True, type=int)
    args = parser.parse_args()

    try:
      self.reader = Reader(args.logfile)
    except IOError:
      print("Cannot open file: {0}".format(args.logfile))
      sys.exit(2)
    self.reporter = Reporting(args.limit)
    self.data = Data()

  def run(self):
    report_time = int(datetime.datetime.now().timestamp()) + 10
    while True:
      try:
        for log_data in self.reader.getData():
          self.data.insert_data(log_data)
      except Exception as e:
        print("{0}: Error: {1}\n".format(e.args[0], e.args[1]))
      # When time, print the report and clean the data
      if(int(datetime.datetime.now().timestamp()) >= report_time):
        self.reporter.report(self.data)
        self.data.clean_10s()
        self.data.clean_2min(report_time)
        report_time +=10
      time.sleep(1)