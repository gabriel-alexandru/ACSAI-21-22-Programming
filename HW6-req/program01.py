import images

def generateBlackPixels(width, height):
   pixels = []
   for i in range(height):
      linePixels = []
      linePixels.extend([(0, 0, 0)] * width)
      pixels.append(linePixels)
   return pixels

def getBuildings(lines):
  mostBuildingIndex = 0
  recordAmount = 0
  buildings = []
  for line in lines:
    text = line.split(',')
    text.remove('')
    if(len(text) > recordAmount):
      recordAmount = len(text)
      mostBuildingIndex = lines.index(line)
    elt = []
    while len(text) > 0:
      if(text != []):
        elt.append([int(text[0]), int(text[1]), tuple(map(int, text[2:5]))])
        del text[0:5]
    buildings.append(elt)

  buildings.remove([])
  return buildings, mostBuildingIndex

def getHeight(buildings, spacing):
  totalHeight = 0
  for building in buildings:
    maxHeight = 0
    for tmp in building:
      currentHeight = tmp[1]
      if currentHeight > maxHeight:
        maxHeight = currentHeight
    totalHeight += maxHeight

  return totalHeight + ((len(buildings) + 1) * spacing)

def getWidth(buildings, mostBuildingIndex, spacing):
  return sum(building[0] for building in buildings[mostBuildingIndex]) + ((len(buildings[mostBuildingIndex]) + 1) * spacing)

def drawRectangle(pixels, x, y, rectangle):
  for i in range(y, y + rectangle[1]):
    for j in range(x, x + rectangle[0]):
      pixels[i][j] = rectangle[2]

def getPreviousHeight(buildings, i):
  height = 0
  if(i != 0):
    height = max(building[1] for building in buildings[i - 1])
  return height

def getPreviousWidth(rectangle, i,  space):
  previousWidth = 0
  if i != 0:
    previousWidth = rectangle[0] + space

  return previousWidth

def getSpaceBetweenBuilding(width, spacing, street):
  buildingSpace = 0
  if len(street) != 1:
    buildingsWidth = sum(building[0] for building in street)
    buildingSpace = (width - (spacing * 2) - buildingsWidth) // (len(street) - 1)
  return buildingSpace

def getLineY(i, previousY, maxPreviousHeight, spacing):
  lineY = 0
  if i != 0:
    lineY = previousY + maxPreviousHeight + spacing
  else:
    lineY = previousY + maxPreviousHeight
  return lineY

def ex(file_dati, file_png, spacing):
    file = open(file_dati, 'r', encoding='utf-8')
    lines = file.read().replace(' ', '').replace('\t', '').split('\n')
    buildings, mostBuildingIndex = getBuildings(lines)
    width = getWidth(buildings, mostBuildingIndex, spacing)
    height = getHeight(buildings, spacing)

    pixels = generateBlackPixels(width, height)
    previousY = spacing
    for i in range(len(buildings)):
      street = buildings[i]
      buildingSpace = getSpaceBetweenBuilding(width, spacing, street)

      maxPreviousHeight = getPreviousHeight(buildings, i)

      maxCurrentHeight = max(building[1] for building in street)

      previousX = spacing
      lineY = getLineY(i, previousY, maxPreviousHeight, spacing)
      for j in range(len(street)):
        previousWidth = getPreviousWidth(street[j - 1], j, buildingSpace)
        startY = lineY + (maxCurrentHeight // 2) - (street[j][1] // 2)
        if len(street) != 1:
          startX = previousX + previousWidth
        else:
          startX = (width // 2) - (street[j][0] // 2)
        drawRectangle(pixels, startX, startY, street[j])
        previousX = startX
        previousY = lineY

    images.save(pixels, file_png)

    return (width, height)

if __name__ == '__main__':
    print(ex('matrices/example.txt', 'test_example.png', 42))
    # place here your personal tests
    pass
