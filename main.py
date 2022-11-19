import numpy as np
from sklearn.svm import LinearSVC
from PIL import Image
import matplotlib.pyplot as plt

arrayOneModelNumberZero = []
arrayOneModelNumberOne = []
arrayOneModelNumberTwo = []
arrayOneModelNumberThree = []
arrayOneModelNumberFour = []
arrayOneModelNumberFive = []
arrayOneModelNumberSix = []
arrayOneModelNumberSeven = []
arrayOneModelNumberEight = []
arrayOneModelNumberNine = []


def modelTraining(valuesPixel):
    with open('n0.pgm', 'rb') as pgmf:
        im1 = plt.imread(pgmf)

    with open('n1.pgm', 'rb') as pgmf:
        im2 = plt.imread(pgmf)

    with open('n2.pgm', 'rb') as pgmf:
        im3 = plt.imread(pgmf)

    with open('n3.pgm', 'rb') as pgmf:
        im4 = plt.imread(pgmf)

    with open('n4.pgm', 'rb') as pgmf:
        im5 = plt.imread(pgmf)

    with open('n5.pgm', 'rb') as pgmf:
        im6 = plt.imread(pgmf)

    with open('n6.pgm', 'rb') as pgmf:
        im7 = plt.imread(pgmf)

    with open('n7.pgm', 'rb') as pgmf:
        im8 = plt.imread(pgmf)

    with open('n8.pgm', 'rb') as pgmf:
        im9 = plt.imread(pgmf)

    with open('n9.pgm', 'rb') as pgmf:
        im10 = plt.imread(pgmf)

    for i in range(0, 10):
        for j in range(0, 10):
            arrayOneModelNumberZero.append(im1[i][j])
            arrayOneModelNumberOne.append(im2[i][j])
            arrayOneModelNumberTwo.append(im3[i][j])
            arrayOneModelNumberThree.append(im4[i][j])
            arrayOneModelNumberFour.append(im5[i][j])
            arrayOneModelNumberFive.append(im6[i][j])
            arrayOneModelNumberSix.append(im7[i][j])
            arrayOneModelNumberSeven.append(im8[i][j])
            arrayOneModelNumberEight.append(im9[i][j])
            arrayOneModelNumberNine.append(im10[i][j])


    treino_x = [arrayOneModelNumberZero, arrayOneModelNumberOne, arrayOneModelNumberTwo, arrayOneModelNumberThree, arrayOneModelNumberFour, arrayOneModelNumberFive,
                arrayOneModelNumberSix, arrayOneModelNumberSeven, arrayOneModelNumberEight, arrayOneModelNumberNine]
    treino_y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    modelo = LinearSVC()
    print(modelo.fit(treino_x, treino_y))

    x = modelo.predict([valuesPixel])
    showPrediction(x)

def showPrediction(x):
    if x == 0:
        im = Image.open('0.png')
        im.show()
    if x == 1:
        im = Image.open('1.jpg')
        im.show()
    if x == 2:
        im = Image.open('2.jpg')
        im.show()
    if x == 3:
        im = Image.open('3.png')
        im.show()
    if x == 4:
        im = Image.open('4.png')
        im.show()
    if x == 5:
        im = Image.open('5.png')
        im.show()
    if x == 6:
        im = Image.open('6.png')
        im.show()
    if x == 7:
        im = Image.open('7.jpeg')
        im.show()
    if x == 8:
        im = Image.open('8.png')
        im.show()
    if x == 9:
        im = Image.open('9.jpg')
        im.show()

def showMatrizNumber(number):
    converted_num = str(number)
    imagePixels = []
    with open('n'+converted_num+'.pgm', 'rb') as pgmf:
        matriz = plt.imread(pgmf)
    print(matriz)
    for i in range(0, 10):
        for j in range(0, 10):
            imagePixels.append(matriz[i][j])
    return imagePixels


def getNumberFromUser():
    print('1 Para verificar a imagem (N9) :')
    print('2 Para verificar a imagem (N8) :')
    print('3 Para verificar a imagem (N7) :')
    print('4 Para verificar a imagem (N6) :')
    print('5 Para verificar a imagem (N5) :')
    print('6 Para verificar a imagem (N4) :')
    print('7 Para verificar a imagem (N3) :')
    print('8 Para verificar a imagem (N2) :')
    print('9 Para verificar a imagem (N1) :')
    print('10 Para verificar a imagem (N0) :')

    number = int(input(':'))

    if number == 1:
        number = 9

    if number == 2:
        number = 8

    if number == 3:
        number = 7

    if number == 4:
        number = 6

    if number == 5:
        number = 5

    if number == 6:
        number = 4

    if number == 7:
        number = 3

    if number == 8:
        number = 2

    if number == 9:
        number = 1

    if number == 10:
        number = 0

    values = showMatrizNumber(number)
    return values

if __name__ == '__main__':
    print('hello')
    valuesPixel = getNumberFromUser()
    modelTraining(valuesPixel)
