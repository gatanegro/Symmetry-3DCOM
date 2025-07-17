import sympy as sp

# --- Declare Symbols ---
n, theta, z = sp.symbols('n theta z', real=True)
delta_theta = sp.Symbol('delta_theta', real=True)

# --- Define Recursive Functions ---
alpha = sp.Symbol('alpha', positive=True)
L0 = sp.Symbol('L0', positive=True)

R_n = alpha**(-n) * L0
f_n = sp.log(1 + n)
gamma = sp.sin(n * theta) * 0.1
beta = sp.cos(n) * 0.05
lambda_n = sp.exp(-n / 5)

# --- Tensor Definition G_ab ---
G = sp.Matrix([
    [f_n,           0,      gamma],
    [0,         R_n**2,     beta],
    [gamma,       beta,  lambda_n]
])

# --- Observer Vector v^a (angle shift only) ---
v = sp.Matrix([0, delta_theta, 0])

# --- Field Tension S = G_ab * v^a * v^b ---
S = (v.T * G * v)[0]

S_simplified = sp.simplify(S)

# Output the field tension symbolic formula
S_simplified
