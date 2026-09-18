assert apply_twice(triple, 2) == 18, (
    f"apply_twice(triple, 2) should be 18, got {apply_twice(triple, 2)}"
)
assert apply_twice(add_ten, 5) == 25, (
    f"apply_twice(add_ten, 5) should be 25, got {apply_twice(add_ten, 5)}"
)
assert apply_twice(lambda x: x + 1, 0) == 2, (
    f"apply_twice(lambda x: x + 1, 0) should be 2, "
    f"got {apply_twice(lambda x: x + 1, 0)}"
)
print("functional6 ✓")