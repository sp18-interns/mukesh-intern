class A:

    def feature1(self):
        print("The mobile is working")
    def feature2(self):
        print("The Camera is working ")
class B(A):

    def feature3(self):
        print("The Game is play")
    def feature4(self):
        print("Speaker play well")
class C(B):
    def feature5(self):
        print("charger well")

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature4

