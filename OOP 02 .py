class TreasureChest():
    #self.__question : STRING
    #self.__answer : INTEGER
    #self.__points : INTEGER
    def __init__(self,question,answer,points):
        self.__question = question
        self.__answer = answer
        self.__points = points
    def getQuestion(self):
        return self.__question
    def checkAnswer(self,response):
        if response == int(self.__answer):
            return True
        else:
            return False
    def getPoints(self,tries):
        if tries == 1:
            return int(self.__points)
        elif tries == 2:
            return int(self.__points) // 2
        elif tries == 3 or tries == 4:
            return int(self.__points) // 4
        else:
            return 0
arrayTreasure = [] #List used as an array
def readData():
    try:
        with open ("TreasureData.txt") as f:
            count = 0
            for line in f:
                if count % 3 == 0:
                    question = line.strip()
                elif count%3 == 1:
                    answer = int(line.strip())
                else:
                    points = int(line.strip())
                    arrayTreasure.append(TreasureChest(question, answer, points))
                count += 1
    except OSError:
        print("File not found")
readData()
num = int(input("Enter a number from 1-5: "))
if num > 0 and num < 6:
    tries = 0
    result = False
    print(arrayTreasure[num-1].getQuestion())
    while result == False:
        response = int(input("Your response: "))
        result = arrayTreasure[num-1].checkAnswer(response)
        tries += 1
        if result == True:
            print("Points:",int(arrayTreasure[num-1].getPoints(tries)))
        else:
            print("Wrong")
