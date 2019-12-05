def main():
    date=input("enter the date :")
    mon,day,year=date.split('/')
    months = ["January", "February", "March", "April","May", "June", "July", "August", "September", "October", "November", "December"]
    mon=months[int(mon)-1]
    print("date is: ",mon+' ',day+' ',year)

main()
print("Hello {0} {1}, you may have won ${2}".format("Mr.", "Smith", 10000))

