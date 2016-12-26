from .alert import Alert
import datetime
# Print the report
class Reporting:
  def __init__(self, threshold):
    self.alert_history = []
    self.alert_current = {}
    self.alert = Alert(threshold)

  def report(self, data):
    self.printReport(data)
    self.printAlertHistory()
    self.printAlert(data)

  def printReport(self, data):
    report = "---------------------------------\n"
    report += "Report at {0}\n".format(datetime.datetime.now().strftime('[%d/%b/%Y:%H:%M:%S %z]'))
    report_10s = data.get_10s_data()
    if report_10s["path"] and report_10s["ips"]:
      report += "Most visited section: \n"
      best_paths = sorted(report_10s['path'], key=report_10s['path'].get, reverse=True)[:2]
      for path in best_paths:
        report += "    {0} -> {1} hits\n".format(path, report_10s['path'][path])
      report += "Most active user: \n"
      best_users = sorted(report_10s['ips'], key=report_10s['ips'].get, reverse=True)[:2]
      for user in best_users:
        report += "    {0} -> {1} hits\n".format(user, report_10s['ips'][user])
      report += "Total Traffic: {0}\n".format(report_10s['traffic'])
    else:
      report += "Nothing happened\n"
    print(report)

  def printAlert(self,data):
    hits_2m = data.get_2m_hits()
    alert_result = self.alert.process(hits_2m)
    if alert_result['status'] == 'Start':
      self.alert_current = {'start': datetime.datetime.now().strftime('%d/%b/%Y:%H:%M:%S'), 'hits': hits_2m}
      print("\033[93m High traffic generated an alert: {0} hits triggered at {1} \033[0m\n".format(hits_2m, self.alert_current['start']))
    elif alert_result['status'] == 'Continue':
      self.alert_current['hits'] = hits_2m if self.alert_current['hits'] < hits_2m else self.alert_current['hits']
      # report += "High traffic generated an alert: maximum of {0} hits triggered at {1}\n".format(self.alert_current['hits'], self.alert_current['start'])
    elif alert_result['status'] == 'Stop':
      self.alert_current['stop'] = datetime.datetime.now().strftime('%d/%b/%Y:%H:%M:%S')
      print("\033[92m Recover from high traffic: {0} max hits started on {1}, finished on {2} \033[0m\n".format(self.alert_current['hits'], self.alert_current['start'], self.alert_current['stop']))
      self.alert_history.append(self.alert_current)
      self.alert_current = {}

  def printAlertHistory(self):
    report = ""
    if self.alert_history:
      report += "Past Alert:\n"
      for alert in self.alert_history:
        report += "  From {0} to {1}, alert due to traffic reaching {2}\n\n".format(alert['start'], alert['stop'], alert['hits'])

    if self.alert_current:
      report += "\033[93m High traffic generated an alert: maximum of {0} hits triggered at {1} \033[0m\n".format(self.alert_current['hits'], self.alert_current['start'])

    print(report)
