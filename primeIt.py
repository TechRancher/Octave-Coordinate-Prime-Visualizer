import matplotlib.pyplot as plt
import math

def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def octave_normalize(n):
    """Normalizes a number to the range [1, 2)."""
    while n >= 2:
        n /= 2
    return n

def visualize_primes(num_primes=100, color_mode="neutral"):
    """Visualizes prime numbers in an octave range."""
    primes = [i for i in range(2, 1000) if is_prime(i)][:num_primes]
    octave_coords = [octave_normalize(p) for p in primes]

    plt.figure(figsize=(10, 6))
    ax = plt.gca()
    ax.set_xlim(1, 2)
    ax.set_ylim(0, 1)  # Adjust y-limit as needed
    ax.set_yticks([])  # Hide y-axis ticks
    ax.set_xlabel("Octave Range (1 to 2)")
    ax.set_title(f"Octave Coordinate Visualization of the First {num_primes} Prime Numbers")

    for i, coord in enumerate(octave_coords):
        if color_mode == "neutral":
            color = 'blue'
        elif color_mode == "gradient":
            # Normalize prime magnitude to a color range (e.g., 0 to 1)
            normalized_magnitude = math.log(primes[i]) / math.log(primes[-1]) if primes[-1] > 1 else 0.5
            color = plt.cm.viridis(normalized_magnitude) # Use a colormap

        # Plot a vertical line at the octave coordinate
        ax.plot([coord, coord], [0.1, 0.9], color=color, linewidth=1)

    plt.grid(axis='x', linestyle='--')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    num_primes_to_display = 50  # You can change this number
    color_option = "gradient"  # Try "neutral" as well
    visualize_primes(num_primes=num_primes_to_display, color_mode=color_option)
