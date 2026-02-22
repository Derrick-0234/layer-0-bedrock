def clean_json_rows(rows):
    cleaned = []

    for row in rows:
        # 1-level flatten: {"user":{"name":"Ann"}} -> {"user_name":"Ann"}
        flat = {}
        for k, v in row.items():
            if isinstance(v, dict):
                for kk, vv in v.items():
                    flat[f"{k}_{kk}"] = vv
            else:
                flat[k] = v

        name = str(flat.get("name") or flat.get("user_name") or "").strip()
        email = str(flat.get("email", "")).strip().lower()
        age = flat.get("age", "")

        # drop bad rows
        if not name or not email or "@" not in email:
            continue

        cleaned.append(
            {
                "name": name,
                "user_name": str(flat.get("user_name", "")).strip(),
                "email": email,
                "age": age,
            }
        )

    return cleaned
