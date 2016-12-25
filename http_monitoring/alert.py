
# Process the alert state
class Alert:
  def __init__(self, threshold):
    self.threshold = threshold
    self.status = False

  def process(self, hits):
    if self.status:
      if hits < self.threshold:
        self.status = False
        return self.stopAlarm(hits)
      return self.continueAlarm(hits)
    else:
      if hits > self.threshold:
        self.status = True
        return self.triggerAlarm(hits)
      return {'status': 'None'}


  def triggerAlarm(self, hits):
    return {'status': 'Start', hits: hits}

  def stopAlarm(self, hits):
    return {'status': 'Stop', hits: hits}

  def continueAlarm(self, hits):
    return {'status': 'Continue', hits: hits}