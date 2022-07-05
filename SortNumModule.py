#SortNumber module made by sadegh_gfc
from itertools import count
class SortNumber():
    def SortNumber_SmallToBig(numbersList = []):
        numbersList_count = len(numbersList)
        #The "i for" Because if you dont put this if your operation just work for 1 time for exam: numbersList = [5, 7, 3 ,4 ,8, 9 ,1 ,6, 2, 0] if you dont appent this "i for" you renderd this: [5 3 4 7 8 1 6 2 0 9]
        # the "j for" Because Sorting
        for i in range(0,numbersList_count):  
            for j in range(0,numbersList_count -1):
                zarf1 = numbersList[j]
                zarf2 = numbersList[j + 1]
                zarf3 = None
                if zarf1 > zarf2:
                    zarf3 = zarf1
                    zarf1 = zarf2
                    zarf2 = zarf3

                    numbersList[j] = zarf1
                    numbersList[j +1] = zarf2
                elif zarf1 < zarf2:
                    continue
                else: 
                    print("SomeThing Wrong in SortNumber class")
                j = j + 1
        return numbersList
     
    def SortNumber_BigToSmall(numbersList = []):
        numbersList_count = len(numbersList)
        for i in range(0,numbersList_count):  
            for j in range(0,numbersList_count -1):
                zarf1 = numbersList[j]
                zarf2 = numbersList[j + 1]
                zarf3 = None
                if zarf1 < zarf2:
                    zarf3 = zarf1
                    zarf1 = zarf2
                    zarf2 = zarf3

                    numbersList[j] = zarf1
                    numbersList[j +1] = zarf2
                elif zarf1 > zarf2:
                    continue
                else: 
                    print("SomeThing Wrong in SortNumber class")
                j = j + 1
        return numbersList


    

