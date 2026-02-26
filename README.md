# Python-Gauss-Kronrod-Integration
Multidimensional numerical integration in Python using Gauss–Legendre and Gauss–Kronrod quadrature rules.
## Overview
This repository provides a simple implementation of multidimensional numerical integration using the product rules of Gauss–Legendre (7-point) and Gauss–Kronrod (15-point) quadrature in Python. It demonstrates structured deterministic integration and runtime comparison for scientific computing applications.
## Features 
- Handles integration of functions in multiple dimensions.
- The user can easily edit the integrand function and integration limits.
- Compares results of Gauss–Legendre and Gauss–Kronrod quadrature rules.
- Prints result and elapsed time for performance measurement.
## Numerical Characteristics

- Uses fixed 7-point Legendre and 15-point Kronrod nodes.
- Deterministic convergence behavior (contrast to Monte Carlo sampling).
- Runtime scales with quadrature order and dimensional nesting.
- Suitable for structured evaluation of smooth integrands.
## Requirements
- Python 3.x
- NumPy
- SciPy
## Installation
To install NumPy, run:
```
pip install numpy
```
To install SciPy, run:
```
pip install scipy
```
## Usage
- Clone or download this repository.
- If needed, install the requirements.
- Edit the function f(x) in the script to change the integrand, and adjust Lower and Upper for integration limits.
- Run the script:
  ```
  python GK_GL_Python.py
  ```
## Example Output
```
Gauss-Legendre: [output value]
Gauss-Kronrod : [output value]
Precision: [output value]
Elapsed time: [output value] s
```
## Customization
- Edit the f(x) function to define the function you wish to integrate.
- Modify the Lower and Upper arrays for different integration limits or number of dimensions (by changing the length of these arrays).
## License
This project is released under the MIT License. See the LICENSE file for details.




