def format_username(username, prefix='user_'):
    return f"{prefix}{username}"

print("Default Prefix:", format_username("purva"))

print("Custom Prefix:", format_username("purva", prefix="admin_"))