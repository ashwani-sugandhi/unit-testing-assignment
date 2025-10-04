def normalize(s: str) -> str:
    """Strip whitespace, lower case, and compress spaces."""
    return " ".join(s.strip().lower().split())
