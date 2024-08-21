import re


def camel_case_to_snake_case(input_str: str) -> str:
    # Регулярное выражение для преобразования CamelCase в snake_case
    snake_str = re.sub(r"(?<=[a-z])(?=[A-Z])", "_", input_str)
    return snake_str.lower()

