
# Weather App

A simple weather application built using **Flask**, which allows users to check the weather of any city by entering the city's name. The app fetches real-time weather data from the **OpenWeatherMap API**.

---

## Features

- Enter any city name to get real-time weather information like temperature, humidity, and weather conditions.
- Built using **Python**, **Flask**, and **OpenWeatherMap API**.
- **Responsive design** to fit on all devices.

---

## Requirements

To run the Weather App locally, you need the following:

- **Python 3.x**
- **Flask** for web development
- **requests** to make HTTP requests
- **python-dotenv** to manage environment variables securely

---

## Installation Steps

Follow these steps to get the Weather App running locally:

1. **Clone the repository:**

   Open your terminal or command prompt and run:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   ```

2. **Navigate into the project directory:**

   ```bash
   cd weather-app
   ```

3. **Install the required Python packages:**

   It's recommended to set up a **virtual environment** first, then install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the `.env` file:**

   - Create a `.env` file in the root directory of your project.
   - Go to [OpenWeatherMap](https://openweathermap.org/) and sign up for an API key.
   - Add the following line to your `.env` file:
     ```bash
     API_KEY=your_api_key_here
     ```

5. **Run the application:**

   In the project folder, run the app:
   ```bash
   python main.py
   ```

6. **Access the app:**

   The app will run locally on your machine. Open your browser and use the appropriate URL to access it.

## License

This project is open-source and available under the [MIT License].

---

### Notes:

- Replace `your_api_key_here` with your actual OpenWeatherMap API key.
- The app will run on your local server.

