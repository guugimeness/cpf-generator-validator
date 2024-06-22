# cpf-generator-validator

## About

CPF generator and validator project intended to help students, programmers, analysts and testers. I used [PySide6](https://pypi.org/project/PySide6/) for the GUI and the logic used to create CPF numbers.

**Warning:** The misuse of data generated here is the sole responsibility of the user.

## Visuals

<p align="center">
  <img src="https://github.com/guugimeness/cpf-generator-validator/blob/82efa47e80b1046bc102910dcf81d88dd07f368a/assets/generate-punc.png" alt="Image">
</p>

<p align="center">
  <img src="https://github.com/guugimeness/cpf-generator-validator/blob/82efa47e80b1046bc102910dcf81d88dd07f368a/assets/generate-nopunc.png" alt="Image">
</p>

## Installation

```bash
# Clone this repository
$ git clone https://github.com/guugimeness/cpf-generator-validator.git

# Access the project folder in your terminal
$ cd cpf-generator-validator

# Create and activate your virtual environment
$ python3 -m venv venv
$ source venv/bin/activate

# Install the dependencies using pip
$ pip install -r requirements.txt

# Use PyInstaller to create the calculator executable
$ pyinstaller Gerador\ e\ Validador\ -\ CPF.spec

# The application will be created in /dist
```

## Tech Stack

The following tools were used in the construction of the project:
* [Python](https://www.python.org/)
* [PySide6](https://pypi.org/project/PySide6/)
* [PyInstaller](https://pyinstaller.org/en/stable/)

## License

This project is under the license [MIT](./LICENSE)

## Status: 50% (Validation part is missing)