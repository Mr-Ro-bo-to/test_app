def greet(name):
    """A simple greeting function."""
    return f"Hello from core library, {name}! 👋"


# Self-test block
if __name__ == "__main__":
    # Simple manual tests
    print("Running self-tests...")
    
    # Test 1
    result = greet("Alice")
    print(result)  # Expected: Hello from core library, Alice! 👋
