# basic starter code for a class that can be expanded to handle callbacks, attachents (buttons, etc) and more!
class Slash():

  def __init__(self, message):
    self.msg = message

  def getMessage(self):
      return self.msg
