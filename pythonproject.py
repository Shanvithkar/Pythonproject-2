def CalculateAngle(h, m):
    #validate the input
    if (h < 0 or m < 0 or h > 12 or m > 60):
        print("Wrong input")
        exit()              #exiting the programm if condition is true
    if (h == 12):
        h=0
    if (m==60):
        m=0
        h += 1
        

#calculate the angles made bu hour and minute hands with reference to 12:00
#360 degrees in 60 minutes so 6 degree in 1 minute
#360 degree in 12 hours so 360/12*60 in 1 minute

    Hour_Angle = 0.5*(h*60+m)
    Minute_Angle = 6*m

#find the difference between two angles
    angle=abs(Hour_Angle-Minute_Angle)
#return the smaller angle of two possible angles
    angle = min(360-angle,angle)

    return angle
#inputing the values h for hours and m for minutes

h=int(input("Enter Hours: "))
m=int(input("Enter Minutes: "))
#checking condition if hours are greater than 12
if (h>=12):
    h=abs(12-h)
#printing and calling  the calculatAngle() function
print("Angle: ",CalculateAngle(h, m)) 