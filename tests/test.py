from GenerateLog import GenerateLog
from parser_test import TestParser
from context import http_monitoring
import sys
import _thread

class TestScenario:
  def __init__(self):
    if TestParser.testParse():
      print('parser ok')
    else:
      print("Error with parser")
      sys.exit(2)
    self.logGenerator = GenerateLog('test.log')
    argv = ['-i', 'test.log', '-l', '400']
    self.cli = http_monitoring.Cli(argv)

  def runAlertScenario(self):
    try:
      _thread.start_new_thread( self.runLogGeneratorForAlert, ())
    except Exception as e:
      print("Cannot start thread")
    self.cli.run()

  def runLogGeneratorForAlert(self):
    self.logGenerator.run(80, 2)
    self.logGenerator.run(60, 8)
    self.logGenerator.run(120, 2)

test = TestScenario()
test.runAlertScenario()