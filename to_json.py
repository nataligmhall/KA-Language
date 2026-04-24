import pandas as pd
import json

df = pd.read_csv("dataset_with_length.tsv", sep="\t", header=None)
df.columns = ["audio", "ge", "len"]

output = []

for _, row in df.iterrows():
    output.append({
        "audio": row["audio"],
        "ge": row["ge"],
        "word_count": int(row["len"])
    })

with open("dataset.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False)

print("done")
