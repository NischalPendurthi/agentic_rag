import sympy

def calculate(expression):
    try:
        result = sympy.simplify(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"