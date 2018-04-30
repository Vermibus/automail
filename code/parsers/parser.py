

class ParserAbstractClass():

  def __init__(self):
    raise NotImplementedError

  def __str__(self):
    raise NotImplementedError

  def parse(self):
    raise NotImplementedError

  def getId(self):
    if self.item_name:
      return sum( [ord(char)**i for i,char in enumerate(self.item_name)] )
    else:
      print('Run parser.parse() first!')
      raise NotImplementedError

  def getVariables(self):
    return {
      'item_name':self.item_name,
      'old_price':self.old_price,
      'new_price':self.new_price,
      'dif_price':self.old_price-self.new_price,
      'item_link':self.item_link,
      'item_image':self.item_image,
      'item_specification':self.item_specification,
    }
