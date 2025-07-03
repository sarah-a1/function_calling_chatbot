# A function to convert distance units
def convert_distance_units(value, unit_from, unit_to):
    """Convert a value from one distance unit to another."""
    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    if unit_from == unit_to:
        return {
            "value": value,
            "unit": unit_to,
        }

    if unit_from == "meters":
        if unit_to == "feet":
            return {
                "value": value * 3.28084,
                "unit": "feet",
            }
        elif unit_to == "miles":
            return {
                "value": value / 1609.34,
                "unit": "miles",
            }

    elif unit_from == "feet":
        if unit_to == "meters":
            return {
                "value": value / 3.28084,
                "unit": "meters",
            }
        elif unit_to == "miles":
            return {
                "value": value / 5280,
                "unit": "miles",
            }

    elif unit_from == "miles":
        if unit_to == "meters":
            return {
                "value": value * 1609.34,
                "unit": "meters",
            }
        elif unit_to == "feet":
            return {
                "value": value * 5280,
                "unit": "feet",
            }
        
    raise ValueError(f"Conversion from {unit_from} to {unit_to} is not supported.")