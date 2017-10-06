class C115:

    def has_duplicate(self,n):
        listLen = len(n) #Lenth of the list
        setLen = len(set(n)) #converting the list to set to find if there was any duplicate
        if(listLen != setLen):
            return True
        return False

if __name__ == '__main__':
    obj=C115()
    print(obj.has_duplicate([1,2,4,6,3,3]))
