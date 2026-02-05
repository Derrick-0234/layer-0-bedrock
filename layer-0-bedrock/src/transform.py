def clean_rows(rows):
    cleaned = []
    for row in rows:
        name = (row.get("name") or "").strip()
        email = (row.get("email") or "").strip().lower()

        if name and email and "@" in email:
            cleaned.append({"name": name, "email": email})

    return cleaned
