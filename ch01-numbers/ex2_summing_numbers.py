import math


def mysum(*args):
    total = 0
    for arg in args:
        total += arg
    return total


def zeta_regularized_sum():
    """
    Compute the 'sum' 1 + 2 + 3 + 4 + ... using Riemann zeta regularization.

    This returns ζ(-1) = -1/12 via the functional equation.
    This is NOT a conventional sum — regular summation diverges to infinity.
    """
    # ζ(2) = π²/6 (Basel problem, proven by Euler)
    zeta_2 = (math.pi ** 2) / 6

    # Functional equation at s = -1:
    # ζ(-1) = 2^(-1) × π^(-2) × sin(-π/2) × Γ(2) × ζ(2)
    s = -1
    result = (2 ** s) * (math.pi ** (s - 1)) * math.sin(math.pi * s / 2) * math.gamma(2) * zeta_2

    return result  # ≈ -0.08333... = -1/12


def zeta_positive(s, terms=100000):
    """
    Compute ζ(s) for s > 1 by summing the series.

    ζ(s) = 1 + 1/2^s + 1/3^s + 1/4^s + ...

    Converges for s > 1.
    """
    if s <= 1:
        raise ValueError("Series only converges for s > 1")
    # Use float exponentiation to avoid integer overflow for large s
    # For large s, the series converges very fast (k^(-s) vanishes quickly)
    return sum(float(k) ** (-s) for k in range(1, terms + 1))


def zeta_negative_integer(n):
    """
    Compute ζ(-n) for positive integer n using the functional equation.

    This gives the 'regularized sum' of:
      n=1: 1 + 2 + 3 + 4 + ...           = -1/12
      n=2: 1 + 4 + 9 + 16 + ...          = 0 (trivial zero)
      n=3: 1 + 8 + 27 + 64 + ...         = 1/120
      n=4: 1 + 16 + 81 + 256 + ...       = 0 (trivial zero)
      ...

    Functional equation: ζ(s) = 2^s × π^(s-1) × sin(πs/2) × Γ(1-s) × ζ(1-s)

    Uses log-space computation to avoid overflow for large n.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    s = -n
    one_minus_s = 1 - s  # = 1 + n

    # sin(πs/2) = sin(-nπ/2)
    # For even n: sin(-nπ/2) = 0 → trivial zeros
    sin_term = math.sin(math.pi * s / 2)
    if abs(sin_term) < 1e-10:
        return 0.0

    # Compute ζ(1-s) = ζ(1+n) using the convergent series
    # For large s, very few terms needed since k^(-s) vanishes quickly
    zeta_1_minus_s = zeta_positive(one_minus_s, terms=1000)

    # Work in log space to avoid overflow:
    # log|result| = s*log(2) + (s-1)*log(π) + log|sin(πs/2)| + lgamma(1-s) + log(ζ(1-s))
    log_abs_result = (
        s * math.log(2) +
        (s - 1) * math.log(math.pi) +
        math.log(abs(sin_term)) +
        math.lgamma(1 - s) +
        math.log(zeta_1_minus_s)
    )

    # Determine the sign
    sign = 1 if sin_term > 0 else -1

    return sign * math.exp(log_abs_result)


def plot_zeta_negative_integers(max_n=20):
    """
    Plot ζ(-n) for n = 1, 2, 3, ..., max_n.

    Shows the fascinating pattern:
    - Negative even integers give 0 (trivial zeros)
    - Negative odd integers give non-zero values related to Bernoulli numbers
    """
    import matplotlib.pyplot as plt
    import numpy as np

    n_values = list(range(1, max_n + 1))
    zeta_values = [zeta_negative_integer(n) for n in n_values]

    # Get only odd values (non-trivial)
    odd_n = [n for n in n_values if n % 2 == 1]
    odd_zeta = [zeta_negative_integer(n) for n in odd_n]

    # Create the plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9))

    # Top plot: log scale of absolute values, colored by sign
    abs_odd_zeta = [abs(z) for z in odd_zeta]
    colors = ['red' if z < 0 else 'blue' for z in odd_zeta]

    ax1.scatter([-n for n in odd_n], abs_odd_zeta, c=colors, s=50, alpha=0.7)
    ax1.set_yscale('log')
    ax1.set_xlabel('s (negative odd integers)')
    ax1.set_ylabel('|ζ(s)|  (log scale)')
    ax1.set_title('Riemann Zeta at Negative Odd Integers\n(Blue = positive, Red = negative)')
    ax1.grid(True, alpha=0.3)

    # Add reference line showing factorial-like growth
    if max_n > 20:
        x_ref = np.array([-n for n in odd_n])
        # Rough approximation of growth rate
        ax1.plot(x_ref, [10 ** (0.4 * abs(x)) for x in x_ref],
                 'g--', alpha=0.5, label='~10^(0.4|s|) reference')
        ax1.legend()

    # Bottom plot: actual values for small n (where visible)
    small_odd_n = [n for n in odd_n if n <= 25]
    small_odd_zeta = [zeta_negative_integer(n) for n in small_odd_n]

    ax2.bar([-n for n in small_odd_n], small_odd_zeta,
            color=['red' if z < 0 else 'blue' for z in small_odd_zeta], alpha=0.7)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax2.set_xlabel('s (negative odd integers, s ≥ -25)')
    ax2.set_ylabel('ζ(s)')
    ax2.set_title('Actual values for small |s| (alternating signs visible)')
    ax2.grid(True, alpha=0.3)

    # Annotate key values
    for n, z in zip(small_odd_n[:7], small_odd_zeta[:7]):
        label = f'{z:.4f}' if abs(z) < 1 else f'{z:.1f}'
        ax2.annotate(label, (-n, z), textcoords="offset points",
                     xytext=(0, 5 if z > 0 else -12), ha='center', fontsize=7)

    plt.tight_layout()
    plt.savefig('zeta_negative_integers.png', dpi=150)
    plt.show()

    return list(zip([-n for n in n_values], zeta_values))


if __name__ == '__main__':
    print("Zeta function at negative integers:")
    print("-" * 65)
    for n in range(1, 21):
        z = zeta_negative_integer(n)
        series = " + ".join([f"{k}^{n}" for k in range(1, 4)]) + " + ..."
        print(f"ζ({-n:3d}) = {z:>20.10e}  ({series})")
    print("-" * 65)
    print("\nGenerating plot...")
    plot_zeta_negative_integers(110)
