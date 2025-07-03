# A function to convert temperature units
def convert_temperature_units(value, unit_from, unit_to):
    """Convert a value from one temperature unit to another."""
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()
    VALID_UNITS = {"celsius", "fahrenheit", "kelvin"}

    if unit_from not in VALID_UNITS or unit_to not in VALID_UNITS:
        raise ValueError(f"Invalid unit(s): {unit_from} or {unit_to}")

    if unit_from == unit_to:
        return {"value": value, "unit": unit_to}

    if unit_from == "celsius":
        if unit_to == "fahrenheit":
            return {"value": value * 9 / 5 + 32, "unit": "fahrenheit"}
        elif unit_to == "kelvin":
            return {"value": value + 273.15, "unit": "kelvin"}

    elif unit_from == "fahrenheit":
        if unit_to == "celsius":
            return {"value": (value - 32) * 5 / 9, "unit": "celsius"}
        elif unit_to == "kelvin":
            return {"value": (value - 32) * 5 / 9 + 273.15, "unit": "kelvin"}

    elif unit_from == "kelvin":
        if unit_to == "celsius":
            return {"value": value - 273.15, "unit": "celsius"}
        elif unit_to == "fahrenheit":
            return {"value": (value - 273.15) * 9 / 5 + 32, "unit": "fahrenheit"}

    raise ValueError(f"Conversion from {unit_from} to {unit_to} is not supported.")
