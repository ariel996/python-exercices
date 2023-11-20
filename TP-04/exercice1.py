class Point:  
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def getX(self):
    return self.__x
  
  def getY(self):
    return self.__x
  
  def setX(self,a):
    self.__x = a
    
  def setY(self,b):
    self.__y = b
  
  def __str__(self):
    return f"p=({self.x}, {self.y})"


class Rectangle(Point):
  def __init__(self, x, y, longueur, largeur):
    super().__init__(x,y)
    self.longueur = longueur
    self.largeur = largeur

  def getLongeur(self):
    return self.__longueur

  def getLargeur(self):
    return self.__largeur
  
  def setLongeur(self, value):
    self.__longueur = value
    
  def setLargeur(self, value):
    self.__largeur = value
  
  def aire(self):
    return self.longueur * self.largeur 
  
  def __str__(self):
    return f"{super().__str__()} , r=({self.longueur}, {self.largeur})"


class Parallelepipede(Rectangle):
  def __init__(self, x, y, longueur, largeur, hauteur):
    super().__init__(x, y, longueur, largeur)
    self.hauteur = hauteur
    
  def getHauteur(self):
    return self.__hauteur
  
  def setHauteur(self,hauteur):
    self.__hauteur = hauteur

  def aire(self):
    return 2 * (self.longueur * self.largeur + self.longueur * self.hauteur + self.largeur * self.hauteur)

  
  def volume(self):
    return self.longueur * self.largeur * self.hauteur

  
  def __str__(self):
    return f"{super().__str__()} ,  h={self.hauteur})"
    


point = Point(1, 2)
print(point)

rectangle = Rectangle(3, 4, 5, 6)
print(rectangle)
print(rectangle.aire())


parallepipede = Parallelepipede(1, 2, 3, 4, 5)
print(parallepipede)
print(parallepipede.aire())
print(parallepipede.volume())