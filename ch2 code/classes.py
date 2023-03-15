
"""
Created on Wed Mar 15 10:24:18 2023

@author: Arman
"""
class Student:
    rollNum = 0
    name = ""
    markList=[]
    stream = ''
    percentage = 0.0
    grade = ''
    division = ''
    
    def __inti__(self, roll,name,stream):
        self.rollNum = roll
        self.name = name
        self.stream = stream
    
    def setMarks(self):
        for i in range(0,5):
            e = int(input("Enter marks : "))
            self.markList.append(e)
    
    def getStream(self,stream):
        streams = {'A':"Arts",'C':"Commerce", 'S':"Science"}
        return streams[stream]
    def percentage(self):
        self.percentage = (sum(self.markList)/len(self.markList)*100)*100
    
    def gradeGen(self):
        self.grade = 'A'
        return self.grade
    
def main():
    s1 = Student()
    s1.setMarks()
    s1.percentage()
    print(s1.markList)
    print(s1.percentage)
    
    
    
if __name__ == '__main__':
    main()
