import pytest
from digits_to_word_nepali import digit_to_nepali_words

def test_conversion():
    assert digit_to_nepali_words(123) == "एक सय तेइस"
    assert digit_to_nepali_words(1001) == "एक हजार एक"

def test_invalid_input():
    with pytest.raises(ValueError):
        digit_to_nepali_words(-5)

if __name__ == "__main__":
    pytest.main()
