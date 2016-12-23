from context  import http_monitoring
import datetime

class TestParser:
  @staticmethod
  def test_parse():
    log_string = '127.0.0.1 paul - [22/Dec/2016:18:02:25 +0000] "POST / HTTP/1.0" 404 1895'
    results = http_monitoring.Parser.parse_w3c(log_string)
    if (results['host'] == '127.0.0.1'
        and results['path'] == '/'
        and results['bytes'] == 1895
        and results['date'] == int(datetime.datetime(2016,12,22,18,2,25).timestamp())):
      return True
    return False
