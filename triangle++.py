import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(3)  # Make the lines thicker

# Function to draw a single triangle
def draw_triangle(side_length, color):
    pen.color(color)
    for _ in range(3):
        pen.forward(side_length)
        pen.left(120)

# Function to draw the pattern of triangles
def draw_pattern():
    range_start = 50
    range_end = 100
    range_step = 10
    
    num_triangles = (range_end - range_start) // range_step
    for i in range(num_triangles):
        length = range_start + i * range_step
        color = colorsys.hsv_to_rgb(i / num_triangles, 1.0, 1.0)  # Generate rainbow colors
        draw_triangle(length, color)
        pen.penup()
        pen.forward(range_step)  # Move forward by a fixed step length
        pen.pendown()

# Draw the pattern
pen.penup()
pen.goto(-200, 0)
pen.pendown()
draw_pattern()

# Hide the turtle and display the window
pen.hideturtle()
turtle.done()
