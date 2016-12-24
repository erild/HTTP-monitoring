import datetime

class Data:
  def __init__(self):
    self.path_10s = {}
    self.traffic_10s = 0
    self.ips_10s = {}
    self.hits_2min = 0
    self.times_2min = {}

  def update_10s(self, log_data):
    self.path_10s[log_data['path']] = self.path_10s[log_data['path']] + 1 if log_data['path'] in self.path_10s else 1
    self.ips_10s[log_data['host']] = self.ips_10s[log_data['host']] + 1 if log_data['host'] in self.ips_10s else 1
    self.traffic_10s += log_data['bytes']

  def clean_10s(self):
    self.path_10s = {}
    self.ips_10s = {}
    self.traffic_10s = 0

  def update_2min(self, log_data):
    self.times_2min[log_data['date']] = self.times_2min[log_data['date']] +1 if log_data['date'] in self.times_2min else 1
    self.hits_2min += 1

  def clean_2min(self,last_date):
    for time_2m in list(self.times_2min.keys()):
      if time_2m + 120 <= last_date:
        self.hits_2min -= self.times_2min[time_2m]
        self.times_2min.pop(time_2m)

  def insert_data(self, log_data):
    self.update_10s(log_data)
    self.update_2min(log_data)

  def get_10s_data(self):
    return {'path': self.path_10s, 'traffic': self.traffic_10s, 'ips': self.ips_10s}

  def get_2m_hits(self):
    return self.hits_2min