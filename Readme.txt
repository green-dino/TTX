# Flask Risk Assessment Web Application

This is a simple Flask web application that allows users to perform two types of risk assessments: DREAD-based risk assessment and Risk Assessment Tool-based risk assessment. Users can input relevant data, and the application calculates the risk and displays the results.

## Features

- Perform DREAD-based risk assessment.
- Perform risk assessment using the Risk Assessment Tool.
- Displays the calculated risk values and risk levels.
- Clean and accessible user interface.

## Prerequisites

Before you can run the application, make sure you have the following dependencies installed:

- Python (3.x recommended)
- Flask (Python web framework)
- prettytable (for displaying results in tabular format)

You can install Flask and prettytable using pip:

```bash
pip install Flask prettytable

Usage

DREAD-based Risk Assessment
Enter values for Damage, Reproducibility, Exploitability, Affected Users, and Discoverability.
Click the "Calculate Risk" button.
The application will display the DREAD-based risk assessment results, including risk value and risk level.
Risk Assessment Tool
Enter values for Threat (t), Vulnerability (v), Countermeasure Effectiveness (c), and Impact (i).
Click the "Calculate Risk" button.
The application will display the Risk Assessment Tool results, including the calculated risk.
Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
See the LICENSE file for details.