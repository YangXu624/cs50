Title: Calculator.py
Video Demo:  <https://youtu.be/udmRjlP1CrM?si=mjBkeZFe2BBPkJqH>
Description:

This project is a web-based calculator application built using the Flask framework. The calculator allows users to perform basic arithmetic operations, advanced mathematical functions, and trigonometric calculations. It features three distinct modes: main, shift, and alpha, each offering a set of functionalities tailored for specific mathematical tasks.

The main mode handles essential calculator functions such as addition, subtraction, multiplication, division, and displays the result. Users can also delete the last entered digit or reset the calculation to zero. Shift mode enables users to perform trigonometric operations like sine, cosine, and tangent, as well as square root and cube root calculations. Alpha mode supports advanced operations, including square, cube, natural logarithm, factorial, and absolute value.

To manage transitions between modes and retain the current calculation, the project uses a global variable 'pv', which stores the result from one mode and passes it to another. For example, if the user performs a trigonometric calculation in shift mode, the result can be retained and used when switching back to main mode or moving to alpha mode.

Additionally, the project utilizes Python's 'math' module for evaluating mathematical functions and a custom rounding function 'dp()' to round results to five decimal places. This ensures that users receive precise answers without excessive decimal expansion.
