def normalize_quota(value):
    return value or 8

def remaining_quota(value, used):
    quota = normalize_quota(value)
    return max(quota - used, 0)
