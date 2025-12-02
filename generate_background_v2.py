"""
Generate a sophisticated background image for the hero section based on research themes:
- Wave propagation (acoustic waves)
- Computational fluid dynamics (flow patterns)
- Finite element meshes
- Mathematical optimization (gradient flows)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.tri import Triangulation

# Set high resolution for crisp output
fig = plt.figure(figsize=(19.2, 10.8), dpi=200)
ax = plt.gca()

# Create sophisticated multi-layer gradient background
x = np.linspace(0, 1, 200)
y = np.linspace(0, 1, 200)
X, Y = np.meshgrid(x, y)

# Define color palette - rich blues with depth
color_dark = np.array([25, 55, 180]) / 255  # Deep blue
color_mid = np.array([37, 99, 235]) / 255   # #2563eb
color_light = np.array([14, 165, 233]) / 255  # #0ea5e9

# Create layered gradient with radial influences
R = (color_dark[0] * (1 - Y) + color_light[0] * Y) * (1 - 0.2 * X)
G = (color_dark[1] * (1 - Y) + color_light[1] * Y) * (1 - 0.15 * X)
B = (color_dark[2] * (1 - Y) + color_light[2] * Y) * (1 - 0.1 * X)

# Add subtle radial gradients for depth
center_x, center_y = 0.3, 0.6
radial = np.sqrt((X - center_x)**2 + (Y - center_y)**2)
radial_factor = 1 - 0.15 * np.exp(-radial * 3)

background = np.dstack([R * radial_factor, G * radial_factor, B * radial_factor])
ax.imshow(background, extent=[0, 10, 0, 10], aspect='auto', alpha=1.0)

# Add elegant wave patterns with varying opacity and thickness
t = np.linspace(0, 10, 2000)
wave_configs = [
    (1.8, 0, 0.20, 2.5, 5.0),
    (2.4, np.pi/3, 0.18, 2.0, 4.5),
    (3.2, np.pi/2, 0.15, 1.8, 5.5),
    (2.0, np.pi, 0.12, 2.2, 6.0),
    (3.8, 3*np.pi/4, 0.10, 1.5, 4.0)
]

for freq, phase, alpha_val, lw, offset in wave_configs:
    y_wave = offset + 1.2 * np.sin(freq * t + phase) + 0.3 * np.sin(freq * 2 * t)
    ax.plot(t, y_wave, 'white', linewidth=lw, alpha=alpha_val, solid_capstyle='round')

# Create elegant finite element mesh - structured regions
np.random.seed(42)

# Create multiple mesh regions for visual interest
mesh_regions = [
    (np.array([0.5, 2.5, 0.5, 2.5]), 15),  # Bottom left
    (np.array([7, 9.5, 7, 9.5]), 12),       # Top right
    (np.array([3, 6, 2, 5]), 18),           # Center-left
]

for bounds, n_pts in mesh_regions:
    mesh_x = np.random.uniform(bounds[0], bounds[1], n_pts)
    mesh_y = np.random.uniform(bounds[2], bounds[3], n_pts)
    triang = Triangulation(mesh_x, mesh_y)
    ax.triplot(triang, color='white', linewidth=0.6, alpha=0.12, linestyle='-')

# Add gradient flow field - more sophisticated pattern
Y_grid, X_grid = np.mgrid[0.8:9.2:12j, 0.8:9.2:12j]

# Create vortex-like flow pattern (typical in CFD)
center_flow = np.array([5.0, 5.0])
dx = X_grid - center_flow[0]
dy = Y_grid - center_flow[1]
r = np.sqrt(dx**2 + dy**2) + 0.1

# Spiral flow pattern
U = -dy / r * np.exp(-r / 4)
V = dx / r * np.exp(-r / 4)

# Add gradient component
U += -0.15 * dx
V += -0.15 * dy

ax.quiver(X_grid, Y_grid, U, V,
          color='white', alpha=0.15, width=0.004,
          scale=12, headwidth=3.5, headlength=4.5)

# Add elegant mathematical annotations with better positioning
equations = [
    (r'$\nabla \cdot \mathbf{u} = 0$', (1.2, 8.8), 16),
    (r'$\nabla^2 p = -\omega^2 c^{-2} p$', (8.2, 1.5), 14),
    (r'$\min_{\mathbf{m}} \, J(\mathbf{m})$', (8.5, 8.5), 16),
    (r'$\mathbf{g} = \nabla_{\mathbf{m}} J$', (1.5, 1.8), 14),
]

for eq, (x_pos, y_pos), fsize in equations:
    text = ax.text(x_pos, y_pos, eq, fontsize=fsize, color='white',
                   alpha=0.18, family='serif', weight='normal',
                   bbox=dict(boxstyle='round,pad=0.4', facecolor='none',
                            edgecolor='none'))

# Add sophisticated geometric elements
# Large circles representing computational domains
circles = [
    (2.2, 7.2, 0.8, 0.10, 2.5),
    (7.8, 3.0, 0.7, 0.12, 2.2),
    (5.0, 5.2, 1.0, 0.08, 2.8),
]

for cx, cy, radius, alpha_val, lw in circles:
    circle = Circle((cx, cy), radius, fill=False,
                   edgecolor='white', linewidth=lw, alpha=alpha_val)
    ax.add_patch(circle)
    # Add inner circle for depth
    inner_circle = Circle((cx, cy), radius * 0.6, fill=False,
                         edgecolor='white', linewidth=lw * 0.6, alpha=alpha_val * 0.5)
    ax.add_patch(inner_circle)

# Add subtle grid overlay for structure
for i in np.linspace(0.5, 9.5, 15):
    ax.plot([i, i], [0, 10], 'white', linewidth=0.3, alpha=0.04)
    ax.plot([0, 10], [i, i], 'white', linewidth=0.3, alpha=0.04)

# Add decorative corner elements
corner_elements = [
    (0.3, 0.3, 0.5, 0.5),
    (9.7, 9.7, -0.5, -0.5),
]

for cx, cy, dx, dy in corner_elements:
    ax.plot([cx, cx + dx], [cy, cy], 'white', linewidth=3, alpha=0.2,
           solid_capstyle='round')
    ax.plot([cx, cx], [cy, cy + dy], 'white', linewidth=3, alpha=0.2,
           solid_capstyle='round')

# Add subtle particle effects
np.random.seed(123)
n_particles = 80
px = np.random.uniform(0, 10, n_particles)
py = np.random.uniform(0, 10, n_particles)
sizes = np.random.uniform(1, 4, n_particles)
alphas = np.random.uniform(0.05, 0.15, n_particles)

for i in range(n_particles):
    ax.plot(px[i], py[i], 'o', color='white', markersize=sizes[i],
           alpha=alphas[i])

# Clean up
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_aspect('equal')

# Save high-quality outputs
plt.tight_layout(pad=0)
plt.savefig('hero-background.png', dpi=200, bbox_inches='tight',
            pad_inches=0, facecolor='none', edgecolor='none',
            transparent=True)
plt.savefig('hero-background.jpg', dpi=200, bbox_inches='tight',
            pad_inches=0, facecolor='#1937b4', edgecolor='none')
plt.close()

print("✓ High-quality background images generated successfully!")
print("  - hero-background.png (transparent, 200 DPI)")
print("  - hero-background.jpg (solid background, 200 DPI)")
