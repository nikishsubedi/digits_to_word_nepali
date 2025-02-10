# digits_to_word_nepali

A Python package to convert digits into Nepali and English words.

## Features
- Convert numerical digits into Nepali words.
- Convert numerical digits into English words.
- Convert Nepali Unicode numbers to English numbers.
- Supports currency formatting in both Nepali and English.
- Handles decimal numbers correctly.
- Simple and easy to use.

## Installation
You can install the package using:

```sh
pip install digits_to_word_nepali
```

## Usage

```python
from digits_to_word_nepali import digit_to_nepali_words

# Convert a number to Nepali words
result = digit_to_nepali_words(1234)
print(result)  # Output: "एक हजार दुई सय चौतीस"

# Convert a number with decimals
result = digit_to_nepali_words(1234, {'include_decimal': True})
print(result)  # Output: "एक हजार दुई सय चौतीस"
```

## Running Tests
To run the tests, navigate to the project directory and use:

```sh
pytest tests/
```

Ensure you have `pytest` installed:

```sh
pip install pytest
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.