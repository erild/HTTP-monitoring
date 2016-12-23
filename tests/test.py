from GenerateLog import GenerateLog
from parser_test import TestParser

if TestParser.test_parse():
  print('ok')

test = GenerateLog('file.log')
test.run(20)