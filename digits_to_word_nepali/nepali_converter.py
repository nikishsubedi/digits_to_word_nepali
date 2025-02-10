class NumberConverter:
    _instance = None

    units_nepali = {
        0: ("zero", "सुन्ना"),
        1: ("one", "एक"),
        2: ("two", "दुई"),
        3: ("three", "तीन"),
        4: ("four", "चार"),
        5: ("five", "पाँच"),
        6: ("six", "छ"),
        7: ("seven", "सात"),
        8: ("eight", "आठ"),
        9: ("nine", "नौ"),
        10: ("ten", "दश"),
        11: ("eleven", "एघार"),
        12: ("twelve", "बाह्र"),
        13: ("thirteen", "तेह्र"),
        14: ("fourteen", "चौध"),
        15: ("fifteen", "पन्ध्र"),
        16: ("sixteen", "सोह्र"),
        17: ("seventeen", "सत्र"),
        18: ("eighteen", "अठार"),
        19: ("nineteen", "उन्नाइस"),
        20: ("twenty", "बीस"),
        21: ("twenty one", "एक्काइस"),
        22: ("twenty two", "बाइस"),
        23: ("twenty three", "तेइस"),
        24: ("twenty four", "चौबिस"),
        25: ("twenty five", "पच्चिस"),
        26: ("twenty six", "छब्बिस"),
        27: ("twenty seven", "सत्ताइस"),
        28: ("twenty eight", "अट्ठाइस"),
        29: ("twenty nine", "उनन्तिस"),
        30: ("thirty", "तीस"),
        31: ("thirty one", "एकत्तिस"),
        32: ("thirty two", "बत्तिस"),
        33: ("thirty three", "तेत्तिस"),
        34: ("thirty four", "चौँतिस"),
        35: ("thirty five", "पैँतिस"),
        36: ("thirty six", "छत्तिस"),
        37: ("thirty seven", "सैँतिस"),
        38: ("thirty eight", "अठतिस"),
        39: ("thirty nine", "उनन्चालीस"),
        40: ("forty", "चालीस"),
        41: ("forty one", "एकचालीस"),
        42: ("forty two", "बयालिस"),
        43: ("forty three", "त्रिचालीस"),
        44: ("forty four", "चवालीस"),
        45: ("forty five", "पैँतालीस"),
        46: ("forty six", "छयालीस"),
        47: ("forty seven", "सतचालीस"),
        48: ("forty eight", "अठचालीस"),
        49: ("forty nine", "उनन्चास"),
        50: ("fifty", "पचास"),
        51: ("fifty one", "एकाउन्न"),
        52: ("fifty two", "बाउन्न"),
        53: ("fifty three", "त्रिपन्न"),
        54: ("fifty four", "चवन्न"),
        55: ("fifty five", "पचपन्न"),
        56: ("fifty six", "छपन्न"),
        57: ("fifty seven", "सन्ताउन्न"),
        58: ("fifty eight", "अन्ठाउन्न"),
        59: ("fifty nine", "उनन्साठी"),
        60: ("sixty", "साठी"),
        61: ("sixty one", "एकसट्ठी"),
        62: ("sixty two", "बयसट्ठी"),
        63: ("sixty three", "त्रिसट्ठी"),
        64: ("sixty four", "चौंसट्ठी"),
        65: ("sixty five", "पैंसट्ठी"),
        66: ("sixty six", "छयसट्ठी"),
        67: ("sixty seven", "सतसट्ठी"),
        68: ("sixty eight", "अठसट्ठी"),
        69: ("sixty nine", "उनन्सत्तरी"),
        70: ("seventy", "सत्तरी"),
        71: ("seventy one", "एकहत्तर"),
        72: ("seventy two", "बहत्तर"),
        73: ("seventy three", "त्रिहत्तर"),
        74: ("seventy four", "चौहत्तर"),
        75: ("seventy five", "पचहत्तर"),
        76: ("seventy six", "छयहत्तर"),
        77: ("seventy seven", "सतहत्तर"),
        78: ("seventy eight", "अठहत्तर"),
        79: ("seventy nine", "उनासी"),
        80: ("eighty", "असी"),
        81: ("eighty one", "एकासी"),
        82: ("eighty two", "बयासी"),
        83: ("eighty three", "त्रियासी"),
        84: ("eighty four", "चौरासी"),
        85: ("eighty five", "पचासी"),
        86: ("eighty six", "छयासी"),
        87: ("eighty seven", "सतासी"),
        88: ("eighty eight", "अठासी"),
        89: ("eighty nine", "उनान्नब्बे"),
        90: ("ninety", "नब्बे"),
        91: ("ninety one", "एकान्नब्बे"),
        92: ("ninety two", "बयानब्बे"),
        93: ("ninety three", "त्रियान्नब्बे"),
        94: ("ninety four", "चौरान्नब्बे"),
        95: ("ninety five", "पन्चान्नब्बे"),
        96: ("ninety six", "छयान्नब्बे"),
        97: ("ninety seven", "सन्तान्नब्बे"),
        98: ("ninety eight", "अन्ठान्नब्बे"),
        99: ("ninety nine", "उनान्सय"),
    }

    scales_nepali = {
        100: ("hundred", "सय"),
        1000: ("thousand", "हजार"),
        100000: ("lakh", "लाख"),
        10000000: ("crore", "करोड"),
        1000000000: ("arab", "अरब"),
        100000000000: ("kharab", "खरब"),
        10000000000000: ("neel", "नील"),
        1000000000000000: ("padma", "पद्म"),
        10**17: ("shankha", "शंख"),
        10**19: ("udpadh", "उपाध"),
        10**21: ("ank", "अंक"),
        10**23: ("jald", "जल्द"),
        10**25: ("madh", "मध"),
        10**27: ("paraardha", "परार्ध"),
        10**29: ("ant", "अन्त"),
        10**31: ("maha ant", "महाअन्त"),
        10**33: ("shishant", "शिशान्त"),
        10**35: ("singhar", "सिंघर"),
        10**37: ("maha singhar", "महासिंघर"),
        10**39: ("adanta singhar", "अदन्त सिंघर"),
    }

    number_scales = [
        {'value': 10**39, 'names': {'en': 'adanta singhar', 'ne': 'अदन्त सिंघर'}},
        {'value': 10**37, 'names': {'en': 'maha singhar', 'ne': 'महासिंघर'}},
        {'value': 10**35, 'names': {'en': 'singhar', 'ne': 'सिंघर'}},
        {'value': 10**33, 'names': {'en': 'shishant', 'ne': 'शिशान्त'}},
        {'value': 10**31, 'names': {'en': 'maha ant', 'ne': 'महाअन्त'}},
        {'value': 10**29, 'names': {'en': 'ant', 'ne': 'अन्त'}},
        {'value': 10**27, 'names': {'en': 'paraardha', 'ne': 'परार्ध'}},
        {'value': 10**25, 'names': {'en': 'madh', 'ne': 'मध'}},
        {'value': 10**23, 'names': {'en': 'jald', 'ne': 'जल्द'}},
        {'value': 10**21, 'names': {'en': 'ank', 'ne': 'अंक'}},
        {'value': 10**19, 'names': {'en': 'udpadh', 'ne': 'उपाध'}},
        {'value': 10**17, 'names': {'en': 'shankha', 'ne': 'शंख'}},
        {'value': 10**15, 'names': {'en': 'padma', 'ne': 'पद्म'}},
        {'value': 10**13, 'names': {'en': 'neel', 'ne': 'नील'}},
        {'value': 10**11, 'names': {'en': 'kharab', 'ne': 'खरब'}},
        {'value': 10**9, 'names': {'en': 'arab', 'ne': 'अरब'}},
        {'value': 10**7, 'names': {'en': 'crore', 'ne': 'करोड'}},
        {'value': 10**5, 'names': {'en': 'lakh', 'ne': 'लाख'}},
        {'value': 10**3, 'names': {'en': 'thousand', 'ne': 'हजार'}},
        {'value': 10**2, 'names': {'en': 'hundred', 'ne': 'सय'}},
    ]

    language_configs = {
        'ne': {
            'currency': 'रुपैयाँ',
            'decimal_suffix': 'दशमलव',
            'currency_decimal_suffix': 'पैसा'
        },
        'en': {
            'currency': 'Rupees',
            'decimal_suffix': 'point',
            'currency_decimal_suffix': 'cents'
        }
    }

    digit_map = {
        '0': '०', '1': '१', '2': '२', '3': '३', '4': '४',
        '5': '५', '6': '६', '7': '७', '8': '८', '9': '९'
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.word_cache = {k: {'en': v[0], 'ne': v[1]} 
                for k, v in cls.units_nepali.items()}
        return cls._instance

    def convert_to_words(self, num, config):
        try:
            if not self.is_valid_number(num):
                raise ValueError("Input must contain only valid digits")

            # Handle negative numbers
            if isinstance(num, (int, float)) and num < 0:
                raise ValueError("Negative numbers are not supported")

            parts = self.split_number(num)
            words = self.convert_integer_part(parts['integer'], config)

            if config['include_decimal'] and parts['decimal'] is not None:
                self.append_decimal_part(words, parts['decimal'], config)

            return self.format_result(words, config)
        except Exception as e:
            raise e

    def is_valid_number(self, num):
        if isinstance(num, (int, float)) and (num != num or abs(num) == float('inf')):
            return False

        str_num = str(num).lstrip('-')
        if '.' in str_num:
            integer_part, decimal_part = str_num.split('.', 1)
            if not integer_part.isdigit() or not decimal_part.isdigit():
                return False
        elif not str_num.isdigit():
            return False

        return True

    def split_number(self, num):
        str_num = str(num)
        if num < 0:
            raise ValueError("Negative numbers are not supported")
            
        if '.' in str_num:
            integer_part, decimal_part = str_num.split('.', 1)
            # Round to 2 decimal places if more digits exist
            decimal_float = float('0.' + decimal_part)
            decimal_part = f"{decimal_float:.2f}".split('.')[1]
            
            # Pad single decimal digit with zero
            if len(decimal_part) == 1:
                decimal_part += '0'
                
            return {
                'integer': int(integer_part),
                'decimal': decimal_part
            }
        return {'integer': int(str_num), 'decimal': None}

    def convert_integer_part(self, num, config):
        if num == 0:
            return [self.get_word_mapping(0, config['lang'])]

        if num <= 99:
            return [self.get_word_mapping(num, config['lang'])]

        words = []
        remaining = num

        for scale in self.number_scales:
            scale_value = scale['value']
            if remaining < scale_value:
                continue

            quotient = remaining // scale_value
            remaining = remaining % scale_value

            if quotient > 0:
                quotient_words = self.convert_to_words(
                    quotient, {**config, 'is_currency': False, 'include_decimal': False}
                )
                scale_name = scale['names'][config['lang']]
                words.append(f"{quotient_words} {scale_name}")

        if remaining > 0:
            words.append(self.get_word_mapping(remaining, config['lang']))

        return words

    def append_decimal_part(self, words, decimal, config):
        suffix = (config['currency_decimal_suffix'] 
                if config['is_currency'] else config['decimal_suffix'])
        words.append(suffix)

        if not decimal or decimal == '0':
            words.append(self.get_word_mapping(0, config['lang']))
            return

        if config['is_currency']:
            decimal_num = int((decimal + '00')[:2])
        else:
            decimal_num = int(decimal)

        # Ensure decimal part uses the same language as the integer part
        words.append(self.get_word_mapping(decimal_num, config['lang']))

    def format_result(self, words, config):
        result = ' '.join(words).strip()
        if config['is_currency']:
            return f"{config['currency']} {result}".strip()
        return result

    def get_word_mapping(self, num, lang):
        if num not in self.word_cache:
            raise ValueError(f"No word mapping found for number: {num}")
        return self.word_cache[num][lang]

def unicode_to_english_number(num_str):
    nepali_digits = {'०':'0', '१':'1', '२':'2', '३':'3', '४':'4', 
                    '५':'5', '६':'6', '७':'7', '८':'8', '९':'9'}
    
    if not num_str or not isinstance(num_str, str):
        raise ValueError("Input must be a non-empty string")
    
    for char in num_str:
        if char not in nepali_digits and char != '.':
            raise ValueError("Input must contain only Nepali digits (०-९)")
    
    return int(''.join(nepali_digits[char] for char in num_str))

def digit_to_nepali_words(num, config=None):
    converter = NumberConverter()
    config = config or {}
    lang = config.get('lang', 'ne')
    default_config = converter.language_configs[lang]  # Use language-specific defaults
    
    merged_config = {
        'lang': lang,
        'is_currency': config.get('is_currency', False),
        'include_decimal': config.get('include_decimal', False),
        'currency': config.get('currency', default_config['currency']),
        'decimal_suffix': config.get('decimal_suffix', default_config['decimal_suffix']),
        'currency_decimal_suffix': config.get('currency_decimal_suffix', 
            default_config['currency_decimal_suffix'])
    }

    return converter.convert_to_words(num, merged_config)

# Test cases
if __name__ == "__main__":
    try:
        print(digit_to_nepali_words(1234.56, {'lang': 'en', 'include_decimal': True}))  # English with decimals
        print(digit_to_nepali_words(-1234))  # Negative number (should throw error)
    except ValueError as e:
        print(f"Error: {e}")