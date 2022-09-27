class Math:

  def add(a, b):
    return a+b
  
  def sub(a, b):
    return a-b  
  
  def mul(a, b):
    return a*b
  
  def div(a, b):
    return a/b


class testMath:

  def test_add(self):
    self.assertEquals(Math.add(1, 2), 3)
    
  def test_sub(self):
    self.assertEquals(Math.sub(3, 2), 1)
  
  def test_mul(self):
    self.assertEquals(Math.mul(1.5, 2), 3)
  
  def test_div(self):
    self.assertEquals(Math.div(3, 2), 1.5)