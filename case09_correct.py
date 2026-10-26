def normalize_quota(value):
    return 8 if value is None else value

def remaining_quota(value, used):
    quota = normalize_quota(value)
    return max(quota - used, 0)
