import turtle
"""
Function: A simple physics program that will calculate and display
the resultant vector between two vectors. A resultant vector is
the vector that is produced after adding two vectors. It will
show in what direction and magnitude force will be applied.
"""


print("Let's Rock!")

def calculate_resultant_vector(vectors):
    print("calculating")
    delta_x = int(vectors[0][0])+int(vectors[1][0])
    delta_y = int(vectors[0][1])+int(vectors[1][1])

    resultant_vector = f"{delta_x},{delta_y}"

    return resultant_vector


def acquire_vectors():
    vector_a_str = input("Please provide me a vector. Ex: 1,2 \n")
    vector_b_str = input("Please provide me another vector. Ex: 1,2 \n")
    list_of_vectors = []

    try:
        vector_a = vector_a_str.split(",")
        vector_b = vector_b_str.split(",")

        list_of_vectors.append(vector_a)
        list_of_vectors.append(vector_b)
    except:
        print("Error")


    return list_of_vectors


def simulation():
    list_of_vectors = acquire_vectors()
    resultant_vector = calculate_resultant_vector(list_of_vectors)

    print(resultant_vector)

    vector_a_x = int(list_of_vectors[0][0])*100
    vector_a_y = int(list_of_vectors[0][1])*100
    vector_b_x = int(list_of_vectors[1][0])*100
    vector_b_y = int(list_of_vectors[1][1])*100
    vector_resultant_str = resultant_vector.split(",")
    vector_resultant_x = int(vector_resultant_str[0])*100
    vector_resultant_y = int(vector_resultant_str[1])*100


    #Instantiate turtle objects
    vector_a = turtle.Turtle()
    vector_b = turtle.Turtle()
    vector_resultant = turtle.Turtle()

    #Alter attr
    vector_a.pensize(8)
    vector_b.pensize(8)
    vector_resultant.pensize(8)
    vector_a.color("blue")
    vector_b.color("blue")
    vector_resultant.color("red")

    #Hide the arrows on the turtle objects
    vector_a.hideturtle()
    vector_b.hideturtle()
    vector_resultant.hideturtle()

    #Display the vectors on screen
    vector_a.setposition(vector_a_x, vector_a_y)
    vector_b.setposition(vector_b_x, vector_b_y)
    print(vector_resultant_x, vector_resultant_y)
    vector_resultant.setposition(vector_resultant_x,vector_resultant_y)



#Tkinter Setup
session = turtle.Screen()
cartesian_x = turtle.Turtle()
cartesian_y = turtle.Turtle()
cartesian_x.pensize(5)
cartesian_y.pensize(5)

cartesian_x.hideturtle()
cartesian_y.hideturtle()
cartesian_x.speed(10)
cartesian_y.speed(10)

cartesian_x.setposition(1000,0)
cartesian_x.setposition(-1000,0)
cartesian_y.setposition(0,1000)
cartesian_y.setposition(0,-1000)


session.setup(width=1200, height=1200, startx=0, starty=0)



#Kick off main function
simulation()

session.exitonclick()

turtle.done()



