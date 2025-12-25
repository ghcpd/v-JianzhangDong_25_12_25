def plot_histogram(data, title="Histogram"):
    """Print a simple text histogram."""
    print(f"{title}")
    print("Simple histogram representation:")
    for value in data:
        print("*" * int(value * 10))  # Simple bar
    return None
