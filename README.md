# Quadratic Formula Slides

A Manim Slides presentation about solving quadratic equations with the quadratic formula.

## Render the deck

```bash
uv sync
uv run manim-slides render --quality h quadratic_formula_slides.py QuadraticFormulaDeck
uv run manim-slides convert QuadraticFormulaDeck quadratic_formula_deck.html
```

The HTML export uses Reveal.js and scales to the browser window automatically. The render command uses Manim's `h` quality preset, which produces 1920×1080 source assets for crisp projection. If you know the target display is higher resolution, Manim also supports `--quality p` for 2560×1440 and `--quality k` for 3840×2160.

The deck covers:
- what it means to solve a quadratic
- how solutions appear as x-intercepts on a graph
- what `a`, `b`, and `c` do to the parabola
- how the discriminant predicts the number of real roots
- an animated derivation of the quadratic formula by completing the square
- worked examples, a repeatable solving routine, and practice questions
