class C115:

    def demo(self):
        a = []
        for i in range(10):
            a.append((i*2))
            a[i] += a[i-1]
        print([ (i**2)+i for i  in range(10)]) # comprehension
        print([chr(i) for i in range(ord('a'),ord('z')+1)])
        return a
if __name__ == '__main__':
    obj=C115()
    print(obj.demo())
