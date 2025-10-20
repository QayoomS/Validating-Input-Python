# Validating-Input-Python

How to validate input in Python:

A simple Python program that asks the user to pick an integer within a defined range (by default 1 to 10) and validates their input.
It ensures the user enters a valid integer and checks whether it lies within the allowed range.

🚀 How It Works: 

The program defines a minimum and maximum number.

It repeatedly asks the user to input an integer.

If the user enters something that’s not an integer, it shows an error message.

If the number is outside the range, it prompts again.

Once a valid number within range is entered, the program confirms and ends.

🧠 Example
Pick an integer between 1 and 10 : 15

Your integer is not between 1 and 10

Pick an integer between 1 and 10 : five

You did not enter a valid integer 

Pick an integer between 1 and 10 : 7

Your integer is between 1 and 10 

Program completed. you chose: 7


🛠️ Requirements

Python 3.x

Run the program:

python file

⚙️ Customization

You can change the allowed range by editing these lines in the script:

min_n, max_n = 1, 10

📄 License

This project is open-source and available under the MIT License. 

Inspired by:
University of Galway, Foundamental of Python lecture notes.
