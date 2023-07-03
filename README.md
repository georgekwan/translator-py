# Translator Script

This Python script utilizes the `translate` library to translate text from English to Korean.

## Prerequisites

- Python 3.x
- `translate` library

## Installation

1. Clone the repository or download the script file.
2. Install the required `translate` library by running the following command:
   `pip install translate`

## Usage

1. Place the text to be translated in a file named `test-input.txt`.
2. Run the script using the following command:
   `python translator_script.py`

3. The translated text will be written to a file named `test-output.txt` in UTF-8 encoding.

## Customization

- You can modify the `to_lang` parameter in the `Translator` object to translate to a different language. For example, to translate to French, set `to_lang="fr"`.
- Ensure that the input file `test-input.txt` is present in the same directory as the script. Adjust the file path if necessary.

## Troubleshooting

- If you encounter a "FileNotFoundError" with the message "check your file path silly!", please ensure that the input file `test-input.txt` is in the correct location relative to the script file.

Feel free to customize and use this script according to your requirements. Happy translating!

**Note:** Ensure that you comply with the terms and conditions of the translation service you are using.
