def clean_json_rows(rows):
    cleaned = []

    for row in rows:
        name = str(row.get("name", "")).strip()
        email = str(row.get("email", "")).strip().lower()
        age = row.get("age", "")

        # drop bad rows
        if not name or not email or "@" not in email:
            continue

        cleaned.append({"name": name, "email": email, "age": age})

    return cleaned
