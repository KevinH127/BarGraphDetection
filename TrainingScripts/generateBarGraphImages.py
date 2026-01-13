"""
Random Bar Graph Generator for Object Detection Training
"""

import os
import random
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Configuration
# -----------------------------

OUTPUT_DIR = "TrainingImages/CleanEnvBarGraphs/Unlabelled"
NUM_IMAGES = 100
IMAGE_SIZE = (6, 4)
DPI = 150

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# Utility Functions
# -----------------------------

def random_color():
    return (random.random(), random.random(), random.random())


def colors_are_identical(color1, color2):
    return np.array_equal(color1, color2)


def ensure_background_is_unique(background_color, bar_colors):
    background = list(background_color)
    for bar_color in bar_colors:
        if colors_are_identical(background, bar_color):
            background[-1] = min(background[-1] + 1e-3, 1.0)
    return tuple(background)


def generate_bar_values(num_bars):
    return np.random.randint(5, 100, size=num_bars)


def generate_bar_positions(num_bars, bar_width):
    """
    Generates bar positions that NEVER overlap.
    Spacing ranges from touching / ~1px gap to normal spacing.
    """

    # Choose spacing mode
    if random.random() < 0.5:
        # Very tight spacing (touching to tiny gap)
        gap = random.uniform(0.0, 0.05 * bar_width)
    else:
        # Normal spacing
        gap = random.uniform(0.2 * bar_width, 0.6 * bar_width)

    step = bar_width + gap

    positions = [0.0]
    for _ in range(1, num_bars):
        positions.append(positions[-1] + step)

    return np.array(positions)


# -----------------------------
# Main Image Generation Loop
# -----------------------------

for image_index in range(NUM_IMAGES):

    number_of_bars = random.randint(3, 10)
    bar_heights = generate_bar_values(number_of_bars)

    bar_width = random.uniform(0.4, 0.8)
    bar_positions = generate_bar_positions(number_of_bars, bar_width)

    fig, ax = plt.subplots(figsize=IMAGE_SIZE, dpi=DPI)

    multicolor_bars = random.random() < 0.4
    collected_bar_colors = []

    if multicolor_bars:
        for bar_index in range(number_of_bars):
            remaining_height = bar_heights[bar_index]
            bottom = 0
            number_of_segments = random.randint(2, 4)

            for _ in range(number_of_segments):
                segment_height = random.uniform(0.2, 0.5) * remaining_height
                segment_color = random_color()
                collected_bar_colors.append(segment_color)

                ax.bar(
                    bar_positions[bar_index],
                    segment_height,
                    bottom=bottom,
                    width=bar_width,
                    color=segment_color
                )
                bottom += segment_height
    else:
        bar_colors = [random_color() for _ in range(number_of_bars)]
        collected_bar_colors.extend(bar_colors)

        ax.bar(
            bar_positions,
            bar_heights,
            width=bar_width,
            color=bar_colors
        )

    # Background color
    background_color = random_color()
    background_color = ensure_background_is_unique(
        background_color,
        collected_bar_colors
    )

    fig.patch.set_facecolor(background_color)
    ax.set_facecolor(background_color)

    # Axis handling
    if random.random() < 0.5:
        ax.axis("off")
    else:
        ax.tick_params(axis='both', which='both', length=0)
        ax.set_xticks([])
        ax.set_yticks([])

    plt.margins(0.05)

    output_path = os.path.join(OUTPUT_DIR, f"bar_graph_{image_index:04d}.png")
    plt.savefig(output_path, bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)

print(f"Generated {NUM_IMAGES} bar graph images in '{OUTPUT_DIR}'")
