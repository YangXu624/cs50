Title: Calculator.py
Video Demo:  <https://youtu.be/udmRjlP1CrM?si=mjBkeZFe2BBPkJqH>
Description:

This project is a web-based calculator application built using the Flask framework. The calculator allows users to perform basic arithmetic operations, advanced mathematical functions, and trigonometric calculations. It features three distinct modes: main, shift, and alpha, each offering a set of functionalities tailored for specific mathematical tasks.

The main mode handles essential calculator functions such as addition, subtraction, multiplication, division, and displays the result. Users can also delete the last entered digit or reset the calculation to zero. Shift mode enables users to perform trigonometric operations like sine, cosine, and tangent, as well as square root and cube root calculations. Alpha mode supports advanced operations, including square, cube, natural logarithm, factorial, and absolute value.

To manage transitions between modes and retain the current calculation, the project uses a global variable 'pv', which stores the result from one mode and passes it to another. For example, if the user performs a trigonometric calculation in shift mode, the result can be retained and used when switching back to main mode or moving to alpha mode.

Additionally, the project utilizes Python's 'math' module for evaluating mathematical functions and a custom rounding function 'dp()' to round results to five decimal places. This ensures that users receive precise answers without excessive decimal expansion.

In the future, the project can be enhanced by adding features such as memory storage** for saving and recalling previous results, a history log for tracking past calculations, and more advanced mathematical functions like exponential and logarithmic calculations in various bases. Additionally, implementing a graphical interface using JavaScript or a front-end framework like React would improve the user experience by making the calculator more interactive and responsive. Another possible improvement is optimizing the application's error handling, ensuring that users receive clearer messages for invalid inputs or calculations, and expanding the mobile-friendly interface for better accessibility on various devices.
