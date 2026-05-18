# CONTEXT.md

## Purpose of this repository

This repository is the beginning of a **full Algebra 2 curriculum** built with **Manim Community Edition** and **Manim Slides**.

The long-term intent is not to keep one giant presentation file. Instead:

- each lesson / presentation should live in its **own Python source file**
- each presentation should define its own **Manim Slides scene class**
- each lesson should be renderable independently and exportable to HTML independently
- the repository should eventually contain a coherent sequence of Algebra 2 lessons with consistent visual language, reusable patterns, and teacher-friendly pacing

The first completed lesson is a deck on solving quadratics with the quadratic formula:

- source file: `quadratic_formula_slides.py`
- scene class: `QuadraticFormulaDeck`
- HTML export: `quadratic_formula_deck.html`

The project should be treated as a curriculum-authoring codebase, not just a Manim sandbox.

---

## Current technology stack

### Core tools

- **Python**: project currently targets Python `>=3.14`
- **Dependency manager / runner**: `uv`
- **Animation engine**: `manim>=0.20.1`
- **Slide system**: `manim-slides>=5.5.0`
- **HTML presentation output**: Manim Slides `convert` command using Reveal.js under the hood

### Project metadata

`pyproject.toml` currently defines:

```toml
[project]
name = "manimations"
version = "0.1.0"
requires-python = ">=3.14"
dependencies = [
    "manim>=0.20.1",
    "manim-slides>=5.5.0",
]
```

The repository is currently small and early-stage. Expect its structure to become more organized as more lessons are added.

---

## Important project philosophy

### 1. This is for teaching, not just visual spectacle

Animations should clarify mathematical structure. Prefer visuals that make the underlying idea easier to understand:

- terms moving across an equation when students need to see why signs change
- graphs showing roots as x-intercepts when solving is being discussed
- controlled pauses where the teacher can ask students to predict an outcome
- multiple examples and practice prompts, not just polished exposition

Avoid animation for its own sake if it makes the lesson harder to follow.

### 2. Presenter control matters

Lessons are meant to be taught live. Use `self.next_slide()` intentionally to create teacher-controlled beats.

Good uses of slide stops include:

- pausing before revealing an answer
- stopping at each graph state so the teacher can ask a question
- splitting a derivation into meaningful algebraic moves
- giving students time to think before the next animation

### 3. Crisp output matters

The final delivery format is usually **HTML**, but HTML export only scales the underlying media. If the source render is low-resolution, the HTML presentation will still look blurry on a projector.

For final classroom-ready exports, render with at least:

```bash
uv run manim-slides render --quality h <file.py> <SceneClass>
```

`--quality h` produces **1920×1080 at 60 fps**. This is the current recommended default for projection.

Higher-quality options exist when needed:

- `--quality p` → 2560×1440
- `--quality k` → 3840×2160

Use higher settings only when the display context justifies the additional render time and asset size.

---

## Current repository structure

### Hand-authored source files

- `quadratic_formula_slides.py`  
  The first full presentation deck. Contains the lesson-specific scene class and currently includes its own style helpers.

- `README.md`  
  Short user-facing instructions for rendering/exporting the current deck.

- `pyproject.toml`  
  Project metadata and dependencies.

- `main.py`  
  Currently just starter boilerplate from project initialization. It is not part of the presentation workflow at this time.

- `CONTEXT.md`  
  This document. Intended for future AI agents and collaborators.

### Generated output and cache directories/files

These are produced by Manim / Manim Slides and should generally **not** be treated as source of truth:

- `media/`
- `slides/`
- `quadratic_formula_deck.html`
- `quadratic_formula_deck_assets/`
- `slides.html`
- `slides_assets/`
- `__pycache__/`

The authored Python files are the source of truth. Generated files may be regenerated after changes.

### Current generated artifacts of note

The current quadratic deck has been rendered and exported. At the time of writing:

- active final slide assets are 1920×1080, 60 fps
- `QuadraticFormulaDeck` currently contains 23 presenter-controlled slide states
- the HTML output is responsive in browser windows via Reveal.js

---

## Expected lesson-file pattern going forward

Each presentation should usually have:

1. **one lesson-specific Python file**
2. **one primary `Slide` subclass**
3. lesson-specific constants/helpers near the top, unless/until common helpers are factored out
4. a clearly sequenced `construct()` method organized by educational sections
5. a corresponding HTML export when needed

Recommended naming pattern:

```text
<topic>_slides.py
```

Examples:

```text
quadratic_formula_slides.py
polynomial_functions_slides.py
exponential_models_slides.py
logarithms_slides.py
```

Recommended scene naming pattern:

```python
class QuadraticFormulaDeck(Slide):
    ...
```

Use clear, lesson-specific scene names rather than generic names like `Scene1` or `Lesson`.

---

## Current visual style conventions

The first deck establishes a visual language that future decks should generally respect unless intentionally redesigned:

### Colors

```python
BG = "#0F172A"      # dark navy background
PANEL = "#111827"   # dark card fill
TEXT = "#E5E7EB"    # primary text
MUTED = "#94A3B8"   # secondary text
BLUE = "#60A5FA"
GREEN = "#34D399"
YELLOW = "#FBBF24"
PINK = "#F472B6"
RED = "#FB7185"
```

### General style

- dark background
- restrained color palette
- color used semantically:
  - blue for core structure / neutral emphasis
  - green for valid roots / positive cases / success
  - yellow for important formulas or transitional emphasis
  - pink / red for alternate or negative cases
- large readable headings
- math-heavy layouts with enough whitespace for classroom projection
- rounded cards for grouped explanations or worked examples

### Layout helpers already present in the first deck

`quadratic_formula_slides.py` defines:

- `title(...)`
- `footer(...)`
- `card(...)`
- `clear_to(...)`

The `card(...)` helper now auto-fits content to the interior of the box. This was added after discovering that fixed cards could allow text to overflow. If common helpers are later extracted into a shared module, preserve this behavior.

---

## Lesson-design expectations

Future decks should generally include a healthy mix of:

- conceptual explanation
- visual interpretation
- symbolic manipulation
- worked examples
- prediction / discussion moments
- practice questions
- some form of summary or takeaway

A good Algebra 2 deck should answer not only **how** to do a procedure, but also:

- what the mathematical objects mean
- what is happening visually
- why a transformation is legal
- how different representations connect
- what students should notice before calculating

### Example from the current quadratic deck

The current deck includes:

- what it means to solve a quadratic
- graph interpretation of roots / zeros / x-intercepts
- coefficient effects on a parabola
- discriminant cases
- a teacher-controlled discriminant question sequence
- animated derivation of the quadratic formula
- worked examples
- a solving routine
- practice problems and answer check

This is a useful model for future lesson depth.

---

## Animation conventions and lessons learned

### Use `TransformMatchingTex` when algebraic identity matters

When showing symbolic transformations, prefer expressions split into meaningful parts:

```python
MathTex(r"x^2", r"+", r"\frac{b}{a}x", r"=", r"-\frac{c}{a}")
```

This makes it easier to animate pieces honestly and lets students track terms.

### Use animations to expose legal algebraic moves

The current quadratic derivation intentionally shows:

- division by `a`
- `c` moving across the equals sign
- sign change becoming visible
- adding the same square-completing term to both sides
- factoring the left side
- square roots introducing `\pm`
- moving `b/(2a)` across and flipping the sign
- combining terms into the final formula

This is the desired standard for derivation-heavy slides.

### Avoid visually noisy morphs when they harm clarity

Earlier versions used broad transformations that made many symbols fly across one another at once. This looked clever but was pedagogically weaker. Prefer motion that lets the eye follow the exact mathematical idea.

### Presenter-controlled sequences

If the teacher needs time to ask a question, do not put all states inside one continuous animation. Insert `self.next_slide()` between states.

Example pattern:

```python
self.play(Create(graph))
self.next_slide()  # teacher asks question
self.play(tracker.animate.set_value(...))
self.next_slide()  # teacher asks next question
```

This is especially useful for:

- discriminant cases
- graph transformations
- domain/range predictions
- end behavior
- inverse-function checks
- function-family comparisons

---

## Rendering and export workflow

### Install dependencies

```bash
uv sync
```

### Quick development render

Use low quality only while iterating:

```bash
uv run manim-slides render --quality l quadratic_formula_slides.py QuadraticFormulaDeck
```

Low quality produces **854×480 at 15 fps**. It is useful for speed, but it is not suitable for final projection.

### Final classroom-ready render

```bash
uv run manim-slides render --quality h quadratic_formula_slides.py QuadraticFormulaDeck
```

### Export to HTML

```bash
uv run manim-slides convert QuadraticFormulaDeck quadratic_formula_deck.html
```

The HTML file references generated media assets in an accompanying assets directory unless the `--one-file` option is explicitly used.

### Verify resolution after export

If quality matters, verify the active generated slide media rather than assuming the latest render was high-res:

```bash
python3 - <<'PY'
import json
from pathlib import Path
cfg = json.loads(Path('slides/QuadraticFormulaDeck.json').read_text())
print(cfg['slides'][0]['file'])
PY
```

Then inspect the resulting file with `ffprobe` if desired.

Expected final classroom output for the current baseline:

```text
width=1920
height=1080
r_frame_rate=60/1
```

### Important workflow warning

If a deck was last rendered at low quality and then exported to HTML, the HTML export will use the low-quality slide media. Always do the **final high-quality render before the final HTML conversion**.

---

## How to add a new presentation

A future agent adding a lesson should usually:

1. Create a new file, for example:

   ```text
   exponential_functions_slides.py
   ```

2. Define a clear `Slide` subclass, for example:

   ```python
   class ExponentialFunctionsDeck(Slide):
       ...
   ```

3. Reuse the established visual style unless there is a deliberate curriculum-wide redesign.

4. Build the lesson in logical sections with comments, such as:

   ```python
   # Slide 1: title
   # Slide 2: what the object means
   # Slide 3: graph interpretation
   # Slide 4: worked example
   ```

5. Include enough `self.next_slide()` calls for live instruction.

6. Render at low quality while iterating.

7. Inspect actual rendered frames for overlap, clipping, or bad transitions.

8. Produce a final high-quality render and HTML export.

9. Update documentation if the new lesson changes project conventions or introduces new reusable patterns.

---

## Quality-control checklist for future agents

Before declaring a deck finished, check all of the following:

### Layout

- no text overflows cards
- no labels collide with graphs
- no equations collide with headings or captions
- no worked examples feel cramped
- all text remains readable at projected scale

### Layout lessons learned from later deck cleanup

Several real issues appeared while polishing `imaginary_solutions_slides.py`. Future contributors should treat these as common failure modes, not one-off accidents:

- **Always inspect the longest content, not just the average case.** A row such as `\sqrt{-50}=\sqrt{25}\sqrt{2}\sqrt{-1}=5\sqrt{2}i` may collide with a nearby card even when the shorter examples above it look fine. If one line is much longer than the others, scale or shift the whole group deliberately rather than assuming a layout that works for the first two lines works for the third.
- **Side-by-side graphs need more separation than expected once labels are added.** Two graph regions can technically fit while their titles, root labels, captions, or explanatory bridge text still overlap. When placing multiple graphs on one slide, budget space for every annotation, not just the axes themselves.
- **Top labels can collide with nearby visuals even when the slide feels spacious.** In the imaginary-solutions quadratic-formula example, `a=1, b=4, c=13` overlapped the top-left of a graph. Keep coefficient lines, legends, and graph labels out of each other's bounding boxes; horizontal relocation is often cleaner than shrinking everything.
- **Text rendering choice matters.** Plain `Text(...)` can produce ugly spacing when a long sentence is compressed into a narrow footer or when multiple fragments are packed too tightly. For math-adjacent typography, `MathTex(r"\text{...}")` may render more consistently, or split text into shorter intentionally spaced pieces.
- **Do not trust conceptual correctness as a proxy for visual correctness.** A slide can be mathematically right and still be presentation-wrong if a box corner is touched, labels crowd each other, or typography looks accidental.

### Recommended visual verification workflow

After any nontrivial layout change:

1. Render a low-quality development version.
2. Inspect the actual rendered slide frames, especially the densest final states after all animations have appeared.
3. For long decks, export representative stills or a contact sheet and then inspect suspicious slides individually at larger size.
4. Re-run the final high-quality render only after those visual checks pass.
5. Regenerate the HTML export after the final render so the exported deck picks up the corrected slide assets.

This matters because some problems only become obvious in rendered output:

- cards that look acceptable in code but are too close in the image
- graph labels that collide only after a later animation stage
- footer text that technically fits but reads as visually broken
- low-quality exports accidentally being mistaken for final output

### Animation

- symbolic motion teaches something concrete
- no animation passes awkwardly through unrelated text unless intentional and legible
- question moments have presenter-controlled pauses where appropriate
- animations are not so fast that students cannot track them

### Pedagogy

- the lesson explains meaning, not just procedure
- at least some examples are worked fully
- practice questions are included where appropriate
- final takeaways are explicit

### Output

- development render tested successfully
- final render done at `--quality h` or better
- HTML export regenerated after the final render
- active assets verified as high resolution when projection quality matters

---

## Current known caveats / cleanup opportunities

### 1. Shared style utilities are still local to one file

The current helper methods and color palette live inside `quadratic_formula_slides.py`. Once several decks exist, consider extracting common items into a shared module, for example:

```text
algebra2_theme.py
```

Possible future shared contents:

- color constants
- title / footer helpers
- card helper
- common graph styling
- equation animation utilities
- common typography scale

Do this when there is enough repetition to justify it; do not prematurely over-abstract after only one deck.

### 2. Generated files are numerous

Manim and Manim Slides create many generated assets. Source files should remain the conceptual source of truth. Be cautious about editing generated files manually.

### 3. README is still focused on the current lesson

As the repository grows into a curriculum, the README should eventually become curriculum-level documentation, while individual lessons may get their own brief metadata or lesson index entry.

### 4. `main.py` is not currently useful

It is leftover starter boilerplate and can eventually be removed or repurposed if a curriculum-level CLI / index script becomes useful.

---

## Guidance for AI agents working in this repository

### First steps when starting work

1. Read `CONTEXT.md`.
2. Read `README.md`.
3. Inspect the target lesson file before editing.
4. Determine whether the user wants:
   - a new lesson
   - a revision to an existing lesson
   - a curriculum-wide convention change
5. Preserve current educational intent unless the user asks for a redesign.

### When the request is broad

If asked to “improve” a lesson, do not immediately patch randomly. First inspect the deck and identify the meaningful options:

- pacing improvements
- mathematical clarity improvements
- visual cleanup
- additional examples
- deeper conceptual explanation
- higher teacher control

Then choose or discuss the right direction.

### When editing math animations

Prefer correctness and legibility over cleverness. Make sure every symbolic change corresponds to a mathematically valid operation and that the motion reinforces that operation.

### When adding interactive / teacher-led beats

Remember that Manim Slides uses `self.next_slide()` to define presenter stops. If the teacher wants to ask students a question before revealing something, make it a real stop rather than a timed animation.

### When changing export workflow

The final intended delivery path is currently **HTML export**, not the desktop Qt presenter. Browser scaling is preferred for actual presentation use.

### When finishing work

Report:

- what changed
- why it changed pedagogically
- how to render/export it
- whether the final output was regenerated and at what resolution

---

## Current lesson summary: quadratic formula deck

### Source

```text
quadratic_formula_slides.py
```

### Scene

```text
QuadraticFormulaDeck
```

### Final export

```text
quadratic_formula_deck.html
```

### Current major sections

1. Title
2. What solving a quadratic means
3. Graph interpretation of roots
4. Coefficient behavior
5. Discriminant cases with presenter-controlled parabola states
6. Deriving the quadratic formula by completing the square
7. Worked examples
8. Solving routine
9. Practice
10. Answer check / closing takeaway

### Distinctive teaching features already implemented

- graphs tied directly to symbolic solutions
- discriminant visualization with teacher pause points
- algebra derivation that visually tracks moved terms and sign changes
- worked examples with multiple solution types
- practice problems and answer key

---

## Suggested future curriculum direction

The repository is intended to become a complete Algebra 2 course. Future lesson families may include:

- review of linear and quadratic functions
- polynomial operations and polynomial functions
- factoring techniques
- complex numbers
- rational exponents and radicals
- exponential functions
- logarithmic functions
- rational functions
- sequences and series
- probability and statistics topics as appropriate to the chosen Algebra 2 scope
- trigonometric foundations if included in the course design

Do not assume exact sequencing without user direction, but design individual decks so they can eventually fit into a coherent course arc.

---

## Practical commands reference

### Install / sync

```bash
uv sync
```

### Fast development render

```bash
uv run manim-slides render --quality l quadratic_formula_slides.py QuadraticFormulaDeck
```

### Final render

```bash
uv run manim-slides render --quality h quadratic_formula_slides.py QuadraticFormulaDeck
```

### HTML export

```bash
uv run manim-slides convert QuadraticFormulaDeck quadratic_formula_deck.html
```

### Example for a future lesson

```bash
uv run manim-slides render --quality h exponential_functions_slides.py ExponentialFunctionsDeck
uv run manim-slides convert ExponentialFunctionsDeck exponential_functions_deck.html
```

---

## Final note

This repository should evolve toward being easy for a teacher to trust:

- mathematically accurate
- visually consistent
- easy to present live
- easy to extend lesson by lesson
- crisp enough for real classroom projection

When in doubt, optimize for the student seeing the idea clearly and the teacher having control over the room.
