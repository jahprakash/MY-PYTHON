#single inheritance
class home:
  def function(Self):
    print("am going to home")
class sweethome:
  def function(self):
    print("am not going to home")
obj=home()
bad=sweethome()
obj.function()
bad.function()
