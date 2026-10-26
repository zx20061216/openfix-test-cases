def lookup(user_id, *, region):
    return {"id": user_id, "region": region}

def load_profile():
    return lookup(42)
