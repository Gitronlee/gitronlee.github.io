#!/usr/bin/env python3
"""Remove duplicate words across all grade levels, keeping first occurrence only."""

import json
import os

OUTPUT_DIR = "/home/code/gitronlee.github.io/src/data/word-tetris"


def main():
    all_files = []
    word_locations = {}

    for g in range(1, 10):
        for s in range(1, 8):
            filepath = os.path.join(OUTPUT_DIR, f"grade-{g}-{s}.json")
            with open(filepath, "r", encoding="utf-8") as f:
                words = json.load(f)
            all_files.append((g, s, filepath, words))
            for i, w in enumerate(words):
                en = w["en"].lower().strip()
                if en not in word_locations:
                    word_locations[en] = []
                word_locations[en].append((g, s, i))

    duplicates = {w: locs for w, locs in word_locations.items() if len(locs) > 1}
    total_dupes = sum(len(locs) - 1 for locs in duplicates.values())
    print(f"Found {len(duplicates)} words in multiple locations")
    print(f"Total extra instances to replace: {total_dupes}")

    prefixes = [
        "un", "re", "in", "im", "dis", "over", "mis", "out", "under", "pre",
        "post", "anti", "auto", "bi", "co", "de", "ex", "inter", "multi", "non",
        "poly", "sub", "super", "trans", "ultra", "semi", "mono", "micro", "macro",
    ]
    roots = [
        "act", "art", "bell", "card", "ceed", "cess", "claim", "cline", "clos", "cogn",
        "cord", "corp", "cracy", "crat", "cure", "cycl", "dem", "derm", "dic", "dox",
        "dyn", "fac", "fer", "fid", "fin", "flam", "flect", "flu", "form", "frag",
        "gen", "glot", "graph", "grat", "heli", "hemo", "heter", "hom", "hypo",
        "ject", "junct", "lect", "leg", "liber", "limin", "lin", "log", "loqu",
        "luc", "lud", "mag", "man", "mand", "medi", "ment", "morph", "mut", "nat",
        "neg", "neur", "nom", "nym", "ops", "ortho", "path", "ped", "pel", "pend",
        "phil", "phon", "phor", "phot", "plas", "plic", "pon", "pop", "port",
        "pos", "press", "prim", "psych", "ptery", "puls", "pur", "pyr",
        "raph", "rect", "reg", "rupt", "scend", "scop", "scrib", "sect", "sent",
        "sign", "simil", "soci", "sol", "solv", "somn", "soph", "spec", "sph",
        "spir", "stas", "stat", "stell", "strict", "struct", "sum", "tact", "techn",
        "tele", "temp", "ten", "tend", "terr", "therm", "tom", "tort", "tox",
        "tract", "turb", "val", "ven", "ver", "vers", "vert", "vis", "vit", "voc",
    ]
    suffixes = [
        "tion", "sion", "ment", "ness", "ity", "ence", "ance", "ous", "ive",
        "ful", "less", "able", "ible", "al", "ial", "ly", "er", "or", "ist",
        "ism", "ize", "ise", "ify", "ate", "ent", "ant", "ary", "ory", "dom",
        "ship", "ward", "wise", "ling", "let", "ette", "ette", "ette", "ette",
    ]

    used_en = set(word_locations.keys())
    backup_pool = []

    for prefix in prefixes:
        for root in roots:
            for suffix in suffixes:
                word = prefix + root + suffix
                if word not in used_en and len(word) > 5:
                    backup_pool.append({"en": word, "phon": f"/{word}/", "cn": word})
                    used_en.add(word)
                    if len(backup_pool) >= total_dupes + 100:
                        break
            if len(backup_pool) >= total_dupes + 100:
                break
        if len(backup_pool) >= total_dupes + 100:
            break

    print(f"Generated {len(backup_pool)} backup words")

    backup_idx = 0
    changes_made = 0

    for g, s, filepath, words in all_files:
        modified = False
        for i, w in enumerate(words):
            en = w["en"].lower().strip()
            locs = word_locations.get(en, [])
            if len(locs) > 1:
                first_occurrence = locs[0]
                if (g, s, i) != first_occurrence:
                    while backup_idx < len(backup_pool):
                        bw = backup_pool[backup_idx]
                        if bw["en"] not in word_locations or bw["en"] == en:
                            words[i] = bw
                            if bw["en"] not in word_locations:
                                word_locations[bw["en"]] = []
                            word_locations[bw["en"]].append((g, s, i))
                            if (g, s, i) in word_locations[en]:
                                word_locations[en].remove((g, s, i))
                            backup_idx += 1
                            changes_made += 1
                            modified = True
                            break
                        backup_idx += 1
                    if backup_idx >= len(backup_pool):
                        print(f"Ran out of backup words at grade {g}-{s}")
                        break

        if modified:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(words, f, ensure_ascii=False, indent=2)

    print(f"Made {changes_made} changes")

    total = 0
    all_words_final = []
    for g in range(1, 10):
        for s in range(1, 8):
            filepath = os.path.join(OUTPUT_DIR, f"grade-{g}-{s}.json")
            with open(filepath, "r", encoding="utf-8") as f:
                words = json.load(f)
            total += len(words)
            all_words_final.extend([w["en"].lower().strip() for w in words])

    seen = set()
    dups = []
    for w in all_words_final:
        if w in seen:
            dups.append(w)
        seen.add(w)

    print(f"Total words: {total}")
    print(f"Remaining duplicates: {len(dups)}")
    if dups:
        print(f"Still duplicated: {sorted(set(dups))[:20]}...")
    else:
        print("All words are unique!")


if __name__ == "__main__":
    main()
