import random
import time
from discord_webhook import DiscordWebhook

#Settings
GardenSize = 14
#Discord webhook url
url = ''


#Max webhook message size is 2000 char. We take the square of this which is 44. I am unsure if emoji words count as a single char or multiple. 
dbug = ['b', 's']
path_emoji = [':green_square:', ':brown_square:']
plant_emojis = {':corn:':1, ':deciduous_tree:':1, ':tomato:':1, ':hibiscus:':1, ':rose:':1, ':potato:':1, ':deciduous_tree: ':1, ':leafy_green:':1, ':strawberry:':1, ':seedling:':2, ':tulip:':2, ':mushroom:':1, ':rock:':0.5, ':wood:':2, ':snail:':1, ':worm:':2, ':lady_beetle:':2, ':bee:':2}


#Fancy way to initialize a 2d array
garden = [[''] * GardenSize for i in range(GardenSize)]


def drawpath():

    #Pick a random point on the edge of the garden 
    EntryPoint = []
    BoundryLimits = [0, GardenSize-1]
    Axis = random.randint(0, 1)
    Boundry = random.choice(BoundryLimits)
    BoundryCoordinate = random.randint(0,GardenSize-1)

    #Assemble our entry point
    if Axis == 0:
        #start with x axis
        EntryPoint = [Boundry, BoundryCoordinate]
    else:
        #start with y axis
        EntryPoint = [BoundryCoordinate, Boundry]


    #Add path emoji to our entry point
    garden[EntryPoint[0]][EntryPoint[1]] = path_emoji[1]

    print(EntryPoint)
    #Assign our positionand check for the next path block to draw
    position = [EntryPoint[0], EntryPoint[1]]

    while True:
        #Get our heading
        direction = random.randint(1,4)

        if direction == 1:
            #Check if out of bounds
            if position[0]-1 < 0:
                print('Out of bounds Left')

                if position != EntryPoint:
                    print(position)
                    break

            #Check if existing path
            elif garden[position[0]-1][position[1]] == path_emoji[0]:
                print('Existing path')
                break

            #Add path and update position
            else:
                garden[position[0]-1][position[1]] = path_emoji[1]
                position[0] = position[0]-1
                continue
        
        elif direction == 2:
            #Check if out of bounds
            if position[1]+1 > GardenSize-1:
                print('Out of bounds UP')
                
                if position != EntryPoint:
                    print(position)
                    break

            #Check if existing path
            elif garden[position[0]][position[1]+1] == path_emoji[0]:
                print('Existing path')
                break

            #Add path and update position
            else:
                garden[position[0]][position[1]+1] = path_emoji[1]
                position[1] = position[1]+1
                continue

        elif direction == 3:
            #Check if out of bounds
            if position[0]+1 > GardenSize-1:
                print('Out of bounds RIGHT')
                
                if position != EntryPoint:
                    print(position)
                    break

            #Check if existing path
            elif garden[position[0]+1][position[1]] == path_emoji[0]:
                print('Existing path')
                break

            #Add path and update position
            else:
                garden[position[0]+1][position[1]] = path_emoji[1]
                position[0] = position[0]+1
                continue

        elif direction == 4:
            #Check if out of bounds
            if position[1]-1 < 0:
                print('Out of bounds DOWN')
                
                if position != EntryPoint:
                    print(position)
                    break

            #Check if existing path
            elif garden[position[0]][position[1]-1] == path_emoji[0]:
                print('Existing path')
                break

            #Add path and update position
            else:
                garden[position[0]][position[1]-1] = path_emoji[1]
                position[1] = position[1]-1
                continue


while True:
    #Draw garden path
    drawpath()

    #Add plants, bugs, etc
    for y in range(GardenSize):
        for x in range(GardenSize):

            for z, q in plant_emojis.items():
                if q >= random.randint(0,100):

                    if garden[y][x] != path_emoji[1]:
                        garden[y][x] = z

    #Fill in empty space with grass
    for y in range(GardenSize):
        for x in range(GardenSize):
            if garden[y][x] == '':
                garden[y][x] = ':seedling:'

    wbhkstr = '‎\n'            

    for x in range(GardenSize):
        for y in range(GardenSize):
            wbhkstr += garden[y][x]
        wbhkstr += '\n'

    print(len(wbhkstr))

    webhook = DiscordWebhook(url=url, content=wbhkstr)
    response = webhook.execute()

    garden = [[''] * GardenSize for i in range(GardenSize)]
    time.sleep(3600)

main()
