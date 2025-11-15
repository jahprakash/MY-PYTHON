#multiple inheritance
class A :
  def draw1(self):
    print("good 1")
class B:
  def draw2(self):
    print("good 2")
class C(A,B):
  pass
obj=A()
obj1=B()
obj.draw1()
obj1.draw2()
