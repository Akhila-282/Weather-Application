import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as tkb
import customtkinter

## 🌦️ get_weather function
def get_weather(city):
    API_key = "05f4ee67848cc2f2685db6e4c1cf5f3e"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error ❌", "City not found!")
        return None
    
    ## 🌐 Parse info into JSON
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    ## 🖼️ get icon and return weather information
    icon = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon, temperature, description, city, country)

## 📡 Search Function
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result == None:
        return
    icon, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    ## 🌡️ getting the weather icon from the URL
    image = Image.open(requests.get(icon, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    ## 🌡️ updating temperature and description info
    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")

root = tkb.Window(themename="flatly")  # Change the theme to "aqua"
root.title("Weather App ☀️🌧️🌡️")
root.geometry("400x400")
root.iconbitmap('empty.ico')

city_entry = tkb.Entry(root, font="Helvetica 18")
city_entry.insert(0, "🏙️ Enter City Name")  # Add a placeholder with an emoji
city_entry.bind("<FocusIn>", lambda event: city_entry.delete(0, "end"))  # Remove the placeholder on focus
city_entry.pack(pady=10)

## Search Button
search_btn = tkb.Button(root, text="Search 📌", command=search, bootstyle="Warning")
search_btn.pack(pady=10)

## Show name of city/country
location_label = tk.Label(root, font="Helvetica 25")
location_label.pack(pady=20)

## Show icon 
icon_label = tk.Label(root)
icon_label.pack()

## Show temperature
temperature_label = tk.Label(root, font="Helvetica 20")
temperature_label.pack()

## Show description
description_label = tk.Label(root, font="Helvetica 20")
description_label.pack()

root.resizable(False, False)
root.mainloop()
