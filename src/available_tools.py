available_tools = [
    {
        "type": "function",
        "function": {
            "name": "convert_temperature_units",
            "description": "Convert a temperature between Celsius, Fahrenheit, and Kelvin.",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "The numeric temperature value to convert."
                    },
                    "unit_from": {
                        "type": "string",
                        "description": "The current unit of the temperature. Must be 'celsius', 'fahrenheit', or 'kelvin'."
                    },
                    "unit_to": {
                        "type": "string",
                        "description": "The unit to convert the temperature to. Must be 'celsius', 'fahrenheit', or 'kelvin'."
                    }
                },
                "required": ["value", "unit_from", "unit_to"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "convert_distance_units",
            "description": "Convert a distance between metres, feet, and miles.",
            "parameters": {
                "type": "object",
                "properties": {
                    "value": {
                        "type": "number",
                        "description": "The numeric distance value to convert."
                    },
                    "unit_from": {
                        "type": "string",
                        "description": "The current unit of the distance. Must be 'meters', 'feet', or 'miles'."
                    },
                    "unit_to": {
                        "type": "string",
                        "description": "The unit to convert the distance to. Must be 'meters', 'feet', or 'miles'."
                    }
                },
                "required": ["value", "unit_from", "unit_to"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform a mathematical operation (add, subtract, multiply, divide) on two numbers.",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["add", "subtract", "multiply", "divide"],
                        "description": "The operation to perform: 'add', 'subtract', 'multiply', or 'divide'."
                    },
                    "x": {
                        "type": "number",
                        "description": "The first number."
                    },
                    "y": {
                        "type": "number",
                        "description": "The second number."
                    }
                },
                "required": ["operation", "x", "y"]
            }
        }
    }
]