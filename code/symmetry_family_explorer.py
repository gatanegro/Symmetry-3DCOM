import matplotlib.pyplot as plt

# --- Recursive Collatz Function ---


def recursive_orbit(n, depth=20):
    orbit = []
    for _ in range(depth):
        n = 3 * n + 1 if n % 2 else n // 2
        # Reduce mod 9; keep 9 instead of 0
        orbit.append(n % 9 if n % 9 != 0 else 9)
    return orbit

# --- Compare Two Orbits ---


def compare_orbits(n1, n2, depth=20):
    """
    Compare two recursive orbits mod 9 and return a similarity score.
    Score = fraction of matching mod-9 values at each recursive depth.
    """
    o1 = recursive_orbit(n1, depth)
    o2 = recursive_orbit(n2, depth)
    matches = sum(1 for a, b in zip(o1, o2) if a == b)
    return matches / depth

# --- Classify Symmetry Families ---


def classify_symmetry_families(N_range, depth=20, threshold=0.8):
    """
    Group numbers in N_range into symmetry families based on orbit similarity.
    Two numbers belong to the same family if their orbit similarity > threshold.
    """
    symmetry_families = []
    used = set()

    for n in N_range:
        if n in used:
            continue
        family = [n]
        used.add(n)
        for m in N_range:
            if m != n and m not in used:
                score = compare_orbits(n, m, depth)
                if score >= threshold:
                    family.append(m)
                    used.add(m)
        symmetry_families.append(family)

    return symmetry_families


# --- Example Usage ---
if __name__ == "__main__":
    N_range = range(1, 51)
    symmetry_groups = classify_symmetry_families(
        N_range, depth=20, threshold=0.75)

    # Print the groups
    for i, group in enumerate(symmetry_groups, 1):
        print(f"Group {i}: {group}")
