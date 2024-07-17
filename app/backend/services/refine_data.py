def refine_text(text):
    return text.replace('\n', '').strip()


def refine_numbers(text):
    multipliers = {'T': 10 ** 12, 'B': 10 ** 9, 'M': 10 ** 6}
    text = (text.replace('\n', '').replace(' ', '')
            .replace('$', '').replace('%', '').replace(',', '.'))

    if 'N/A' in text:
        return None
    for key, multiplier in multipliers.items():
        if key in text:
            return float(text.replace(key, '')) * multiplier

    return float(text)
