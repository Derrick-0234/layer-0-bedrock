def left_join_by_email(left_rows, right_rows):
    """
    Left join on email.
    Rules:
    - normalize email: strip + lowercase before matching
    - keep all left rows
    - add right-side fields if match exists, else blank
    """
    # Build lookup from right_rows by normalized email
    right_map = {}
    right_fields = set()

    for r in right_rows:
        email = (r.get("email") or "").strip().lower()
        if not email:
            continue
        right_map[email] = r
        right_fields.update(r.keys())

    right_fields.discard("email")

    out = []
    for l in left_rows:
        email = (l.get("email") or "").strip().lower()
        merged = dict(l)
        merged["email"] = email

        r = right_map.get(email)
        if r:
            for k in right_fields:
                merged[k] = r.get(k, "")
        else:
            for k in right_fields:
                merged[k] = ""

        out.append(merged)

    return out, list(right_fields)
