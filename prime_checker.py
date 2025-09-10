print("🔢 Prime Number Checker")

# Function to check prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Keep running until user quits
while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input.lower() == 'q':
        print("👋 Exiting program. Bye!")
        break

    try:
        number = int(user_input)
        if is_prime(number):
            print(f"✅ {number} is a PRIME number.")
        else:
            print(f"❌ {number} is NOT a prime number.")

        # NEW FEATURE: list primes up to number
        primes = [str(i) for i in range(2, number + 1) if is_prime(i)]
        print(f"👉 Prime numbers up to {number}: {', '.join(primes)}\n")

    except ValueError:
        print("⚠️ Please enter a valid number.\n")
