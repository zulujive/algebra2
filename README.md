# Manim Algebra 2

![Manim Algebra 2 Logo](https://github.com/zulujive/algebra2/blob/master/Manim_Algebra_2_Logo_black-to-gray.png?raw=true)

![Static Badge](https://img.shields.io/badge/Currently%20Maintained-brightgreen) ![Static Badge](https://img.shields.io/badge/In%20Development-yellow) ![GitHub Repo stars](https://img.shields.io/github/stars/zulujive/algebra2?style=flat) ![GitHub watchers](https://img.shields.io/github/watchers/zulujive/algebra2?style=flat) ![GitHub License](https://img.shields.io/github/license/zulujive/algebra2)

This project is the start of a full **Algebra 2 curriculum** built with **Manim** and **Manim Slides**. Each lesson presentation is intended to live in its own Python file and can be rendered/exported independently.

The repository currently includes a quadratic formula lesson:

- source file: `quadratic_formula_slides.py`
- scene class: `QuadraticFormulaDeck`
- pre-rendered slideshow: `quadratic_formula_deck.html`

## Project Purpose and Motivations
Current solutions for teaching math through slideshow lectures do *not* effectively teach students the mechanics and intuition needed to be successful in their subject. This project addresses that by providing a number of mini-lesson slideshows that teach through visual intuition and beautiful animations using the Manim engine inspired by the work of Grant Sanderson at [3Blue1Brown](https://www.3blue1brown.com/). We believe that the best type of learning happens when students can see manipulations to variables in realtime and how that works, exactly. We're also working with educators to improve and add to the project in order to give teachers what they need. We hope this is just the beginning of this effort and that new classes are added to achieve our mission in creating the best math lesson toolkit available.

## Pre-rendered slideshows

Lessons have already been rendered and exported to HTML and can be opened directly in a browser without rendering first. This is the easiest way to present slideshows.

Current pre-rendered slideshow files:

- `quadratic_formula_deck.html`

These HTML exports use Reveal.js and automatically scale to the browser window. We __**highly**__ recommend that you use the pre-rendered files instead of rendering them yourself. This project is not designed for a streamlined rendering process and attempting it on your machine may be difficult.

To use the HTML presentations, download the repo or clone it with:
```bash
git clone https://github.com/zulujive/algebra2.git
```

Then open the HTML slideshow of your choice. Work is being done to have a plug-and-play single-HTML download that references the animation files on GitHub.

### IMPORTANT

Currently, it is *not* possible to simply download a standalone HTML file because the animations are sourced from the host machine. You **must** download the *full* repo for the presentations to work.

## Install dependencies

```bash
uv sync
```

## Render and export a slide deck

Each slide deck has two important names:

1. the Python source file
2. the Manim Slides scene class inside that file

General pattern:

```bash
uv run manim-slides render --quality h <deck_file.py> <SceneClass>
uv run manim-slides convert <SceneClass> <output_file.html>
```

For the current quadratic formula deck:

```bash
uv run manim-slides render --quality h quadratic_formula_slides.py QuadraticFormulaDeck
uv run manim-slides convert QuadraticFormulaDeck quadratic_formula_deck.html
```

### Render quality

Use `--quality h` for final classroom-ready output. It produces **1920×1080 at 60 fps**, which is the recommended baseline for crisp projection.

Useful Manim quality presets:

- `--quality l` → fast draft render, 854×480 at 15 fps
- `--quality h` → recommended final render, 1920×1080 at 60 fps
- `--quality p` → 2560×1440 at 60 fps
- `--quality k` → 3840×2160 at 60 fps

Use low quality while iterating, then re-render at high quality before exporting the final HTML slideshow.

## Presentation controls for HTML slideshows

When presenting a pre-rendered HTML slideshow in the browser:

| Key | Action |
| --- | --- |
| `←` / `→` | Move backward or forward through the slides |
| `f` | Enter fullscreen |
| `Esc` | Exit fullscreen (if in fullscreen)|
| `v` | Hide the slideshow / reveal it again |
| `Esc` | Open the slideshow index when not in fullscreen |
| `o` | Open the slideshow index while in fullscreen |

Notes:

- The arrow keys are the main navigation controls during teaching.
- `v` is useful when you want to temporarily blank the projected content while discussing something off-slide.
- The slideshow index gives an overview of the presentation and lets you jump to a different slide section quickly.

## Current deck contents

The quadratic formula lesson covers:

- what it means to solve a quadratic
- how solutions appear as x-intercepts on a graph
- what `a`, `b`, and `c` do to a parabola
- how the discriminant predicts the number of real roots
- teacher-controlled pauses for discussing discriminant cases
- an animated derivation of the quadratic formula by completing the square
- worked examples, a repeatable solving routine, and practice questions

## Notes for contributors and AI agents

For detailed project conventions, lesson-design philosophy, workflows, quality expectations, and future expansion guidance, see:

```text
CONTEXT.md
```
