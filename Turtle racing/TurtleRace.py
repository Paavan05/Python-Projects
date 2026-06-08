import turtle, random, time

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_no_of_racers():
    racers = 0
    
    while True:
        racers = input("Enter number of racers (2 - 10): ")
        
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Invalid input. Type in digits")
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number of racers must be between 2 and 10.")
            
def init_turtle_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

def create_turtle(colors):
    turtles = []
    spacingX = WIDTH // (len(colors) + 1)
        
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1)*spacingX, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    
    return turtles

def race(colors):
    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]

racers = get_no_of_racers()
init_turtle_screen()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"Winner is the {winner} color Turtle!")
time.sleep(3)