import turtle


turtle.speed(20) 
''' Sets the turtle drawing speed to 20. '''
turtle.screensize(2500,2500, "#D3D3D3") 
''' Allocated the screensize '''

total_cake_height = 15 #setting initial cake height as table height is 15


#This function creates each layer in the for loop below.
def create_layer():
    
    global total_cake_height
    turtle.penup()
    turtle.goto(-(cakeWidth/2), total_cake_height)
    turtle.pencolor(layerFlav) # Takes the color we input in the desired flavor, for each layer.
    turtle.fillcolor(layerFlav) # same thing as above
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(cakeWidth)
    turtle.left(90)
    turtle.forward(layerHeight) # Takes the size of the cake according to the i value again, same thing as flavor Ex: when we input the height between (30-50)
    turtle.left(90)
    turtle.forward(cakeWidth) 
    turtle.left(90)
    turtle.forward(layerHeight)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
     
    total_cake_height += layerHeight # This is to note the total cake height so it adds each layer in order for us to draw the cirlce on top of the cake.
    
#This function draws the toppings on the cake.    
def cake_topping():    
    r_of_frosting = cakeWidth/16    
    
    turtle.goto(-((cakeWidth/2) + (r_of_frosting)) , total_cake_height)
    turtle.right(90)
    turtle.pencolor("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    
    ''' This draws the frosting on top of the cake '''
    for i in range(9):
        turtle.circle(r_of_frosting,180)
        turtle.right(180)
    turtle.end_fill()
    ''' This draws the circle on top of the cake'''
    turtle.penup()
    turtle.goto(0, total_cake_height)
    turtle.left(90)
    turtle.pendown()
    turtle.pencolor('#d20a2e')
    turtle.fillcolor('#d20a2e')
    turtle.begin_fill()
    turtle.circle(8)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
''' this function draws the window'''    
def window_draw():
    
    turtle.goto(200, 100)
    turtle.pensize(15)
    turtle.pencolor("white")
    turtle.fillcolor("sky blue")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(150)
    turtle.circle(90,180)
    turtle.forward(150)
    turtle.end_fill()
    turtle.pensize(8)
    turtle.penup()
    turtle.left(180)
    turtle.forward(150)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(180)
    turtle.penup()
    turtle.left(180)
    turtle.forward(60)
    turtle.right(120)
    turtle.pendown()
    turtle.forward(70)
    turtle.penup()
    turtle.left(180)
    turtle.forward(70)
    turtle.right(60)
    turtle.forward(30)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(90)
    turtle.left(180)
    turtle.forward(240)
    turtle.left(180)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(60)
    turtle.forward(70)
    turtle.left(180)
    turtle.forward(70)
    turtle.right(120)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(180)
    turtle.penup()
''' This function draws the table.'''    
def table_draw(length):
    
    turtle.pencolor(table_color)
    turtle.fillcolor(table_color)
    turtle.begin_fill()
    turtle.forward(length/2)
    turtle.left(180)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(15)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(15)
    turtle.end_fill()
    turtle.penup()
    
    #Legs on the right side
    leg_height = 0.6 * length
    turtle.pencolor(table_color)
    turtle.fillcolor(table_color)
    turtle.begin_fill()
    turtle.home()
    turtle.forward((length/2)-20)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(leg_height)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(leg_height)
    
    turtle.penup()
    turtle.left(90)
    turtle.forward(22)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(leg_height-10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(leg_height-10)
    
    turtle.penup()
    turtle.home()
    turtle.left(180)
    
    #legs on the left side
    turtle.forward((length/2)-20)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(leg_height)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(leg_height)
    
    turtle.penup()
    turtle.right(90)
    turtle.forward(22)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(leg_height-10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(leg_height-10)
    turtle.end_fill()
    turtle.penup()
    turtle.home()
''' This function draws the balloon.'''
def balloon_1():
    turtle.goto(-300,0)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(16)
    turtle.pendown()
    turtle.forward(84)
    turtle.right(90)
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.pencolor("black")
    turtle.circle(35)
    turtle.end_fill()
    turtle.penup()
''' This function draws the banner on top.'''
def banner():
    turtle.penup()
    turtle.goto(-100,200)
    turtle.pendown()
    turtle.fillcolor("Pink")
    turtle.begin_fill()
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()
    turtle.penup()
    ''' This part of the function creates the text Happy birthday and changes the font in the rectangle.'''
    turtle.goto(-90,235)
    turtle.color("White")
    turtle.write("Happy Birthday!", font=("Blackadder ITC", 20, "bold"))
    
    turtle.goto(-70,300)
    turtle.pendown()
    turtle.color("Black")
    turtle.fillcolor("violet")
    turtle.begin_fill()
    turtle.left(180)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(500)
    turtle.end_fill()
    turtle.penup()
    
    turtle.goto(60 ,300)
    turtle.pendown()
    turtle.color("Black")
    turtle.fillcolor("violet")
    turtle.begin_fill()
    turtle.left(180)
    turtle.forward(500)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(500)
    turtle.end_fill()
    turtle.penup()
    
''' Calls all the functions.'''
def main():
    table_draw(table_length)
    window_draw()
    turtle.pensize(0)
    cake_topping()
    balloon_1()
    banner()


"""Asks the user how many layers of cake they wish to have"""

print("---------------- TURTLE CAKE MAKER ----------------")
table_color = input("Enter your desired table color: ")
table_length = int(input("Enter desired length of table (200-500): "))
no_of_layers = int(input("How many layers would you like in your cake(1-4)?:  "))
cakeWidth = int(input("Enter width of desired cake(100-200): "))
layerHeight = ''
#variable to store height of a layer
layerFlav= ''
''' Same thing with the height '''

''' for loop is used here so that the code can run depending on the number of times the user chooses their layers, 
EX: if the user picks 2, then the code will run twice and ask for 2 different layers. '''


for i in range(no_of_layers):
    flavTemp = int(input(f"Enter (1-4) the desired flavor of layer {i+1} from the following options:"+ "\n"+ "1 -> Vanilla "+"\n"+"2 -> Chocolate"+ "\n"+ "3 -> Strawberry" +"\n"+ "4 -> Red Velvet" +"\n"+ 
                         "------------------------------------------------------------------------------"+ "\n"))
    heightTemp = int(input(f"Enter the desired height of layer {i +1} (30-50): "))
    print("------------------------------------------------------------------------------")
    
    #Settings colors for each flavor.
    if flavTemp == 1:
        layerFlav ='#F3E5AB'
        
    elif flavTemp == 2:
        layerFlav= "#352728"
        
    elif flavTemp == 3:
        layerFlav = "#F07173"
    
    elif flavTemp == 4:
        layerFlav = "#9c0000"
    
    else:
        continue
    ''' if the user has not entered 1 2 3 or 4 for the flavors, it will go back to the for loop because they entered because they entered a invalid number
    (continue just repeats the loop)
    '''
    layerHeight = heightTemp
    
    create_layer()

'''This function creates the cake.'''  
    

      


main()
turtle.penup()
turtle.home()


input("Your cake is loading.. Happy birthday!!")