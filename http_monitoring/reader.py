from .parser import Parser
# Read data from a w3c-compliant log
class Reader:
  def __init__(self, file):
    self.fileHandle = open(file, 'r')
    self.fileHandle.seek(0, 2)

  def getData(self):
    data = []
    line = self.fileHandle.readline()
    while line:
      data.append(Parser.parse_w3c(line))
      line = self.fileHandle.readline()
    return data
