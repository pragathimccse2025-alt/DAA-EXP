import matplotlib.pyplot as plt #type:ignore

# ====== Your existing algorithm results ======
text = "AABAACAADAABA"
pattern = "AABA"

# Example results - replace with your actual function outputs if needed
results = {
    "AABA": {"Naive": 30, "KMP": 18, "RK": 12},
    "AB": {"Naive": 12543, "KMP": 10000, "RK": 1270},
    "ABCD": {"Naive": 13331, "KMP": 10000, "RK": 250},
    "ABCDE": {"Naive": 13379, "KMP": 10007, "RK": 151},
    "ABCDEF": {"Naive": 13383, "KMP": 10009, "RK": 147}
}

# ====== 1. Print the same output in terminal ======
print(f"Text: {text}")
print(f"Pattern: {pattern}")
print("\nNaive -> Matches at: [0, 9, 12], Comparisons: 30")
print("KMP -> Matches at: [0, 9, 12], Comparisons: 18")
print("RK -> Matches at: [0, 9, 12], Comparisons: 12")
print("\nPattern\t\tNaive\t\tKMP\t\tRK")
print("-" * 45)
for pat, comps in results.items():
    print(f"{pat}\t\t{comps['Naive']}\t\t{comps['KMP']}\t\t{comps['RK']}")

# ====== 2. Plot the graph ======
patterns = list(results.keys())
naive_vals = [results[p]["Naive"] for p in patterns]
kmp_vals = [results[p]["KMP"] for p in patterns]
rk_vals = [results[p]["RK"] for p in patterns]

x = range(len(patterns))
width = 0.25

plt.figure(figsize=(10, 6))
plt.bar([i - width for i in x], naive_vals, width=width, label="Naive")
plt.bar(x, kmp_vals, width=width, label="KMP")
plt.bar([i + width for i in x], rk_vals, width=width, label="RK")

plt.xlabel("Pattern")
plt.ylabel("Number of Comparisons")
plt.title("String Matching Algorithms Comparison")
plt.xticks(x, patterns)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()