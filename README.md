# 🌤️ Weathery

> **Real-time weather information at your fingertips**

[![Python](https://img.shields.io/badge/python-3.13-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)  
[![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-API-blue)](https://openweathermap.org/api)

---

## ✨ About

**Weathery** is a **modern, liquid-glass styled weather web app** built with **Python Flask, HTML, and CSS**. Get **real-time weather information** for any city worldwide, including temperature, humidity, pressure, and precipitation.

---

## 🌟 Features

- 🔍 Search for any city worldwide  
- 🌡️ Current Weather with condition description and weather icon  
- 🌡️ Temperature in **Celsius & Fahrenheit**  
- 🤗 Feels Like temperature and **Pressure**  
- 💧 **Humidity** with dynamic progress bar  
- 🌧️ Precipitation information  
- 📱 Responsive design with **liquid glass styling**  
- ⚡ Modern UI with easy-to-read layout  

---

## 🎨 Demo

![Weathery Screenshot](demo.png)  
*Example interface showing current weather, humidity, and precipitation.*
---

## 🛠️ Installation on Development Environment

1️⃣ **Clone the repository**

```bash
git clone https://github.com/AbhishekAEDan/Weathery
cd weathery
```

2️⃣ Create a virtual environment

```bash
python -m venv venv
```

3️⃣ Activate the virtual environment
- Windows:
  ```bash
  venv\Scripts\activate
  ```
- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

5️⃣ Set up environment variables
Create a .env file in the root directory:
```bash
OPENWEATHER_API_KEY=your_openweathermap_api_key
```

## 🚀 Usage

Run the Flask app:
```bash
python app.py
```
