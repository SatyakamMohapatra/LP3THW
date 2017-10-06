class C117:

    def scale(self,n,factor):
        for val in range(len(n)):
            n[val] *= factor
        return n

if __name__ == '__main__':
    obj=C117()
    print(obj.scale([1,2,4,6,3,3],2))
