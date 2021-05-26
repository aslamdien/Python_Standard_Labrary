from datetime import datetime, timedelta

dt = datetime(2021, 5, 26)
add_dt1 = dt + timedelta(weeks=2)
print("First Date is: " + str(add_dt1.strftime("%m-%d-%Y")))

add_dt2 = add_dt1 + timedelta(weeks=2)
print("Second Date is: " + str(add_dt2.strftime("%m-%d-%Y")))

add_dt3  = add_dt2 + timedelta(weeks=2)
print("Third Date is: " + str(add_dt3.strftime("%m-%d-%Y")))

add_dt4 = add_dt3 + timedelta(weeks=2)
print("Forth Date is: " + str(add_dt4.strftime("%m-%d-%Y")))

add_dt5 = add_dt4 + timedelta(weeks=2)
print("Fifth Date is: " + str(add_dt5.strftime("%m-%d-%Y")))

add_dt6 = add_dt5 + timedelta(weeks=2)
print("Sixth Date is: " + str(add_dt6.strftime("%m-%d-%Y")))

add_dt7 = add_dt6 + timedelta(weeks=2)
print("Seven Date is:" + str(add_dt7.strftime("%m-%d-%Y")))

add_dt8 = add_dt7 + timedelta(weeks=2)
print("Eight Date is: " + str(add_dt8.strftime("%m-%d-%Y")))

add_dt9 = add_dt8 + timedelta(weeks=2)
print("Ninth Date is: " + str(add_dt9.strftime("%m-%d-%Y")))

add_dt10 = add_dt9 + timedelta(weeks=2)
print("Tenth Date is:" + str(add_dt10.strftime("%m-%d-%Y")))

#Tepleo Version
current_date = datetime.today()

for i in range(0, 10): # it uses a loop
    added_date = current_date + timedelta(weeks=2) # You could also use days in timedelta
    current_date = added_date 
    print(added_date.strftime("%Y-%m-%d"))
