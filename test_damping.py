# Test script to verify damping effect
import numpy as np

# Natural frequency
omega_n = 1.487  # rad/s

# Wave frequencies
omegas = np.array([0.3927, 0.5445, 0.6964, 0.8482, 1.0001, 1.1519])

# Damping parameters
M = 1.0e6  # kg
c = 30e3   # N·s/m

# Damping ratio
zeta = c / (2 * M * omega_n)
print(f"Damping ratio ζ = {zeta:.4f} = {zeta*100:.2f}%")
print(f"Natural frequency ω_n = {omega_n:.3f} rad/s")
print()

# Frequency ratios
print("Frequency ratios (ω/ω_n):")
for i, omega in enumerate(omegas):
    ratio = omega / omega_n
    print(f"  Component {i+1}: {ratio:.3f}")
print()

# Magnification factor with and without damping
print("Theoretical magnification factors:")
print("At resonance (ω/ωn ≈ 1):")
H_no_damp = 1 / (2 * 0.001)  # assume very small damping
H_with_damp = 1 / (2 * zeta)
print(f"  Without damping (ζ=0.1%): {H_no_damp:.1f}×")
print(f"  With damping (ζ={zeta*100:.2f}%): {H_with_damp:.1f}×")
print(f"  Reduction factor: {H_no_damp/H_with_damp:.1f}×")
