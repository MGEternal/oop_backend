
class Product:
    def __init__(self,id,name,price,description,image,qty,last_update):
      self.__id = id
      self.__name = name
      self.__price = price
      self.__description = description
      self.__image = image
      self.__qty = qty
      self.__last_update = last_update
      
    @property
    def id(self):
          return self.__id
        
    @property
    def name(self):
          return self.__id


#############################################################   Keyboard inherite form product #########################################################

class Keyboard(Product):
  def __init__(self, id, name, price, description, image, qty, last_update, version, type, switches, color):
    super().__init__(id, name, price, description, image, qty, last_update)
    self.__version = version
    self.__type = type
    self.__switches = switches
    self.__color = color
    
  @property
  def id(self):
      return self._Product__id
  
  @property
  def name(self):
      return self._Product__name

############################################################# Mouse ###########################################################

class Mouse(Product):
      def __init__(self, id, name, price, description, image, qty, last_update, connection, color):
        super().__init__(id, name, price, description, image, qty, last_update)
        self.__connection = connection
        self.__color = color
      
      @property
      def id(self):
          return self._Product__id

      @property
      def name(self):
        return self._Product__name

########################################################### Switch ########################################

class Switch(Product):
      def __init__(self, id, name, price, description, image, qty, last_update, option, quantity_set):
        super().__init__(id, name, price, description, image, qty, last_update)
        self.__option = option
        self.__quantity_set = quantity_set
       
      @property 
      def id(self):
        return self._Product__id
      
      @property
      def name(self):
        return self._Product__name
  ########################################################### Keycap ########################################

class Keycap(Product):
      def __init__(self, id, name, price, description, image, qty, last_update, version, color):
        super().__init__(id, name, price, description, image, qty, last_update)
        self.__version = version
        self.__color = color
        
      @property 
      def id(self):
        return self._Product__id
      
      @property
      def name(self):
        return self._Product__name
  