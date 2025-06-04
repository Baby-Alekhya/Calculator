import math

def calculate(x, op, y=None):
    try:
        if op == '+':
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y if y != 0 else "❌ Division by zero"
        elif op == '%':
            return x % y
        elif op == '//':
            return x // y
        elif op == '**':
            return x ** y
        elif op == 'sqrt':
            return math.sqrt(x)
        elif op == 'abs':
            return abs(x)
        else:
            return "❌ Unsupported operation"
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

print("🧮 Advanced Python Calculator")
print("Available operations: +, -, *, /, %, //, **, sqrt, abs")

while True:
    op = input("Enter operation (e.g., +, sqrt, **): ").strip()

    if op in ['sqrt', 'abs']:
        try:
            x = float(input("Enter number: "))
            result = calculate(x, op)
        except ValueError:
            print("❌ Invalid number.")
            continue
    else:
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            result = calculate(x, op, y)
        except ValueError:
            print("❌ Invalid number.")
            continue

    print(f"✅ Result: {result}")

    again = input("Do you want to calculate again? (yes/no): ").lower()
    if again != 'yes':
        print("👋 Goodbye!")
        break
