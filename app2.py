class H():
    def __init__(self):
        self.text = 'Hello World'
    def returnH(self):
        return (self.text.lower().count('h') * 'h').upper()

class E():
    def __init__(self):
        self.text = 'Hello World'
    def returnE(self):
        return (self.text.lower().count('e') * 'e')

class L():
    def __init__(self):
        self.text = 'Hello World'
    def returnFirstL(self):
        string = self.text.lower().split('e')[1].split('o')[0]
        ls = []
        for letter in string:
            ls.append(letter)
        return ls[0]
    def returnSecondL(self):
        string = self.text.lower().split('e')[1].split('o')[0]
        ls = []
        for letter in string:
            ls.append(letter)
        return ls[1]
    def returnThirdL(self):
        string2 = self.text.lower().split('r')[1].split('d')[0]
        return string2

class O():
    def __init__(self):
        self.text = 'Hello World'
    def returnFirstO(self):
        return self.text.split(' ')[0].split('l')[2]
    def returnSecondO(self):
        return self.text.split('W')[1].split('r')[0]

class W():
    def __init__(self):
        self.text = 'Hello World'
    def returnW(self):
        return self.text.split(' ')[1].split('o')[0]

classH = H()
classE = E()
classL = L()
classO = O()
classW = W()
h = classH.returnH()
e = classE.returnE()
l1 = classL.returnFirstL()
l2 = classL.returnSecondL()
o1 = classO.returnFirstO()
w = classW.returnW()
o2 = classO.returnSecondO()

l3 = classL.returnThirdL()
h_f = ''.join(h)
he_f = ''.join([h,e])
hel_f = ''.join([he_f,l1])
hell_f = ''.join([hel_f,l2])
hello_f = ''.join([hell_f,o1])
hello__f = ''.join([hello_f,' ']) # couldn't use a class for space bc it wasn't working for some weird reason
hello_w_f = ''.join([hello__f,w])
hello_wo_f = ''.join([hello_w_f,o2])
print(hello_wo_f)