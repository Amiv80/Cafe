import time
import progressbar
import datetime
import jdatetime

def total_income(income):
    return round(sum(income), 3)

def minute_price(price, clock):
    minute_cost = round((price / 60) * clock, 2)
    return minute_cost

def hour_price(integer, decimal, price):
    dec = round(decimal * 100, 2)
    hour_cost = (integer * price) + (dec * (price / 60))
    return hour_cost

def clock_show():
    geo_time = datetime.datetime.now()
    pre_time = jdatetime.datetime.now()
    georgian = geo_time.strftime("%m/%d/%Y, %H:%M:%S")
    persian = pre_time.strftime("%m/%d/%Y, %H:%M:%S")
    print(f"{georgian} Equivalent to {persian}\n")

def waiting():
    widgets = ['Processing: ', progressbar.AnimatedMarker(), ' ', progressbar.Percentage(), ' ',
               progressbar.Bar(marker='=', left='[', right=']'), ' ']
    bar = progressbar.ProgressBar(widgets=widgets).start()
    for i in range(10):
        time.sleep(0.1)
        bar.update(i)
    bar.finish()


def exit_cafe():
    print("\nPress Enter to exit...")
    input()
    print("\nGoodbye...!")

customer_list = []
customer_counter = 0

print("\n\tWelcome to Cafe...!\n")
clock_show()

rate_price = 0
while True:
    try:
        rate_price = float(input("Enter the rate per hour of the game: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid rate.")

vip_question = input("Does your cafe have a VIP membership? [Yes/No]: ").lower()

if vip_question in ['y', 'yes']:
    vip_discount_rate = 0
    while True:
        try:
            vip_discount_rate = float(input("Enter the discount amount for VIP members: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid discount rate.")

    while True:
        clock = input("\nHow many hours or minutes did you play? [h = hour, m = min, e = exit]: ")
        new_time = clock.split(" ")

        if "h" in new_time:
            try:
                hour = float(new_time.pop(0))
                integer, dec = divmod(hour, 1)
                hours_cost = hour_price(integer, dec, rate_price)

                vip_discount = abs(((hours_cost * vip_discount_rate) / 100) - hours_cost)
                print("The cost with a special member discount is equal to:", vip_discount)

                customer_counter += 1
                customer_list.append(vip_discount)
            except ValueError:
                print("Invalid input. Please enter a valid number of hours.")

        elif "m" in new_time:
            try:
                minute = int(new_time.pop(0))
                minute_cost = minute_price(rate_price, minute)

                vip_discount = abs(((minute_cost * vip_discount_rate) / 100) - minute_cost)
                print("The cost with a special member discount is equal to:", vip_discount)

                customer_counter += 1
                customer_list.append(vip_discount)
            except ValueError:
                print("Invalid input. Please enter a valid number of minutes.")

        elif "e" in clock:
            waiting()
            total_income_value = total_income(customer_list)
            print(f"\nToday you had {customer_counter} customer(s). Your total income is {total_income_value} Toumaan.")
            exit_cafe()
            break

elif vip_question in ['n', 'no']:
    while True:
        clock = input("\nHow many hours or minutes did you play? [h = hour, m = min, e = exit]: ")
        new_time = clock.split(" ")

        if "h" in new_time:
            try:
                hour = float(new_time.pop(0))
                integer, dec = divmod(hour, 1)
                hours_cost = hour_price(integer, dec, rate_price)

                print(f"\nYou played for {hour} hour(s). The cost is equal to {hours_cost} Toumaan.")

                customer_counter += 1
                customer_list.append(hours_cost)
            except ValueError:
                print("Invalid input. Please enter a valid number of hours.")

        elif "m" in new_time:
            try:
                minute = int(new_time.pop(0))
                minutes_cost = minute_price(rate_price, minute)

                print(f"\nYou played for {minute} minute(s). The cost is equal to {minutes_cost} Toumaan.")

                customer_counter += 1
                customer_list.append(minutes_cost)
            except ValueError:
                print("Invalid input. Please enter a valid number of minutes.")

        elif "e" in clock:
            waiting()
            total_income_value = total_income(customer_list)
            print(f"\nToday you had {customer_counter} customer(s). Your total income is {total_income_value} Toumaan.")
            exit_cafe()
            break
