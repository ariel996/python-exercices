class Batiment():
  def __init__(self, adresse):
    self.adresse = adresse
    
  def getAdresse(self):
    return self.__adresse 
  
  def setAdresse(self,adresse):
    self.__adresse = adresse
    
  def __str__(self) :
    return f"adresse : {self.adresse}"
  
  
class Maison(Batiment):
  def __init__(self, adresse, nbPieces):
    super().__init__(adresse)
    self.nbPieces = nbPieces
    
  def getNbPieces(self):
    return self.__nbPieces 
  
  def setNbPieces(self, nbPieces):
    self.__nbPieces = nbPieces 
    
  def __str__(self) :
    return f"{super().__str__()}, nbPieces : {self.nbPieces}"
    
    
class Immeuble(Maison):
  def __init__(self, adresse, nbPieces, nbAppart):
    super().__init__(adresse, nbPieces)
    self.nbAppart = nbAppart
    
  def getNbAppart(self):
    return self.__nbAppart 
  
  def setNbAppart(self,nbAppart):
    self.__nbAppart = nbAppart 
    
  def __str__(self) :
    return f"{super().__str__()}, nbAppart : {self.nbAppart}"


b = Batiment("Morocco")
print(b)

m = Maison("Morocco", 3)
print(m)

i = Immeuble("Morocco", 3, 15)
print(i)