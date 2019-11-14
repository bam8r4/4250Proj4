#Author of this code: Brent Moran
#Program written to show polymorhpism and inheritance in python.


#Parent class definition.
class Product:
    
    #Constructor to assign values to data memebers. 
    def __init__(self, name, price, discountPercent):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent
    
    #Function to return the amount of the discount.    
    def getDiscountAmount(self):
        return(self.discountPercent * self.price)
    
    #Function to return price of the product after discount is applied.     
    def getDiscountPrice(self):
        return((1 - self.discountPercent) * self.price)
     
    #Print out information related to the product.    
    def printDescription(self):
        
        message = "The product name is " + self.name + " the original price was $" + str(self.price) + ", the discount is $"
        message += str(round(self.getDiscountAmount(),2)) + ", and the new price is $"
        message += str(round(self.getDiscountPrice(),2)) + "."
        print(message)
        
#We are making a subclass of the  superclass product. 
class Book(Product):
    def __init__(self, name, price, discountPercent, author):
        self.author = author
        
        #Initializing attributes of the parent class. 
        super().__init__(name, price, discountPercent)

    def printDescription(self):
        
        message = "The book is " + self.name + " written by " + self.author 
        message +=", the original price was $" + str(self.price) + ", the discount is $"
        message += str(round(self.getDiscountAmount(),2)) + ", and the new price is $"
        message += str(round(self.getDiscountPrice(),2)) + "."
        print(message)
        #print("This is a polymorphic function.")

#We are making a subclass of the superclass prduct.        
class Movie(Product):
    def __init__(self,name, price, discountPercent, year):
        
        self.year = year
        
        #We are initializing the attributes of the parent class. 
        super().__init__(name, price, discountPercent)
        
    def printDescription(self):
        
        message = "The movie is " + self.name + ", which was released in " + str(self.year)
        message += ". The original price was $" + str(self.price) + ", the discount is $"
        message += str(round(self.getDiscountAmount(),2)) + ", and the new price is $"
        message += str(round(self.getDiscountPrice(),2)) + "."
        print(message)


#Instantiation of classes and sub classes. 
x = Product("Printer Paper", 4.95, 0.60)
y = Book("Harry Potter", 9.95, 0.75, "J.K. Rowling")
z = Movie("Titanic", 19.95 ,0.30, "1997")

#Printing descriptions for both the super and subclasses instantiated above. 
x.printDescription()
y.printDescription()
z.printDescription()





