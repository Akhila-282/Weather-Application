# Weather App ☀️🌧️🌡️

This Python program is a simple weather application that allows you to check the current weather for a city. It uses the OpenWeatherMap API to fetch weather information for a specified city and displays it in a user-friendly graphical interface built with the Tkinter library.

## Features 🌐
- Get the current weather for a city 🏙️.
- Display temperature in Celsius 🌡️.
- Show a weather icon to represent the current conditions 🌤️.
- Provide a description of the weather conditions 📋.
- Display the name of the city and its country 🌍.

## Installation 🛠️
This program requires the following Python libraries to be installed:
- tkinter
- requests
- PIL (Pillow)
- ttkbootstrap

You can install the required packages using pip:
```bash
pip install tkinter
pip install requests
pip install pillow
pip install ttkbootstrap
```

## Usage 💻
1. Run the program using a Python interpreter:

```bash
python weather_app.py
```

2. Enter the name of the city and click the "Search" button to fetch and display the weather information.

## API Key
This application uses the OpenWeatherMap API to fetch weather data. You need to obtain an API key from OpenWeatherMap and replace the `API_key` variable in the code with your own API key.

```python
API_key = "YOUR_API_KEY"
```


## License 📄
This project is open-source and available under the [MIT License](LICENSE).

## Credits 💡
- Python: [python.org](https://www.python.org/)
- Tkinter: [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- OpenWeatherMap API: [OpenWeatherMap](https://openweathermap.org/)
- ttkbootstrap: [ttkbootstrap Documentation](https://ttkbootstrap.com/)

Enjoy checking the weather with this simple and stylish weather app! 🌞🌧️🌈

---

## Compiling the Python File into an Executable (`.exe`) 🚀

If you want to share your Weather App with others who may not have Python installed, you can compile it into an executable file. We'll use the `auto-py-to-exe` tool to do this.

### Prerequisites 📦

Before proceeding, ensure that you have `auto-py-to-exe` installed. If you don't have it installed, you can install it using pip:

```bash
pip install auto-py-to-exe
```

### Compilation Steps 🛠️

1. Open a terminal/command prompt.

2. Run `auto-py-to-exe` by entering the following command:

   ```bash
   auto-py-to-exe
   ```

   This will open the `auto-py-to-exe` graphical user interface.

3. Configure the settings in the `auto-py-to-exe` interface according to your preferences. You can specify the source Python script (in this case, `weather_app.py`) and customize other options as needed.

4. In the "Advanced" settings, you can add emojis to your graphical interface. Here's how you can do it:

   - For Tkinter buttons and labels, you can use emojis directly in the text, for example:
     - `"Search 🌍"` or `"Get Weather 🌤️"`

5. Once you're satisfied with the configuration, click the "Convert .py to .exe" button.

6. `auto-py-to-exe` will compile your Python script into an executable. You can find the output files in the "Output" folder.

### Running the Compiled Executable 🏃‍♂️

To run the compiled executable:

1. Navigate to the "Output" folder created by `auto-py-to-exe`.

2. You will find a file named `main.exe`. This is your compiled Weather App.

3. Double-click on `main.exe` to launch the application.

4. You can now use your Weather App without needing to install Python or any additional libraries.

Remember that the emojis will be displayed in the user interface as you configured them during the compilation.

Enjoy using your Weather App with emojis! 🌞🌧️🌈

---

This guide explains how to compile your Python program into an executable using `auto-py-to-exe` and how to add emojis to the user interface to enhance the user experience. Users will find the compiled executable in the "Output" folder, and they can run it without needing to install Python or any additional dependencies.
