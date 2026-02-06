def dedupe_by_email(rows):
    """
    Rules:
    - email key = "email"
    - normalize email: strip spaces + lowercase
    - drop rows with missing email
    - keep the first time each email appears
    """
    seen = set()
    out = []

    for row in rows:
        email = (row.get("email") or "").strip().lower()

        if not email:
            continue

        if email in seen:
            continue

        seen.add(email)

        # keep row, but normalize email in the output
        new_row = dict(row)
        new_row["email"] = email
        out.append(new_row)

    return out
