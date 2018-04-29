from parsers import hotshot


class Parser(hotshot.Parser):
  
  def __init__(self):
    super(Parser, self).__init__()
    self.url = 'https://al.to/'

  def __str__(self):
    return 'al.to_parser'
