#SortNumber module made by sadegh_gfc
class SortNumber():
    def SortNumber_SmallToBig(numbersList = []):
        numbersList_count = len(numbersList)
        #The "i for" Because if you dont put this if your operation just work for 1 time for exam: numbersList = [5, 7, 3 ,4 ,8, 9 ,1 ,6, 2, 0] if you dont appent this "i for" you renderd this: [5 3 4 7 8 1 6 2 0 9]
        # the "j for" Because Sorting
        for i in range(numbersList_count):  
            for j in range(numbersList_count -1):
                repositori1 = numbersList[j]
                repositori2 = numbersList[j + 1]
                repositori3 = None
                if repositori1 > repositori2:
                    repositori3 = repositori1
                    repositori1 = repositori2
                    repositori2 = repositori3

                    numbersList[j] = repositori1
                    numbersList[j +1] = repositori2
                elif repositori1 < repositori2:
                    continue
                #cahe unexpected Erorr
                else: 
                    print("SomeThing Wrong in SortNumber class")
        return numbersList
     
    def SortNumber_BigToSmall(numbersList = []):
        numbersList_count = len(numbersList)
        for i in range(numbersList_count):  
            for j in range(numbersList_count -1):
                repositori1 = numbersList[j]
                repositori2 = numbersList[j + 1]
                repositori3 = None
                if repositori1 < repositori2:
                    repositori3 = repositori1
                    repositori1 = repositori2
                    repositori2 = repositori3

                    numbersList[j] = repositori1
                    numbersList[j +1] = repositori2
                elif repositori1 > repositori2:
                    continue
                else: 
                    print("SomeThing Wrong in SortNumber class")
        return numbersList


    

