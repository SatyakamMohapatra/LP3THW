from random import randint

class C115:
    def demo(self,n):
        a=[]
        for i in range(len(n)):
            a.append(n[-i])
        return a
        for j in range(len(n)):
            val1 = randint(n[i],a[i])

if __name__ == '__main__':
    obj=C115()
    print(obj.demo([1,2,3,4,5]))
