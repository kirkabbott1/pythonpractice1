
week =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

day_of_week = int(raw_input("Please give a day of week (0-6) 0 is Sunday."))
if day_of_week == 0 or day_of_week == 6:
    print "It is %s, sleep in." % week[day_of_week]
else:
    print "It is %s, go to work." % week[day_of_week]
