<!-- @format -->

# GPA Calculation Web App

This is a simple web application for calculating the GPA (Grade Point Average) of a student based on their grades in different subjects. The application is built using **Streamlit**, a Python library that allows you to create interactive web applications.

## Features

- **User-Friendly Interface**: The app allows users to input their grades for different subjects through an easy-to-use interface with number inputs.
- **Responsive Design**: The app uses columns to neatly organize the input fields for different subjects.
- **GPA Calculation**: With a click of a button, the app calculates and displays the GPA of the student.

## Subjects Included

The app includes input fields for the following subjects:

- English
- Mathematics
- Science
- History
- Geography
- Art and Design
- Music
- Physical Education
- Information Technology

## How It Works

1. **Enter Grades**: The user enters their grades for each subject using number inputs (values range from 0 to 20).
2. **GPA Calculation**: When the user clicks the "GPA calculation" button, the app calculates the average of the entered grades and displays the GPA.
3. **Result**: The GPA is displayed in a success message, rounded to two decimal places.

## Technologies Used

- **Python**: The core programming language used for building the app.
- **Streamlit**: A Python library for creating web applications quickly and easily.

## Installation

To run this app on your local machine, follow these steps:

1. Clone this repository:

   git clone https://github.com/AliFathi1325/GPA_Calculation_Program_Streamlit.git

2. Navigate to the project directory:

   cd gpa-calculation-app

3. Install the required Python packages:

   pip install -r requirements.txt

4. Run the app using Streamlit:

   streamlit run app.py

## Example

Once the app is running, you will see a web interface where you can input grades for different subjects. After entering the grades, press the "GPA calculation" button to get your GPA displayed in real-time.
