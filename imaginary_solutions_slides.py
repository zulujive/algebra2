from __future__ import annotations

from manim import *
from manim_slides import Slide


BG = "#0F172A"
PANEL = "#111827"
TEXT = "#E5E7EB"
MUTED = "#94A3B8"
BLUE = "#60A5FA"
GREEN = "#34D399"
YELLOW = "#FBBF24"
PINK = "#F472B6"
RED = "#FB7185"

config.background_color = BG


class ImaginarySolutionsDeck(Slide):
    """A visual lesson on imaginary and complex quadratic solutions."""

    def title(self, text: str, subtitle: str | None = None) -> VGroup:
        heading = Text(text, font_size=34, color=TEXT, weight=BOLD).to_edge(UP)
        parts = [heading]
        if subtitle:
            parts.append(Text(subtitle, font_size=20, color=MUTED).next_to(heading, DOWN, buff=0.15))
        return VGroup(*parts)

    def footer(self, text: str) -> Text:
        return Text(text, font_size=16, color=MUTED).to_edge(DOWN)

    def card(
        self,
        *mobjects: Mobject,
        width: float = 5.4,
        height: float = 2.5,
        buff: float = 0.22,
        inner_margin: float = 0.32,
        stroke_color: str = BLUE,
    ) -> VGroup:
        box = RoundedRectangle(
            corner_radius=0.18,
            width=width,
            height=height,
            stroke_color=stroke_color,
            stroke_opacity=0.5,
            fill_color=PANEL,
            fill_opacity=0.95,
        )
        content = VGroup(*mobjects).arrange(DOWN, buff=buff)
        max_width = width - 2 * inner_margin
        max_height = height - 2 * inner_margin
        content.scale(min(
            1,
            max_width / content.width if content.width else 1,
            max_height / content.height if content.height else 1,
        ))
        content.move_to(box)
        return VGroup(box, content)

    def clear_to(self, *mobjects: Mobject) -> None:
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.45)
        self.add(*mobjects)

    def construct(self) -> None:
        # Slide 1: title
        title = Text("Imaginary Solutions", font_size=50, color=TEXT, weight=BOLD)
        subtitle = Text("Why i exists, where complex roots live, and how to solve for them", font_size=24, color=MUTED)
        hook = VGroup(
            MathTex(r"x^2+1=0", color=TEXT).scale(1.1),
            MathTex(r"x=\pm i", color=YELLOW).scale(1.35),
        ).arrange(DOWN, buff=0.28)
        intro = VGroup(title, subtitle, hook).arrange(DOWN, buff=0.35)
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.12))
        self.play(Write(hook[0]), Write(hook[1]))
        self.next_slide()

        # Slide 2: the problem that creates i
        heading = self.title("1. Why do we need a new number?")
        real_line = NumberLine(x_range=[-4, 4, 1], length=7, color=MUTED, include_numbers=True).shift(DOWN * 1.0)
        eq = MathTex(r"x^2=-1", color=TEXT).scale(1.2).shift(UP * 1.35)
        examples = VGroup(
            MathTex(r"2^2=4", color=GREEN),
            MathTex(r"(-2)^2=4", color=GREEN),
            MathTex(r"0^2=0", color=GREEN),
        ).arrange(RIGHT, buff=0.6).shift(UP * 0.35)
        prompt = Text("Every real square is nonnegative.", font_size=24, color=MUTED).next_to(examples, DOWN, buff=0.35)
        no_point = Text("So -1 is not reached anywhere on the real line.", font_size=22, color=RED).next_to(real_line, DOWN, buff=0.35)
        minus_one = Dot(real_line.n2p(-1), color=RED)
        self.clear_to(heading)
        self.play(Write(eq), Create(real_line))
        self.play(LaggedStart(*[Write(e) for e in examples], lag_ratio=0.18), FadeIn(prompt))
        self.next_slide()
        self.play(FadeIn(minus_one), FadeIn(no_point))
        self.next_slide()

        # Slide 3: definition and why it is not a trick
        heading = self.title("2. Define i by the job it does")
        definition = MathTex(r"i^2=-1", color=YELLOW).scale(1.45)
        left = self.card(
            Text("Definition", font_size=25, color=BLUE, weight=BOLD),
            MathTex(r"i=\sqrt{-1}", color=TEXT),
            Text("A new number whose square is -1.", font_size=21, color=TEXT),
            width=4.2,
            height=2.3,
        ).shift(LEFT * 3.1 + DOWN * 0.25)
        right = self.card(
            Text("Why it matters", font_size=25, color=PINK, weight=BOLD),
            Text("The reals were once extended too:", font_size=20, color=TEXT),
            MathTex(r"\text{counting} \to \text{negative} \to \text{fraction} \to \text{irrational}", color=MUTED).scale(0.62),
            Text("i extends the number system again.", font_size=20, color=TEXT),
            width=5.0,
            height=2.5,
            stroke_color=PINK,
        ).shift(RIGHT * 2.7 + DOWN * 0.25)
        self.clear_to(heading)
        self.play(Write(definition))
        self.next_slide()
        self.play(FadeIn(left, shift=RIGHT * 0.15), FadeIn(right, shift=LEFT * 0.15))
        self.next_slide()

        # Slide 4: numeric intuition for negative square roots
        heading = self.title("3. What happens when the negative pops out?", "This is the move students use most often")
        start = MathTex(r"\sqrt{-9}", color=TEXT).scale(1.45)
        split = MathTex(r"\sqrt{-9}", r"=", r"\sqrt{9}", r"\sqrt{-1}", color=TEXT).scale(1.25)
        finish = MathTex(r"\sqrt{-9}", r"=", r"3", r"i", color=YELLOW).scale(1.35)
        note = self.card(
            Text("Think of two pieces", font_size=25, color=TEXT, weight=BOLD),
            MathTex(r"\sqrt{\text{size}}\cdot\sqrt{\text{negative part}}", color=TEXT).scale(0.82),
            MathTex(r"\sqrt{9}\cdot\sqrt{-1}=3i", color=GREEN),
            width=5.2,
            height=2.2,
        ).shift(DOWN * 1.55)
        minus_seed = MathTex(r"-1", color=RED).scale(0.9).next_to(start, UP, buff=0.4)
        self.clear_to(heading)
        self.play(Write(start))
        self.next_slide()
        self.play(FadeIn(minus_seed, shift=DOWN * 0.1))
        self.play(
            TransformMatchingTex(start, split, transform_mismatches=True),
            run_time=1.2,
        )
        self.play(minus_seed.animate.move_to(split[-1]), Indicate(split[-1], color=YELLOW), run_time=0.8)
        self.play(FadeOut(minus_seed), run_time=0.25)
        self.next_slide()
        self.play(TransformMatchingTex(split, finish, transform_mismatches=True), FadeIn(note))
        self.next_slide()

        # Slide 5: repeated numeric examples
        heading = self.title("4. The same idea works every time")
        examples = VGroup(
            MathTex(r"\sqrt{-4}=\sqrt{4}\sqrt{-1}=2i", color=GREEN),
            MathTex(r"\sqrt{-16}=\sqrt{16}\sqrt{-1}=4i", color=GREEN),
            MathTex(r"\sqrt{-50}=\sqrt{25}\sqrt{2}\sqrt{-1}=5\sqrt{2}i", color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38).scale(0.9).shift(LEFT * 3.0)
        rule = self.card(
            Text("Useful rule", font_size=25, color=BLUE, weight=BOLD),
            MathTex(r"\sqrt{-k}=\sqrt{k}\,i", color=YELLOW).scale(1.15),
            Text("Pull the negative into its own √(-1).", font_size=21, color=TEXT),
            width=5.0,
            height=2.25,
        ).shift(RIGHT * 3.0)
        self.clear_to(heading)
        self.play(FadeIn(rule))
        self.next_slide()
        self.play(LaggedStart(*[Write(ex) for ex in examples], lag_ratio=0.22))
        self.next_slide()

        # Slide 6: hidden parabola in complex space
        heading = self.title("5. The parabola was not gone — we needed one more axis", "For x² + 1 = 0, the real-number view misses the roots")
        real_axes = Axes(
            x_range=[-3, 3, 1], y_range=[-1, 6, 1], x_length=4.4, y_length=3.0,
            axis_config={"color": MUTED, "include_numbers": True, "font_size": 18},
        ).shift(LEFT * 3.25 + DOWN * 1.0)
        real_graph = real_axes.plot(lambda x: x**2 + 1, x_range=[-2.2, 2.2], color=BLUE)
        real_label = MathTex(r"f(x)=x^2+1", color=BLUE).scale(0.68).next_to(real_axes, UP, buff=0.08)
        no_roots = Text("No real x-intercepts", font_size=21, color=RED).next_to(real_axes, DOWN, buff=0.25)

        imag_axes = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 2, 1], x_length=4.4, y_length=3.0,
            axis_config={"color": MUTED, "include_numbers": True, "font_size": 18},
        ).shift(RIGHT * 3.1 + DOWN * 1.0)
        imag_graph = imag_axes.plot(lambda t: 1 - t**2, x_range=[-2.2, 2.2], color=PINK)
        imag_label = MathTex(r"\text{imaginary-number view}", color=PINK).scale(0.62).next_to(imag_axes, UP, buff=0.08)
        imag_roots = VGroup(Dot(imag_axes.c2p(-1, 0), color=GREEN), Dot(imag_axes.c2p(1, 0), color=GREEN))
        imag_root_labels = VGroup(
            MathTex(r"-i", color=GREEN).scale(0.75).next_to(imag_roots[0], DOWN),
            MathTex(r"i", color=GREEN).scale(0.75).next_to(imag_roots[1], DOWN),
        )
        bridge = VGroup(
            MathTex(r"x^2+1=0", color=TEXT),
            Text("No real answer here...", font_size=20, color=MUTED),
            Text("...so we look on a new imaginary-number axis.", font_size=20, color=YELLOW),
        ).arrange(DOWN, buff=0.12).scale(0.88).shift(UP * 1.75)
        self.clear_to(heading)
        self.play(Create(real_axes), Create(real_graph), Write(real_label), FadeIn(no_roots))
        self.next_slide()
        self.play(FadeIn(bridge))
        self.next_slide()
        self.play(Create(imag_axes), Create(imag_graph), Write(imag_label))
        self.play(FadeIn(imag_roots), LaggedStart(*[Write(l) for l in imag_root_labels], lag_ratio=0.2))
        self.next_slide()

        # Slide 7: one extra axis
        heading = self.title("6. Imaginary solutions live on one extra axis")
        plane = ComplexPlane(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=6.0, y_length=4.8,
            background_line_style={"stroke_color": "#334155", "stroke_opacity": 0.55}, axis_config={"color": MUTED},
        ).add_coordinates().shift(LEFT * 2.75 + DOWN * 0.1)
        roots = VGroup(Dot(plane.n2p(1j), color=GREEN), Dot(plane.n2p(-1j), color=GREEN))
        root_labels = VGroup(MathTex(r"i", color=GREEN).next_to(roots[0], RIGHT), MathTex(r"-i", color=GREEN).next_to(roots[1], RIGHT))
        side = self.card(
            Text("Same equation, larger picture", font_size=24, color=TEXT, weight=BOLD),
            MathTex(r"x^2+1=0", color=TEXT),
            MathTex(r"x=\pm i", color=YELLOW),
            Text("The usual number line is horizontal.", font_size=20, color=TEXT),
            Text("Imaginary answers sit on the new vertical axis.", font_size=20, color=TEXT),
            width=4.9,
            height=2.9,
        ).shift(RIGHT * 3.0)
        self.clear_to(heading)
        self.play(Create(plane), FadeIn(side))
        self.play(LaggedStart(*[FadeIn(r) for r in roots], lag_ratio=0.2), LaggedStart(*[Write(l) for l in root_labels], lag_ratio=0.2))
        self.next_slide()

        # Slide 8: ± creates the pair numerically
        heading = self.title("7. Why do answers usually come in pairs?")
        equation = MathTex(r"x=\pm 3i", color=TEXT).scale(1.35).shift(UP * 1.0)
        pair = VGroup(MathTex(r"x=3i", color=GREEN), MathTex(r"x=-3i", color=GREEN)).arrange(RIGHT, buff=1.1).shift(DOWN * 0.1)
        note = self.card(
            Text("The ± does the work", font_size=25, color=TEXT, weight=BOLD),
            Text("One square-root step creates", font_size=21, color=TEXT),
            Text("a positive answer and a negative answer.", font_size=21, color=TEXT),
            MathTex(r"(3i)^2=(-3i)^2=-9", color=YELLOW),
            width=5.2,
            height=2.5,
        ).shift(DOWN * 1.7)
        self.clear_to(heading)
        self.play(Write(equation))
        self.next_slide()
        self.play(TransformFromCopy(equation, pair[0]), TransformFromCopy(equation, pair[1]), FadeIn(note))
        self.next_slide()

        # Slide 9: class example A
        heading = self.title("8. Class example A", "Solve x² + 9 = 0")
        steps = [
            MathTex(r"x^2", r"+", r"9", r"=", r"0", color=TEXT),
            MathTex(r"x^2", r"=", r"-9", color=TEXT),
            MathTex(r"x", r"=", r"\pm\sqrt{-9}", color=TEXT),
            MathTex(r"x", r"=", r"\pm\sqrt{9}\sqrt{-1}", color=TEXT),
            MathTex(r"x", r"=", r"\pm 3i", color=GREEN),
        ]
        captions = [
            "Start in standard form",
            "Move 9 across; the sign flips",
            "Take square roots",
            "Pull the negative into its own √(-1)",
            "Use √(-1)=i",
        ]
        anchor = ORIGIN + UP * 0.25
        cap_anchor = ORIGIN + DOWN * 1.15
        current = steps[0].scale(1.25).move_to(anchor)
        caption = Text(captions[0], font_size=23, color=MUTED).move_to(cap_anchor)
        side_plane = ComplexPlane(x_range=[-1, 1, 1], y_range=[-4, 4, 1], x_length=2.2, y_length=4.0, axis_config={"color": MUTED}).shift(RIGHT * 4.2)
        top = Dot(side_plane.n2p(3j), color=GREEN)
        bottom = Dot(side_plane.n2p(-3j), color=GREEN)
        side_labels = VGroup(MathTex(r"3i", color=GREEN).scale(0.8).next_to(top, RIGHT), MathTex(r"-3i", color=GREEN).scale(0.8).next_to(bottom, RIGHT))
        self.clear_to(heading)
        self.play(Write(current), FadeIn(caption), Create(side_plane))
        for idx in range(1, len(steps)):
            self.next_slide()
            nxt = steps[idx].scale(1.25).move_to(anchor)
            self.play(
                TransformMatchingTex(current, nxt, transform_mismatches=True, path_arc=-PI / 2 if idx == 1 else 0),
                Transform(caption, Text(captions[idx], font_size=23, color=MUTED).move_to(cap_anchor)),
                run_time=1.15,
            )
            current = nxt
            if idx == 3:
                self.play(FadeIn(top), FadeIn(bottom), Write(side_labels))
        self.next_slide()

        # Slide 10: class example B with quadratic formula
        heading = self.title("9. Class example B", "Solve x² + 4x + 13 = 0")
        line1 = MathTex(r"a=1,\quad b=4,\quad c=13", color=TEXT).scale(0.9).shift(LEFT * 2.55 + UP * 1.35)
        line2 = MathTex(r"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}", color=TEXT)
        line3 = MathTex(r"x=\frac{-4\pm\sqrt{16-52}}{2}", color=TEXT)
        line4 = MathTex(r"x=\frac{-4\pm\sqrt{-36}}{2}", color=TEXT)
        line5 = MathTex(r"x=\frac{-4\pm \sqrt{36}\sqrt{-1}}{2}", color=TEXT)
        line6 = MathTex(r"x=\frac{-4\pm 6i}{2}", color=TEXT)
        line7 = MathTex(r"x=-2\pm 3i", color=GREEN)
        stack = [line2, line3, line4, line5, line6, line7]
        complex_plane = ComplexPlane(
            x_range=[-5, 2, 1], y_range=[-4, 4, 1], x_length=4.7, y_length=4.2,
            background_line_style={"stroke_color": "#334155", "stroke_opacity": 0.45}, axis_config={"color": MUTED},
        ).add_coordinates().shift(RIGHT * 3.55 + DOWN * 0.1)
        roots = VGroup(Dot(complex_plane.n2p(-2 + 3j), color=GREEN), Dot(complex_plane.n2p(-2 - 3j), color=GREEN))
        labels = VGroup(
            MathTex(r"-2+3i", color=GREEN).scale(0.72).next_to(roots[0], UL, buff=0.08),
            MathTex(r"-2-3i", color=GREEN).scale(0.72).next_to(roots[1], DL, buff=0.08),
        )
        self.clear_to(heading)
        self.play(Write(line1), Create(complex_plane))
        current = line2.scale(1.03).shift(LEFT * 2.55 + DOWN * 0.15)
        self.play(Write(current))
        for nxt in stack[1:]:
            self.next_slide()
            nxt.scale(1.03).move_to(current)
            self.play(TransformMatchingTex(current, nxt, transform_mismatches=True), run_time=1.1)
            current = nxt
        self.play(FadeIn(roots), LaggedStart(*[Write(l) for l in labels], lag_ratio=0.2))
        self.next_slide()

        # Slide 11: solving routine
        heading = self.title("10. A reliable routine for imaginary solutions")
        routine = VGroup(
            Text("1. Solve as usual until a negative appears under a square root.", font_size=24, color=TEXT),
            Text("2. Split √(-k) into √k · √(-1).", font_size=24, color=TEXT),
            Text("3. Replace √(-1) with i.", font_size=24, color=TEXT),
            Text("4. Simplify the real-number part.", font_size=24, color=TEXT),
            Text("5. Remember that ± gives the two answers.", font_size=24, color=TEXT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        self.clear_to(heading)
        for line in routine:
            self.play(Write(line), run_time=0.85)
            self.next_slide()

        # Slide 12: student practice
        heading = self.title("11. Try these yourself")
        practice = VGroup(
            MathTex(r"1.\; x^2+16=0", color=TEXT),
            MathTex(r"2.\; x^2-6x+13=0", color=TEXT),
            MathTex(r"3.\; 2x^2+8x+20=0", color=TEXT),
            MathTex(r"4.\; (x-1)^2+9=0", color=TEXT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(LEFT * 2.7)
        prompts = self.card(
            Text("For each one", font_size=25, color=BLUE, weight=BOLD),
            Text("• solve exactly", font_size=22, color=TEXT),
            Text("• show where the negative comes out", font_size=22, color=TEXT),
            Text("• write both ± answers", font_size=22, color=TEXT),
            width=4.7,
            height=2.9,
        ).shift(RIGHT * 2.8)
        self.clear_to(heading)
        self.play(FadeIn(practice, shift=RIGHT * 0.15), FadeIn(prompts, shift=LEFT * 0.15))
        self.next_slide()

        # Slide 13: practice walkthrough A/B
        heading = self.title("12. Practice walkthroughs", "Problems 1 and 2")
        left = self.card(
            Text("1. x² + 16 = 0", font_size=23, color=BLUE, weight=BOLD),
            MathTex(r"x^2=-16", color=TEXT),
            MathTex(r"x=\pm\sqrt{-16}", color=TEXT),
            MathTex(r"x=\pm 4i", color=GREEN),
            width=4.5,
            height=3.0,
        ).shift(LEFT * 2.7)
        right = self.card(
            Text("2. x² - 6x + 13 = 0", font_size=23, color=PINK, weight=BOLD),
            MathTex(r"x=\frac{6\pm\sqrt{36-52}}{2}", color=TEXT),
            MathTex(r"x=\frac{6\pm\sqrt{-16}}{2}", color=TEXT),
            MathTex(r"x=3\pm 2i", color=GREEN),
            width=5.0,
            height=3.0,
            stroke_color=PINK,
        ).shift(RIGHT * 2.65)
        self.clear_to(heading)
        self.play(FadeIn(left, shift=UP * 0.15))
        self.next_slide()
        self.play(FadeIn(right, shift=UP * 0.15))
        self.next_slide()

        # Slide 14: practice walkthrough C/D
        heading = self.title("13. Practice walkthroughs", "Problems 3 and 4")
        left = self.card(
            Text("3. 2x² + 8x + 20 = 0", font_size=23, color=BLUE, weight=BOLD),
            MathTex(r"x=\frac{-8\pm\sqrt{64-160}}{4}", color=TEXT),
            MathTex(r"x=\frac{-8\pm\sqrt{-96}}{4}", color=TEXT),
            MathTex(r"x=-2\pm\sqrt{6}i", color=GREEN),
            width=5.0,
            height=3.0,
        ).shift(LEFT * 2.6)
        right = self.card(
            Text("4. (x - 1)² + 9 = 0", font_size=23, color=PINK, weight=BOLD),
            MathTex(r"(x-1)^2=-9", color=TEXT),
            MathTex(r"x-1=\pm 3i", color=TEXT),
            MathTex(r"x=1\pm 3i", color=GREEN),
            width=4.7,
            height=3.0,
            stroke_color=PINK,
        ).shift(RIGHT * 2.75)
        self.clear_to(heading)
        self.play(FadeIn(left, shift=UP * 0.15))
        self.next_slide()
        self.play(FadeIn(right, shift=UP * 0.15))
        self.next_slide()

        # Slide 15: closing synthesis
        heading = self.title("14. Big picture")
        summary = self.card(
            Text("What changed today?", font_size=27, color=BLUE, weight=BOLD),
            MathTex(r"i^2=-1", color=YELLOW),
            Text("The number line became a plane.", font_size=22, color=TEXT),
            Text("No real roots can still mean real structure.", font_size=22, color=TEXT),
            Text("Complex roots reveal the rest of the graph's story.", font_size=22, color=TEXT),
            width=6.3,
            height=3.25,
        )
        footer = MathTex(
            r"\text{Real axis = one slice.}\qquad \text{Complex plane = the fuller picture.}",
            color=MUTED,
        ).scale(0.62).to_edge(DOWN)
        self.clear_to(heading)
        self.play(FadeIn(summary), FadeIn(footer))
        self.next_slide()
