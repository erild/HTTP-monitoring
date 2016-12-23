import datetime

class Data:
  def __init__(self):
    self.path_10s = {}
    self.traffic_10s = 0
    self.ips_10s = {}
    self.hits_2min = 0
    self.times_2min = {}

  def update_10s(self, log_data):
    self.path_10s[log_data['path']] += 1 if log_data['path'] in self.path_10s else self.path_10s[log_data['path']] = 1
    self.ips_10s[log_data['host']] += 1 log_data['host'] in self.path_10s else self.ips_10s[log_data['host']] = 1
    self.traffic_10s += log_data['bytes']

  def clean_10s(self):
    self.path_10s = {}
    self.ips_10s = {}
    self.traffic_10s = 0

  def update_2min(self, log_data):
    self.times_2min.append(log_data['date'])
    self.hits_2min += 1

  def clean_2min(self):
    for time_2m, time_hits in self.times_2min:
      if time_2m + 120 > int(datetime.datetime.now().timestamp()):
        self.hits_2min -= time_hits
        self.times_2min.pop(time_2m)

  def insert_data(self, log_data):
    self.clean_2min()
    self.update_10s(log_data)
    self.update_2min(log_data)

  def get_10s_data(self):
    return {'path': self.path_10s, 'traffic': self.traffic_10s, 'ips': self.ips_10s}