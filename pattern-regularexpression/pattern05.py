import traceback

def find_error_in_program(code):
    try:
        exec(code)
        print("No errors found in the program.")
    except Exception as e:
        print("Error found in the program:")
        print(traceback.format_exc())

# Example usage
program_code = """
a = 10
b = 0
c = a / b  # This will raise a ZeroDivisionError
"""

find_error_in_program(program_code)