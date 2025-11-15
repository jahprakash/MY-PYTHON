class encap:
  def __init__(self):
    self.public=100
    self.__private=10
  def get_private(self):
    return self.__private
obj=encap()
print(obj.public)
print(obj.get_private())
