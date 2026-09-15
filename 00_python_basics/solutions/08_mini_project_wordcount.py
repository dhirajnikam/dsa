def word_report(text, top=3):
    tokens = [t.strip(".,!?;:'\"") for t in text.lower().split()]
    tokens = [t for t in tokens if t]
    counts = {}
    longest = ""
    for t in tokens:
        counts[t] = counts.get(t, 0) + 1
        if len(t) > len(longest):
            longest = t
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:top]
    return {"words": len(tokens), "unique": len(counts), "top": ranked, "longest": longest}
