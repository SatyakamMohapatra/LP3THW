class C113:

    def odd_pair(self,n):
        for i in range(len(n)-1):
            for j in range(1,len(n)):
                prod = n[i] * n[j]
                if prod & 1:
                    return True
        return False

if __name__ == '__main__':
    obj=C113()
    print(obj.odd_pair([1,2,4,6,3]))
