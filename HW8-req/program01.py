# -*- coding: utf-8 -*-

def getNextMove(color, move, level):
   if level == 2:
      nextMove = (color, move)
   else:
      nextMove = (color, *move)
   return nextMove

def getNextMoveMatrix(matrix):
   return [[*row] for row in matrix]

def getCombinations(colors, level):
   combinations = []
   if level <= 1:
      return tuple(colors)
   
   for color in colors:
      nextMoves = getCombinations(colors, level - 1)
      for move in nextMoves:
         combinations.append(getNextMove(color, move, level))
   return combinations

def getCombinationsRect(colors, level):
   tmp = getCombinations(colors, level)
   combinations = []
   for combination in tmp:
      valid = False
      for i in range(len(combination) - 1):
         if combination[i] != combination[i + 1]:
            valid = True
         else:
            valid = False
            break
      if valid:
         combinations.append(combination)
   return combinations

def subdivide(n, lst):
    return tuple([lst[i:i+n] for i in range(0, len(lst), n)])

def divideTuple(tpl, n, newTpl):
   if len(tpl) == 0:
      return tuple(newTpl)

   newTpl.append(tuple(tpl[0:n]))
   del tpl[0:n]
   return divideTuple(tpl, n, newTpl)

def getEmptyPattern(colors, D):
   images = []
   combinations = getCombinations(colors, D * D)
   isTuple = isinstance(combinations, tuple)
   combLen = len(combinations)
   if(combLen > 1 and not isTuple):
      for combination in combinations:
         images.append(subdivide(D, combination))
   elif(isTuple and combLen > 1):
      images.extend(subdivide(D, divideTuple(list(combinations), D, [])))
   else:
      images.append(tuple([combinations]))
   return images

def getCrossPattern(colors, D):
   images = []
   combinations = [combination for combination in getCombinations(colors, 2) if combination[0] != combination[1]]

   for combination in combinations:
      if(D % 2 == 1):
         tmp = subdivide(D, combination * ((D * D)))
         images.extend(list(divideTuple(list(tmp), D, [])))
      else:
         tmp = subdivide(D, combination * ((D * D) // 2))
         tmp2 = []
         for i in range(len(tmp)):
            if i % 2 == 0:
               tmp2.extend([tmp[i][::-1]])
            else:
               tmp2.extend([tmp[i]])
         images.append(tuple(tmp2))
   return images

def getVRect(colors, D):
   images = []
   combinations = getCombinationsRect(colors, D)

   for combination in combinations:
      tmp = combination * D
      images.append(subdivide(D, tmp))
   return images

def getHRect(colors, D):
   images = []
   combinations = getCombinationsRect(colors, D)
   
   for combination in combinations:
      image = []
      for color in combination:
         image.append(tuple([color] * D))
      
      images.append(tuple(image))
   return images

def getDiffPattern(colors, D):
   images = []
   tmp = getDiffCombinations(colors, D, D*D, getMatrix(D))
   for combination in tmp:
      images.append(subdivide(D, combination))
   return images

def neighbours(matrix, x, y, color):
   for previousX in range(x-1, x+2):
      try:
         if matrix[y-1][previousX] == color and previousX != -1:
            return False
      except IndexError:
         break

   if matrix[y][x-1] == color and x-1 != -1:
      return False

   return True

def getMatrix(D):
   return [[None]*D]*D

def getNextMovesDiff(colors, D, level, nextMoveMatrix, x, y):
   return getDiffCombinations(colors, D, level, nextMoveMatrix, 0, y+1) if x+1 == D else getDiffCombinations(colors, D, level, nextMoveMatrix, x+1, y)

def getDiffCombinations(colors, D, level, matrix, x=0, y=0):
   if level == 1:
      return [c for c in colors if neighbours(matrix, x, y, c)]          
   combos = []          
   for color in colors:
      nextMoveMatrix = getNextMoveMatrix(matrix)
      if neighbours(nextMoveMatrix, x, y, color):
         nextMoveMatrix[y][x] = color
         for move in getNextMovesDiff(colors, D, level - 1, nextMoveMatrix, x, y):
            combos.append(getNextMove(color, move, level))
   return combos

def ex(colors, D, img_properties):
   if img_properties == '':
      return getEmptyPattern(colors, D)
   elif img_properties == 'pattern_cross_':
      return getCrossPattern(colors, D)
   elif img_properties == 'pattern_vrect_':
      return getVRect(colors, D)
   elif img_properties == 'pattern_hrect_':
      return getHRect(colors, D)
   elif img_properties == 'pattern_diff_':
      return getDiffPattern(colors, D)
   else:
      return []

if __name__ == '__main__':
   # add here your test cases
   print(ex([0, 128, 196, 255], 7, 'pattern_diff_'))
   pass
