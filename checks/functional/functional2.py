assert absolute(5) == 5, f"absolute(5) should be 5, got {absolute(5)}"
assert absolute(-3) == 3, f"absolute(-3) should be 3, got {absolute(-3)}"
assert absolute(0) == 0, f"Expected absolute(0) to be 0, got {absolute(0)}"
assert absolute(-100) == 100, f"Expected absolute(-100) to be 100, got {absolute(-100)}"
print("functional2 ✓")
