from datetime import datetime     #packagename and library
from datetime import date

datetime.today()     #method called as today
today = datetime.today()
todaydate = date.today()
todaydate.month

todaydate.year

todaydate.day


Republic_Day = date(2020, 1, 26)
Republic_Day
if Republic_Day is not todaydate:
    print("Sorry there are still " + str((Republic_Day - todaydate).days) + " days until Republic Day!")
else:
    print("Yay it's Republic Day!")
