"""Core operations for the sample calculator project."""


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
    print("Sample Calculator")
    print("Enter an expression such as 12.5 * 4, or q to quit.")

    while True:
        expression = input("> ").strip()
        if expression.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            return

        parts = expression.split()
        if len(parts) != 3:
            print("Use the format: number operator number")
            continue

        try:
            left, operator, right = parts
            result = Calculator.calculate(float(left), operator, float(right))
            print(f"= {result:g}")
        except ValueError as error:
            print(f"Error: {error}")
        except ZeroDivisionError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()