from PIL import Image
import os
import turtle

pt = 1
draw = 0

#Writes categories to file
def write(array, name, pt, colours):
    if (pt == 1):
        print("")
    f = open(name, "w")
    space = ""
    for i in range(len(colours)):
        space += " "
        for j in range(len(array["%s" % colours[i]])):
            f.write("%d%s%d\n" % (array["%s" % colours[i]][j][0], space, array["%s" % colours[i]][j][1]))
            if (pt == 1):
                print("%d%s%d" % (array["%s" % colours[i]][j][0], space, array["%s" % colours[i]][j][1]))
            if j%2 == 1:
                f.write("=NA()%s=NA()\n" % space)
            if (pt == 1):
                print("=NA()%s=NA()" % space)
    f.close()    

def finalwrite(array, name, pt):
    if (pt == 1):
        print("")
    f = open(name, "w")
    for i in array:
        f.write("%s\n" % i)
        if (pt == 1):
            print("%s" % i)
    f.close()

def combine(array, colours, output, pt):
    if (pt == 1):
        print("")
    space = ""
    remspace = ""
    n = 1
    for i in range(len(colours)):
        while (int(1.5*len(array["%s" % colours[i]]))) >= len(output):
            output.append(output[0])
        output[0] += "  "
        space += " "
        remspace = ""
        for j in range(len(colours)-i):
            remspace += " "
        for j in range(len(array["%s" % colours[i]])):
            output[n] += "%d%s%d%s" % (array["%s" % colours[i]][j][0], space, array["%s" % colours[i]][j][1], remspace)
            if (pt == 1):
                print(output[n])
            n += 1
            if j%2 == 1:
                output[n] += "=NA()%s=NA()%s" % (space, remspace)
                if (pt == 1):
                    print(output[n])
                n+= 1
        while n < len(output):
            output[n] += space + space
            n+=1
    #print(len(output))
    return output

def scanimage(xoffset, yoffset, col, filename, colours):
    im = Image.open(filename, 'r')
    pix = im.load()
    #print(im.size)  # Get the width and hight of the image for iterating over

    vline_colours = {}
    vlines = 0
    for i in range(0, im.size[0]):
        currentcolour = [255, 255, 255]
        colourindex = 0
        for j in range(0, im.size[1]):
            temp = int(col*((pix[i,j][0]+col/2)//col))
            colour = [temp, temp, temp]
            if temp < 255:
                if colour not in colours:
                    colours.append(colour)
                    print("added ", colour)
                if "%s" % colour not in vline_colours:
                    vline_colours["%s" % colour] = []
                if currentcolour != colour: #if different colour
                    vline_colours["%s" % colour].append([i+xoffset, -j+yoffset]) #add start of line
                    vline_colours["%s" % colour].append([i+xoffset, -j-1+yoffset]) #add end point of line
                    vlines += 1
                else:
                    #print(len(line_colours[colourindex]))
                    vline_colours["%s" % colour][len(vline_colours["%s" % colour])-1] = [i+xoffset, -j-1+yoffset] # extend line by 1
                #print(i, j, colour)  # Get the RGBA Value of the a pixel of an image
            currentcolour = colour
    #print(vlines)

    hline_colours = {}
    hlines = 0
    for i in range(0, im.size[1]):
        currentcolour = [255, 255, 255]
        colourindex = 0
        for j in range(0, im.size[0]):
            #colour = pix[i,j]
            temp = int(col*((pix[j,i][0]+col/2)//col))
            colour = [temp, temp, temp]
            if temp < 255:
                if colour not in colours:
                    colours.append(colour)
                    line_colours["%s" % colour] = []
                    print("added ", colour)
                if "%s" % colour not in hline_colours:
                    hline_colours["%s" % colour] = []
                if currentcolour != colour: #if new colour
                    hline_colours["%s" % colour].append([j+xoffset, -i+yoffset]) #add start of line
                    hline_colours["%s" % colour].append([j+1+xoffset, -i+yoffset]) #add end point of line
                    hlines += 1
                else:
                    #print(len(line_colours[colourindex]))
                    hline_colours["%s" % colour][len(hline_colours["%s" % colour])-1] = [j+1+xoffset, -i+yoffset] # extend line by 1
                #print(i, j, colour)  # Get the RGBA Value of the a pixel of an image
            currentcolour = colour
    #print(hlines)

    if hlines < vlines:
        #print("horizontal")
        #print(hlines)
        return hlines, colours, hline_colours
    else:
        #print("vertical")
        #print(vlines)
        colour = [0, 0, 0]
        if "%s" % colour not in vline_colours:
            vline_colours["%s" % colour] = []
            vline_colours["%s" % colour].append([0, 0]) #add start of line
            vline_colours["%s" % colour].append([0, 0]) #add start of line
            vlines += 2
            #print("Empty Frame, Adding line")
        return vlines, colours, vline_colours

colours = []
max_lines = 0
clines= [""]

xoffset = -240
yoffset = 180
start = 1
end = 6573

for image in range(start, end+1):
    #image = 3306
    filename = "badapple0"
    for i in range (4-len("%s" % image)):
        filename += "0"
    filename += "%s.png" % image
    print(filename)

    if draw == 1:
        turtle.setup(480, 360, 0, 0)
        turtle.title("Frame %s.py" % filename)
        turtle.pu()
        turtle.home()
        turtle.clear()
        print(turtle.window_width())
        print(turtle.window_height())
        turtle.colormode(255)
        turtle.speed(0)
        #turtle.speed(1)


    im = Image.open(filename, 'r')

    pix = im.load()
    #print(im.size)  # Get the width and hight of the image for iterating over
    #for i in range(0, im.size[0]):
    #    for j in range(0, im.size[1]):
    col = 256
    line_colours = {}

    lines, colours, line_colours = scanimage(xoffset, yoffset, col, filename, colours)

    if lines > max_lines:
        max_lines = lines

    #print("colours: ", len(colours))
    #print(max_lines)

    clines = combine(line_colours, colours, clines, 0)
    #write(line_colours, "frame%d.txt" % image, pt, colours)

    for i in range(len(line_colours)):
        #print(colours[i])
        if draw == 1:
            turtle.pencolor(colours[i])
            for j in range(len(line_colours["%s" % colours[i]])):
                #turtle.goto(line_colours[i][j])
                turtle.goto(line_colours["%s" % colours[i]][j])
                if turtle.isdown()== 0:
                    turtle.pd()
                else:
                    turtle.pu()
                #print(turtle.isdown())
            #print(line_colours[i][j])

finalwrite(clines, "Frames %d-%d.txt" % (start, end), 0)
print("colours: ", len(colours))
print(max_lines)
