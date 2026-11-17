# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#پروژه تهیه لیست عادت ها و ثبت وضعیت روزانه با قابلیت گزارش گیری (Habit List Management)

#کتابخانه json برای ذخیره و خواندن داده‌های ساخت‌یافته
#در این پروژه کاربرد برای ذخیره و خواندن داده‌ها به صورت فایل JSON
import json
#کتابخانه os برای برای تعامل با فایل‌ها و سیستم‌عامل
#در این پروژه کاربرد برای بررسی وجود فایل
import os
#کتابخانه date کاربرد برای برای مدیریت زمان و تاریخ
#در این پروژه برای کار با تاریخ‌ها و محاسبات زمانی
from datetime import date

#متغیر - نام فایلی که تمام داده‌های عادت‌ها داخلش ذخیره می شود
FILE_NAME = "habits.json"

#تابع برای بارگذاری داده ها
def load_data():
    #در صورت وجود نداشتن، برگرداندن یک دیکشنری خالی
    if not os.path.exists(FILE_NAME):
        return {}
    #در صورت وجود داشتن، خواندن داده ها از JSON و برگرداندن
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)

#تابع برای ذخیره داده‌های دیکشنری data در فایل JSON
def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        #با ensure_ascii=False کاراکترهای فارسی خراب نمیشن
        json.dump(data, f, ensure_ascii=False, indent=2)

#تابع برای افزودن عادت جدید از کاربر، با بررسی اینکه قبلاً وجود داشته یا نه
def add_habit(data):
    name = input("نام عادت: ").strip()
    if name in data:
        print("این عادت قبلاً وجود دارد!")
        return
    #در صورت جدید بودن عادت، ایجاد یک لیست خالی برای ثبت روزها
    data[name] = []
    print("عادت با موفقیت اضافه شد.")

#تابع برای ثبت عادت های روز
def mark_today(data):
    #گرفتن تاریخ امروز
    today = str(date.today())
    if not data:
        print("هیچ عادتی ثبت نشده.")
        return
#نمایش لیست عادت‌ها و انتخاب شماره
    for i, habit in enumerate(data.keys(), 1):
        print(f"{i}. {habit}")

    choice = int(input("شماره عادت: "))
    habit_name = list(data.keys())[choice - 1]
#بررسی اینکه امروز برای اون عادت قبلاً ثبت شده یا نه، در صورت ثبت نشدن ثبت می‌کنه
    if today not in data[habit_name]:
        data[habit_name].append(today)
        print("برای امروز ثبت شد ✅")
    else:
        print("امروز قبلاً ثبت شده.")

#تابع برای گزارش گیری از هر عادت
def report(data):
    if not data:
        print("داده‌ای وجود ندارد.")
        return

    today = date.today()
    for habit, days in data.items():
        total_days = (today - date.fromisoformat(min(days))) .days + 1 if days else 0
        #ارائه تعداد روزهای ثبت‌شده
        done = len(days)
        #ارائه درصد پایبندی (نسبت انجام‌شده به کل روزها از اولین ثبت)
        percent = (done / total_days * 100) if total_days else 0

        print("-" * 30)
        print(f"عادت: {habit}")
        print(f"روزهای انجام‌شده: {done}")
        print(f"پایبندی: {percent:.1f}%")

#بخش منو و اجرای برنامه
def main():
    data = load_data()
#اجرای منو اصلی در حلقه
    while True:
        print("\n--- Habit Tracker ---")
        print("1. افزودن عادت")
        print("2. ثبت انجام عادت امروز")
        print("3. گزارش")
        print("4. خروج") # شماره‌گذاری اصلاح شد

        choice = input("انتخاب: ")
#فراخوانی توابع بر اساس انتخاب کاربر و بروزرسانی فایل بعد از هر عمل
        if choice == "1":
            add_habit(data)
        elif choice == "2":
            mark_today(data)
        elif choice == "3":
            report(data)
        elif choice == "4": # گزینه خروج
            save_data(data)
            print("خداحافظ 👋")
            break
        else:
            print("انتخاب نامعتبر!")

        # ذخیره داده‌ها پس از هر عملیات به جز خروج
        if choice in ["1", "2", "3"]:
            save_data(data)

#تضمین اجرای تابع main() با اجرای این فایل
if __name__ == "__main__":
    main()