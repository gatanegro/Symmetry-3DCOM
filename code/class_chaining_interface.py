import numpy as np
from sympy import symbols, Function, simplify


class RecursiveAlgebra:
    def __init__(self, initial_n, depth=20, theta=0):
        """
        Initialize with:
        - initial_n: Starting integer (e.g., Collatz seed).
        - depth: Recursion depth for orbit generation.
        - theta: Observer phase angle (radians).
        """
        self.n = initial_n
        self.depth = depth
        self.theta = theta
        self.orbit = self._generate_orbit()

    def _generate_orbit(self):
        """Generate Collatz orbit mod 9."""
        orbit = []
        n = self.n
        for _ in range(self.depth):
            n = 3 * n + 1 if n % 2 else n // 2
            orbit.append(n % 9 if n % 9 != 0 else 9)  # Mod 9, 0 → 9
        return orbit

    def R(self, theta):
        """Rotate orbit by phase theta (mod 9)."""
        rotated = [(x + int(theta * 9 / (2*np.pi)) - 1) %
                   9 + 1 for x in self.orbit]
        self.orbit = rotated
        self.theta += theta
        return self  # Enable chaining

    def M(self):
        """Mirror orbit (qualia collapse)."""
        self.orbit = [10 - x if x != 9 else 1 for x in self.orbit]
        return self

    def T(self, k):
        """Translate initial n by k and regenerate orbit."""
        self.n += k
        self.orbit = self._generate_orbit()
        return self

    def S(self, lam):
        """Scale recursion depth by lambda."""
        self.depth = max(1, int(self.depth * lam))
        self.orbit = self.orbit[:self.depth]
        return self

    def __repr__(self):
        return f"RecursiveAlgebra(n={self.n}, depth={self.depth}, θ={self.theta:.2f}): {self.orbit}"


# Example Usage:
ra = RecursiveAlgebra(13).R(np.pi/2).M().S(0.5)
print(ra)
