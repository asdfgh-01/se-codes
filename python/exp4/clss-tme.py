class Time:
    def __init__(self,hours,minutes):
        self.hours=hours
        self.minutes=minutes
    def addTime(self,x,y):
        self.total_hours=(x.hours+y.hours)+(x.minutes+y.minutes)//60
        self.total_minutes=(x.minutes+y.minutes)%60
    def displayTime(self):
        print("addition of both : ",self.total_hours,"hours and",self.total_minutes,"minutes")
    def displayMinute(self):
        self.only_minutes=(self.hours*60)+self.minutes
        print(f"total minutes of {self.hours} hours and {self.minutes} minutes:",self.only_minutes)
h1,m1=input("enter your time: ").split()
h2,m2=input("enter your time: ").split()
t1=Time(int(h1),int(m1))
t2=Time(int(h2),int(m2))
t3=Time(0,0)     
t3.addTime(t1,t2)
t3.displayTime()
t1.displayMinute()