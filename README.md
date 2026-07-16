# Sowon

A fullscreen digital stopwatch built with Python and Tkinter. It displays elapsed time using custom PNG digit images with a cycling animation effect, all rendered in a dark theme.

## Features

- **Fullscreen display** -- Time fills the entire screen with large digit images
- **Animated digits** -- Three image sets cycle per digit, each with different phase offsets, creating a dynamic visual effect
- **Responsive resizing** -- Frames, labels, and images all adapt when the window is resized
- **Dark theme** -- Uses ttkbootstrap's "darkly" theme with a black background
- **Stop shortcut** -- Press `s` to stop the timer

## Requirements

- Python >= 3.12
- [uv](https://docs.astral.sh/uv/) package manager (recommended)

## Installation

```bash
git clone <repo-url>
cd "timer project"
uv sync
```

## Usage

```bash
uv run src/main.py
```

Press `s` to stop the timer.

## Project Structure

```
src/
  main.py              # Entry point and counter loop
  root.py              # Window creation (ttkbootstrap)
  frames.py            # Frame layout (8 frames for digits/colons)
  labels.py            # Label widgets inside frames
  images.py            # Image loading and resizing with Pillow
  selecting_images.py  # Image selection and assignment to labels
  vars.py              # Global state and variables
  window_vars.py       # Screen dimension calculations
  resizing.py          # Dynamic resize handler
assests/
  first/               # Style 1 digit images (0-9 + colon)
  second/              # Style 2 digit images
  third/               # Style 3 digit images
```

## Dependencies

| Package | Purpose |
|---------|---------|
| [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap) | Themed Tkinter widgets and dark theme |
| [Pillow](https://python-pillow.org/) | Image loading, resizing, and conversion for Tkinter |
