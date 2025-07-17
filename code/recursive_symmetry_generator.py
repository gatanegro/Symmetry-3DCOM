def symmetry_orbit(n, depth=5):
    orbit = [n]
    for i in range(depth):
        n = collatz(n)
        n_mod = n % 9
        orbit.append(n_mod)
    return orbit
