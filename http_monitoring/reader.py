from .parser import Parser

class Reader:
  def __init__(self, file):
    try:
      self.fileHandle = open(file, 'r')
    except IOError:
      print("Could not open file!")
    self.fileHandle.seek(0, 2)

  def getData(self):
    data = []
    line = self.fileHandle.readline()
    while line:
      data.append(Parser.parse_w3c(line))
      line = self.fileHandle.readline()
    return data
