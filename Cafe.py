import time, progressbar, datetime, jdatetime
#------------------------------
def Total_Income(income):
    sum_income = 0
    for x in income:
        sum_income += x
    return float("{:.3f}".format(sum_income))
#------------------------------
#Calculate price in minute
def minute_price(pri , clk):
    minute_cost = float("{:.2f}". format((pri / 60) * clk))#calculate new price per minute
    return minute_cost
#------------------------------
#Calculate price in hour
def hour_price(integer, decimal, pri):
    #decimal * 100 = actual and correct minute value. example: 0.30 * 100 = 30
    dec = float("{:.2f}". format(decimal * 100))
    hour_cost = (integer * pri) + (dec * (pri / 60))
    return hour_cost
#------------------------------
def clock_show():
    geo_time = datetime.datetime.now()
    pre_time = jdatetime.datetime.now()
    georgian = geo_time.strftime("%m/%d/%Y, %H:%M:%S")
    persian = str(pre_time.strftime("%m/%d/%Y, %H:%M:%S"))
    print(f"{georgian} Equivalent to {persian}\n")
#------------------------------
def Waiting():
    widgets = ['Waiting: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
    
    for i in range(10):
        time.sleep(0.1)
        bar.update(i)
#------------------------------
def Exit_Cafe():
    #exit_cafe =
    input("\nPress Enter to exit...")
    print("\nGoodBye...!\n")
    #return exit_cafe

Customer_List = []
customer_counter = 0

print("\n\tWelcome to Cafe...!\n")
clock_show()

#Amount of game cost per hour.
rate_price = float(input("Enter the amount of the rate per hour of game: "))

vip_question = input("Your cafe have a VIP membership? [Yes/NO]: ").lower()

if vip_question == 'y' or vip_question == 'yes':
    vip_discount_rate = float(input("Enter the discount amount for VIP member: "))
    while True:
        clock = input("\nHow many Hours or Minutes did you play?\n[h = hour and m = min. e for exit.]: ")
        new_time = clock.split(" ")

        if "h" in new_time:
        #split clock to integer and decimal. integer = hour and dec = minutes
            hour = float(new_time.pop(0))
            integer, dec = divmod(hour, 1)
            hours_cost = hour_price(integer, dec, rate_price)

            vip_discount = abs(((hours_cost * vip_discount_rate) / 100) - hours_cost)
            print("The cost with a special member discount is equal to = " ,vip_discount)

            customer_counter += 1
            Customer_List.append(vip_discount)

        elif "m" in new_time:
            minute = int(new_time.pop(0))
            minute_price(rate_price , minute)
            minute_cost = minute_price(rate_price , minute)

            vip_discount = abs(((minute_cost * vip_discount_rate) / 100) - minute_cost)
            print("The cost with a special member discount is equal to = " ,vip_discount)

            customer_counter += 1
            Customer_List.append(vip_discount)

        elif "e" in clock:
            Waiting()
            print(f"\nToday you have ({customer_counter}) customer."+
                    f"\nYour total income is {Total_Income(Customer_List)} Toumaan.")
            Exit_Cafe()
            break
    
elif vip_question == 'n' or vip_question == 'no':
    while True:
        clock = input("\nHow many Hours or Minutes did you play?\n[h = hour and m = min. e for exit.]: ")
        new_time = clock.split(" ")

        if "h" in new_time:
        #split clock to integer and decimal. integer = hour and dec = minutes
            hour = float(new_time.pop(0))
            integer, dec = divmod(hour, 1)
            hours_cost = hour_price(integer, dec, rate_price)

            print(f"\nYou played for {hour} hours. The cost is equal to {hours_cost} Toumaan.")

            customer_counter += 1
            Customer_List.append(hours_cost)

        elif "m" in new_time:
            minute = int(new_time.pop(0))
            minute_price(rate_price , minute)
            minutes_cost = minute_price(rate_price , minute)

            print(f"\nYou played for {minute} minutes. The cost is equal to {minutes_cost} Toumaan.")

            customer_counter += 1
            Customer_List.append(minutes_cost)

        elif "e" in clock:
            Waiting()
            print(f"\nToday you have ({customer_counter}) customer."+
                    f"\nYour total income is {Total_Income(Customer_List)} Toumaan.")
            Exit_Cafe()
            break