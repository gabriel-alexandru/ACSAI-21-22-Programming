import images

def hasNeighborBlack(pixels, x, y):
   for i in range(-1 , 2):
      for j in range(-1 , 2):
         if pixels[x+i][y+j] == (0, 0, 0):
            return True

def generateBlackPixels(width, height):
   pixels = []
   for i in range(width):
      linePixels = []
      linePixels.extend([(0, 0, 0)] * height)
      pixels.append(linePixels)
   return pixels

def readLines(text):
   lines = []
   for line in text:
      if line != '':
         numbers = line.split(' ')
         partialLine = []
         for number in numbers:
            if(number != ''):
               partialLine.append(int(number))
            
         lines.append(partialLine)
   return lines

def checkRedCorrect(pixels, width, height):
   for i in range(1, width - 9):
      for j in range(1, height - 9):
         if(pixels[i][j] == (255, 0, 0) and not hasNeighborBlack(pixels, i, j)):
            pixels[i][j] = (0, 255, 0)

def countReds(pixels):
   redpixelsCount = sum(line.count((255, 0, 0)) for line in pixels)
   return redpixelsCount

def setBorder(pixels, i, j, x1, y1, x2, y2):
   if (i == y2 or i == y1) or (j == x1 or j == x2):
      if hasNeighborBlack(pixels, i, j):
         pixels[i][j] = (255, 0, 0)
      else:
         pixels[i][j] = (0, 255, 0)

def generateRectangles(pixels, line):
   x1, x2, y1, y2 = line[0], line[2], line[1], line[3]
   for i in range(y2, y1 + 1):
      for j in range(x1, x2 + 1):
         pixels[i][j] = (255, 255, 255)
         setBorder(pixels, i, j, x1, y1, x2, y2)

def ex1(text_file, pngfile):
   # insert your code here
   file = open(text_file, 'r')
   text = file.read().split('\n')
   file.close()
   lines = readLines(text)

   maxColumns = list(map(max, zip(*lines)))
   height = maxColumns[0] + 10 if maxColumns[0] > maxColumns[2] else maxColumns[2] + 10
   width = maxColumns[1] + 10 if maxColumns[1] > maxColumns[3] else maxColumns[3] + 10

   # pixels = [[(0, 0, 0)] * height for i in range(width)]
   pixels = generateBlackPixels(width, height)

   for line in lines:
      generateRectangles(pixels, line)

   checkRedCorrect(pixels, width, height)

   images.save(pixels, pngfile)
   return countReds(pixels)

if __name__ == '__main__':
   ex1('rectangles_1.txt', 'test.png')
   pass
   # insert your examples here

