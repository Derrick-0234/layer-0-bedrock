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

        # allow name from either top-level name or flattened user_name
        name = str(flat.get("name") or flat.get("user_name") or "").strip()
        email = str(flat.get("email", "")).strip().lower()
        age = flat.get("age", "")

        # drop bad rows
        if not name or not email or "@" not in email:
            continue

        # IMPORTANT: keep output schema stable (tests expect only these keys)
        cleaned.append(
            {
                "name": name,
                "email": email,
                "age": age,
            }
        )

    return cleaned
