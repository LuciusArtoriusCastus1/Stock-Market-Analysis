def refine_text(text):
    return text.replace('\n', '').strip()


def refine_numbers(text):
    text = (text.replace('\n', '').replace(' ', '')
            .replace('$', '').replace('%', '').replace(',', '.'))
    if 'N/A' in text:
        return None
    elif 'T' in text:
        return float(text.replace('T', '')) * 10**12
    elif 'B' in text:
        return float(text.replace('B', '')) * 10**9
    elif 'M' in text:
        return float(text.replace('M', '')) * 10**6
    else:
        return float(text)
