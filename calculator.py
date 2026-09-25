"""Core operations for the sample calculator project."""


class DarkTheme:
    """ANSI colors for the calculator's dark terminal presentation."""

    RESET = "\033[0m"
    TEXT = "\033[38;2;226;232;240m"
    MUTED = "\033[38;2;148;163;184m"
    ACCENT = "\033[38;2;103;232;249m"
    RESULT = "\033[38;2;134;239;172m"
    ERROR = "\033[38;2;252;165;165m"

    @classmethod
    def style(cls, text: str, color: str) -> str:
        return f"{color}{text}{cls.RESET}"


class Calculator:
    """Perform basic arithmetic operations."""

    @staticmethod
    def calculate(left: float, operator: str, right: float) -> float:
        if operator == "+":
            return left + right
        if operator == "-":
            return left - right
        if operator == "*":
            return left * right
        if operator == "/":
            if right == 0:
                raise ZeroDivisionError("cannot divide by zero")
            return left / right
        raise ValueError(f"unsupported operator: {operator}")


def main() -> None:
    print(DarkTheme.style("Sample Calculator", DarkTheme.ACCENT))
    print(DarkTheme.style("Enter an expression such as 12.5 * 4, or q to quit.", DarkTheme.MUTED))

    while True:
        expression = input(DarkTheme.style("> ", DarkTheme.TEXT)).strip()
        if expression.lower() in {"q", "quit", "exit"}:
            print(DarkTheme.style("Goodbye!", DarkTheme.MUTED))
            return

        parts = expression.split()
        if len(parts) != 3:
            print(DarkTheme.style("Use the format: number operator number", DarkTheme.ERROR))
            continue

        try:
            left, operator, right = parts
            result = Calculator.calculate(float(left), operator, float(right))
            print(DarkTheme.style(f"= {result:g}", DarkTheme.RESULT))
        except ValueError as error:
            print(DarkTheme.style(f"Error: {error}", DarkTheme.ERROR))
        except ZeroDivisionError as error:
            print(DarkTheme.style(f"Error: {error}", DarkTheme.ERROR))


if __name__ == "__main__":
    main()