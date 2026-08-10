def format_likes(count):
    if count >= 1_000_000:
        formatted = f"{count / 1_000_000:.1f}".rstrip('0').rstrip('.')
        return f"{formatted}M"
    elif count >= 1_000:
        formatted = f"{count / 1_000:.1f}".rstrip('0').rstrip('.')
        return f"{formatted}K"
    return str(count)