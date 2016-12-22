import re
import datetime

class Parser:
  # Host User Name Date Req_type path protocol Status Size
  W3C_PATTERN = '^(.+)\s(.+)\s(.+)\s\[(.+)\]\s"(\w+)\s(/[^/]*).*\s(.+)"\s(\d+)\s(\d+|-)$'
  DATE_PATTERN = '^(\d+)/(\w+)/(\d+):(\d+):(\d+):(\d+) (.....)$'

  MONTHS = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}


  @staticmethod
  def parse_w3c(line):
    matches = re.match(Parser.W3C_PATTERN, line)
    result = {}
    result['host'] = matches.group(1)
    result['user'] = matches.group(2)
    result['date'] = Parser.parse_date(matches.group(4))
    result['path'] = matches.group(6)
    result['bytes'] = int(matches.group(9))
    return result

  @staticmethod
  def parse_date(date_str):
    date_matches = re.match(Parser.DATE_PATTERN, date_str)
    return datetime.datetime(int(date_matches.group(3)), int(Parser.MONTHS[date_matches.group(2)]), int(date_matches.group(1)), int(date_matches.group(4)), int(date_matches.group(5)), int(date_matches.group(6)))
