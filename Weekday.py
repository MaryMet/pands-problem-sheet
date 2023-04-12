# Weekly task No 5
# Is this a week day or a weekend day
# using lists, tuples and dictionaries
# Author MAry Metcalfe

Days_of_Week = ("Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
)

Weekend_Days = ("Saturday",
                "Sunday"
)


print (Days_of_Week)
print (Weekend_Days)
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
if x.strftime("%A") in Days_of_Week:
    print ("Unfortunatly today is a weekday")
else:
    print ("It is the weekend Yipee")

# if Days_of_Week : x.strftime("%A") = Days_of_Week
   # print ("Unfortunatly today is a weekday") 
#elif
    #print ("It is the weekend Yipee")

#if (Days_of_Week) = x:
    #print(f"{x} is a weekend unfortuately")

#elif:
    #print(f"{x} Yipee its the weekend")

#for x in Days_of_Week:
   # print(f"{x} is a week day unfortuately")

#for x in Weekend_Days:
   # print (f"{x} is in the weekend - Yippeee")


