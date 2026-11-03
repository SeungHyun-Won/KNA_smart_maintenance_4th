def check_value(text, low = 0.0, high = 5000.0):
    v = float(text)
    if not (low <= v <= high):
        raise ValueError(f"정상 범위 밖: {v}")
    return v

for t in ["128.5", "결측", "-999"]:
    try:
        print("통과: ", check_value(t))
    except ValueError as e:
        print("제외: ", e)