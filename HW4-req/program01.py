import pronouncing
import math

def c(first, second, tau):
    cont = 0
    for i in range(len(first)):
        if first[i] == '1':
            for j in range(0, tau+1):
                if('1' in second[i-j: i+1]):
                    cont += 1
                    break

    return cont

def m(line):
    return line.count('1')

def SyncCalc(lineA, lineB, tau):
    accsA, accsB = m(lineA), m(lineB)
    return 0 if accsA == 0 or accsB == 0 else (0.5 * (c(lineB, lineA, tau) + c(lineA, lineB, tau))) / math.sqrt(accsA * accsB)

def normaliseMatrix(matrix):
    newMatrix = []
    length = max([len(i) for i in matrix])
    for line in matrix:
        line += '0' * (length - len(line))
        newMatrix.append(line)
    return newMatrix

def generateAvgSync(matrix, tau):
    synclist = []
    matLen = len(matrix)
    for i in range(matLen - 1):
        for j in range(i + 1, matLen):
            synclist.append(SyncCalc(matrix[i], matrix[j], tau))
    return round(sum(synclist) / len(synclist), 6)

def getMatrix(lines):
    mainAccents = []
    for line in lines:
        print(ord('—'))
        trans = {33: 32, 34: 32, 35: 32, 36: 32, 37: 32, 38: 32, 39: 32, 40: 32, 41: 32, 42: 32, 43: 32, 44: 32, 45: 32, 46: 32, 47: 32, 58: 32, 59: 32, 60: 32, 61: 32, 62: 32, 63: 32, 64: 32, 91: 32, 92: 32, 93: 32, 94: 32, 95: 32, 96: 32, 123: 32, 124: 32, 125: 32, 126: 32, 8212: 32}
        line = line.translate(trans)
        lineAccents = ''
        if line != '':
            text = line.split(' ')
            for word in text:
                if word != '':
                    lineAccents += getAccents(word)

            mainAccents.append(lineAccents)
    return mainAccents

def getAccents(word):
    phones = pronouncing.phones_for_word(word)
    return pronouncing.stresses(phones[0]).replace('2', '0') + '0' if len(phones) > 0 else '0' * int(len(word) / 2) + '0'

def PoemSync(inputfilename, outputfilename, tau):
    file = open(inputfilename, "r", encoding='utf-8')
    lines = file.read().split('\n')
    file.close()

    mainAccents = getMatrix(lines)

    
    mainAccents = normaliseMatrix(mainAccents)

    outputfile = open(outputfilename, 'w', encoding='utf-8')
    outputfile.write('\n'.join(mainAccents))
    outputfile.close()
    return generateAvgSync(mainAccents, tau)

if __name__ == "__main__":
    # Use phone_for_words and stresses functions.
    PoemSync('poems/text04.200.txt', 'test.txt', 15)
    pass

