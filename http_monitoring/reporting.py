

class Reporting:
  def __init__(self):
    self.alert_history = []
    self.alert_current = []

  def print_report(self, data):
    report = ""
    report_10s = data.get_10s_data()
    print(report_10s)
    if report_10s["path"]:
      report += "Most visited section: \n"
      best_paths = sorted(report_10s['path'], key=report_10s['path'].get, reverse=True)
      for path in best_paths:
        report += "    {0} -> {1} hits".format(path, report_10s['path'][path])
    if report_10s["ips"]:
      report += "Most active user: \n"
      best_users = sorted(report_10s['ips'], key=report_10s['ips'].get, reverse=True)
      for user in best_users:
        report += "    {0} -> {1} hits".format(user, report_10s['ips'][user])
    report += "Total Traffic: {0}\n".format(report_10s['traffic'])
    print(report)