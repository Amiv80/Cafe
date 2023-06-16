Cafe Management System

This Python code implements a cafe management system that calculates the cost of playing games at the cafe based on the rate per hour. It offers features such as VIP membership discounts and tracks the total income generated.

Features:
- Calculates the cost of playing games at the cafe based on the rate per hour.
- Supports VIP membership discounts for eligible customers.
- Displays the current time in both Gregorian and Jalali calendars.
- Provides a progress bar while waiting.
- Tracks the number of customers and their respective costs.
- Calculates the total income generated.

Usage:
1. Import the required modules:
   - `time` for managing time-related operations.
   - `progressbar` for displaying a progress bar while waiting.
   - `datetime` for working with dates and times in the Gregorian calendar.
   - `jdatetime` for working with dates and times in the Jalali calendar.

2. Initialize the `customer_list` and `customer_counter` variables to track the number of customers and their respective costs.

3. Prompt the user for the rate per hour of the game.

4. Ask the user if the cafe has VIP membership.

5. If VIP membership is available, ask for the discount amount for VIP members.

6. Use the input loop to repeatedly ask for the number of hours or minutes played, calculate the cost, apply VIP discounts if applicable, and track the customer's cost in the `customer_list`.

7. If the user chooses to exit, display a progress bar while simulating waiting, calculate the total income using the `total_income()` function, and print the number of customers and the total income.

8. Finally, the program prompts the user to press Enter to exit.

Ensure that the required modules (`progressbar`, `jdatetime`) are installed and available for import before running the code.


سیستم مدیریت کافه

این کد پایتون یک سیستم مدیریت کافه را پیاده‌سازی می‌کند که هزینه بازی در کافه را بر اساس نرخ در ساعت محاسبه می‌کند. این کد شامل ویژگی‌هایی مانند تخفیف عضویت VIP و پیگیری درآمد کل است.

ویژگی‌ها:
- محاسبه هزینه بازی در کافه بر اساس نرخ در ساعت
- پشتیبانی از تخفیف عضویت VIP برای مشتریان واجد شرایط
- نمایش زمان فعلی در تقویم‌های میلادی و جلالی
- ارائه نوار پیشرفت در زمان انتظار
- پیگیری تعداد مشتریان و هزینه‌های آن‌ها
- محاسبه کل درآمد تولید شده

روش استفاده:
1. وارد کردن ماژول‌های مورد نیاز:
   - `time` برای مدیریت عملیات مربوط به زمان
   - `progressbar` برای نمایش نوار پیشرفت در زمان انتظار
   - `datetime` برای کار با تاریخ و زمان در تقویم میلادی
   - `jdatetime` برای کار با تاریخ و زمان در تقویم جلالی

2. مقداردهی اولیه متغیرهای `customer_list` و `customer_counter` برای پیگیری تعداد مشتریان و هزینه‌های آن‌ها.
3. دریافت از کاربر نرخ در ساعت بازی.
4. پرسیدن از کاربر درباره وجود عضویت VIP در کافه.
5. اگر عضویت VIP موجود باشد، درخواست تخفیف عضویت برای اعضا را بپرسید.
6. استفاده از حلقه ورودی برای چندین بار پرسیدن تعداد ساعت یا دقیقه‌های بازی شده، محاسبه هزینه، اعمال تخفیف VIP در صورت لزوم و پیگیری هزینه مشتری در `customer_list`.
7. در صورت انتخاب خروج، نمایش نوار پیشرفت در زمان انتظار، محاسبه کل درآمد با استفاده از تابع `total_income()` و چاپ تعداد مشتریان و کل درآمد.
8. در نهایت، برنامه کاربر را به فشردن Enter برای خروج دعوت می‌کند.
قبل از اجرای کد، اطمینان حاصل کنید که ماژول‌های مورد نیاز (`progressbar` و `jdatetime`) نصب شده و قابل وارد شدن باشند.


