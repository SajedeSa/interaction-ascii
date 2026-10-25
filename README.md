# Interactive Rainbow ASCII Art

An interactive generative art project built with **Python and Pygame**, featuring thousands of colorful ASCII particles that respond dynamically to mouse movement.

The project combines particle animation, vector mathematics, mouse interaction, and HSV color generation to create a responsive rainbow effect.

## Preview

Move your cursor across the screen to interact with the particles. Nearby particles move away from the mouse and gradually return to their original positions.

*Add a screenshot or GIF of your project here.*

## Features

- Rainbow-colored ASCII particle grid
- Real-time mouse repulsion
- Smooth return-to-home animation
- Independent movement for every particle
- HSV-based color generation
- Optimized text rendering
- Customizable particle density, interaction radius, and animation speed

## Technologies

- Python 3
- Pygame
- Math (Python standard library)
- Colorsys (Python standard library)

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

**2. Install Pygame**

```bash
pip install pygame
```

**3. Run the project**

```bash
python main.py
```

Replace `main.py` with your actual Python filename if it is different.

## How It Works

The application generates a grid of ASCII particles. Each particle stores its original position, current position, and pre-rendered colored character.

During every frame:

1. The program reads the current mouse position.
2. It calculates the distance between each particle and the cursor.
3. Particles within the interaction radius move away from the mouse.
4. Other particles gradually return to their original positions.
5. Pygame renders the updated particle positions.

Particle colors are generated using the HSV color model, creating a continuous rainbow gradient across the screen.

## Configuration

You can customize the animation by modifying these variables:

```python
spacing = 8
interaction_radius = 100
repulsion_speed = 4
return_speed = 2
```

| Parameter | Description |
|---|---|
| `spacing` | Distance between particles |
| `interaction_radius` | Mouse interaction range |
| `repulsion_speed` | Speed at which particles move away |
| `return_speed` | Speed at which particles return home |

Smaller spacing values create a denser particle grid but increase computational workload.

## Performance

Each particle's colored ASCII character is rendered only once during initialization and reused throughout the animation.

This avoids repeatedly calling `font.render()` during every frame and improves performance when working with thousands of particles.

## Future Improvements

- [ ] Circular and spiral particle arrangements
- [ ] Animated rainbow gradients
- [ ] Adjustable interaction settings
- [ ] Additional ASCII characters and patterns
- [ ] Screenshot and GIF export

## License

No license has been specified yet.

---

Made with Python, Pygame, and a little creativity.
