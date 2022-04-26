import roman

def get_greater_roman(text: str) -> dict:
    """ Get the greater Roman value within a string """

    valid_romans = ["I", "V", "X", "L", "C", "D", "M"]

    text_romans = ""
    for x in text:
        if x in valid_romans:
            text_romans += x
        else :
            text_romans += "-"

    list_romans = list(text_romans.split("-"))
    list_romans = list(filter(None, list_romans))

    try:
        max_int = 0
        max_roman = ''
        for i in list_romans:
            if roman.fromRoman(i) > max_int:
                max_int = roman.fromRoman(i)
                max_roman = i
    except Exception as e:
        return {
            "error": str(e)
        }

    return {
		"number": max_roman,
		"value": max_int,
	}
