import json

import requests


response = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
data = response.json()


for val in data:
    if val["Ccy"] == "USD":
        usd_rate = float(val["Rate"])
        date = val["Date"]
    elif val["Ccy"] == "EUR":
        eur_rate = float(val["Rate"])


while True:
    print("\nValyuta turini tanlang !")
    choice1 = input("1: UZS || 2: USD || 3: EUR || -> ").strip()

    if choice1 not in ["1", "2", "3"]:
        print("❌ Valyuta raqamini to`gri kiriting!")
        continue

    if choice1 == "1":
        from_currency = "UZS"
    elif choice1 == "2":
        from_currency = "USD"
    elif choice1 == "3":
        from_currency = "EUR"

    print("\nQaysi valyutaga o'tkazmoqchisiz?")
    choice2 = input("1: UZS || 2: USD || 3: EUR || -> ").strip()

    if choice2 not in ["1", "2", "3"]:
        print("❌ Valyuta raqamini to`g`ri kiriting!")
        continue

    if choice2 == "1":
        to_currency = "UZS"
    elif choice2 == "2":
        to_currency = "USD"
    elif choice2 == "3":
        to_currency = "EUR"

    # Agar Valyutalar turi bir xil bo`lib qolsa bizga dasturimiz  
    # bunday qilish mumkin emasligini ko`rsatish uchun yozilgan kod
    if from_currency == to_currency:
        print("Valyutalar turli xil bo`lishi kerak!")
        continue

    try:
        amount = float(input(f"\n{from_currency} miqdorini kiriting: "))
    except ValueError:
        print("❌ Noto`g`ri son kiritildi!")
        continue

    if from_currency == "UZS" and to_currency == "USD":
        result = amount / usd_rate
    elif from_currency == "UZS" and to_currency == "EUR":
        result = amount / eur_rate
    elif from_currency == "USD" and to_currency == "UZS":
        result = amount * usd_rate
    elif from_currency == "EUR" and to_currency == "UZS":
        result = amount * eur_rate
    elif from_currency == "USD" and to_currency == "EUR":
        result = (amount * usd_rate) / eur_rate
    elif from_currency == "EUR" and to_currency == "USD":
        result = (amount * eur_rate) / usd_rate
    else:
        print("❌ Bunday amal bajarib bo`lmaydi!")
        continue

    print(f"\n✅ {amount:,.2f} {from_currency} = {result:,.2f} {to_currency} ({date})")

    next_step = input("\nYana hisoblashni xohlaysizmi? (1: ha/ 2: yo`q): ").lower().strip()
    if next_step != "1":
        print("Dastur tugadi...")
        break
