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


class QuadraticFormulaDeck(Slide):
    """A slide deck introducing what it means to solve a quadratic equation."""

    def title(self, text: str, subtitle: str | None = None) -> VGroup:
        heading = Text(text, font_size=34, color=TEXT, weight=BOLD).to_edge(UP)
        items = [heading]
        if subtitle:
            sub = Text(subtitle, font_size=20, color=MUTED).next_to(heading, DOWN, buff=0.15)
            items.append(sub)
        return VGroup(*items)

    def footer(self, text: str) -> Text:
        return Text(text, font_size=16, color=MUTED).to_edge(DOWN)

    def card(
        self,
        *mobjects: Mobject,
        width: float = 5.4,
        height: float = 2.5,
        buff: float = 0.22,
        inner_margin: float = 0.32,
    ) -> VGroup:
        box = RoundedRectangle(
            corner_radius=0.18,
            width=width,
            height=height,
            stroke_color=BLUE,
            stroke_opacity=0.5,
            fill_color=PANEL,
            fill_opacity=0.95,
        )
        content = VGroup(*mobjects).arrange(DOWN, buff=buff)
        max_width = width - 2 * inner_margin
        max_height = height - 2 * inner_margin
        scale_factor = min(
            1,
            max_width / content.width if content.width else 1,
            max_height / content.height if content.height else 1,
        )
        content.scale(scale_factor)
        content.move_to(box)
        return VGroup(box, content)

    def clear_to(self, *mobjects: Mobject) -> None:
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.45)
        self.add(*mobjects)

    def construct(self) -> None:
        # Slide 1: title
        title = Text("Solving Quadratics", font_size=50, color=TEXT, weight=BOLD)
        subtitle = Text("What the answers mean, how the graph behaves, and why the formula works", font_size=24, color=MUTED)
        formula = MathTex(r"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}", color=YELLOW).scale(1.25)
        group = VGroup(title, subtitle, formula).arrange(DOWN, buff=0.35)
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.15))
        self.play(Write(formula))
        self.next_slide()

        # Slide 2: what solving means
        heading = self.title("1. What does it mean to solve a quadratic?")
        equation = MathTex(r"x^2-5x+6=0", color=TEXT).scale(1.15)
        prompt = Text("Find every x-value that makes the equation true.", font_size=25, color=MUTED)
        checks = VGroup(
            MathTex(r"x=2:\quad 2^2-5(2)+6=0", color=GREEN),
            MathTex(r"x=3:\quad 3^2-5(3)+6=0", color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        answer = MathTex(r"\text{Solutions: }x=2\text{ and }x=3", color=YELLOW)
        body = VGroup(equation, prompt, checks, answer).arrange(DOWN, buff=0.35)
        self.clear_to(heading)
        self.play(Write(equation), FadeIn(prompt))
        self.next_slide()
        self.play(LaggedStart(*[Write(line) for line in checks], lag_ratio=0.3))
        self.play(Write(answer))
        self.next_slide()

        # Slide 3: equation ↔ graph
        heading = self.title("2. The same solutions appear on the graph")
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-4, 8, 2],
            x_length=6.2,
            y_length=4.2,
            axis_config={"color": MUTED, "include_numbers": True, "font_size": 20},
        ).shift(LEFT * 3.1 + DOWN * 0.2)
        graph = axes.plot(lambda x: x**2 - 5 * x + 6, x_range=[-0.4, 5.4], color=BLUE)
        graph_label = axes.get_graph_label(graph, MathTex(r"y=x^2-5x+6", color=BLUE), x_val=4.6, direction=UP)
        dots = VGroup(
            Dot(axes.c2p(2, 0), color=GREEN),
            Dot(axes.c2p(3, 0), color=GREEN),
        )
        root_labels = VGroup(
            MathTex(r"x=2", color=GREEN).scale(0.8).next_to(dots[0], DOWN),
            MathTex(r"x=3", color=GREEN).scale(0.8).next_to(dots[1], DOWN),
        )
        side = self.card(
            Text("Graph meaning", font_size=25, color=TEXT, weight=BOLD),
            Text("Solving y = 0 means:", font_size=20, color=MUTED),
            MathTex(r"\text{Where does the parabola cross the }x\text{-axis?}", color=YELLOW).scale(0.68),
            Text("Those crossings are called roots, zeros, or x-intercepts.", font_size=18, color=TEXT),
            width=5.2,
            height=2.9,
        ).shift(RIGHT * 3.1 + DOWN * 0.1)
        self.clear_to(heading)
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.play(FadeIn(side))
        self.next_slide()
        self.play(LaggedStart(FadeIn(dots[0]), Write(root_labels[0]), FadeIn(dots[1]), Write(root_labels[1]), lag_ratio=0.25))
        self.next_slide()

        # Slide 4: anatomy and dynamics
        heading = self.title("3. What the coefficients do")
        equation = MathTex(r"ax^2+bx+c=0", color=TEXT).scale(1.2).to_edge(LEFT).shift(UP * 1.6 + RIGHT * 0.7)
        a_note = Text("a: opens up/down and controls width", font_size=22, color=BLUE)
        b_note = Text("b: shifts the axis of symmetry", font_size=22, color=PINK)
        c_note = Text("c: y-intercept", font_size=22, color=GREEN)
        notes = VGroup(a_note, b_note, c_note).arrange(DOWN, aligned_edge=LEFT, buff=0.25).next_to(equation, DOWN, aligned_edge=LEFT, buff=0.45)
        mini_axes = Axes(x_range=[-4, 4, 1], y_range=[-2, 8, 2], x_length=5.1, y_length=3.8, axis_config={"color": MUTED}).shift(RIGHT * 3.1 + DOWN * 0.2)
        up_graph = mini_axes.plot(lambda x: 0.6 * (x - 1) ** 2 - 1, color=BLUE)
        down_graph = mini_axes.plot(lambda x: -0.6 * (x - 1) ** 2 + 5, color=PINK)
        symmetry = DashedLine(mini_axes.c2p(1, -2), mini_axes.c2p(1, 8), color=YELLOW)
        c_dot = Dot(mini_axes.c2p(0, -0.4), color=GREEN)
        c_label = MathTex(r"c", color=GREEN).next_to(c_dot, LEFT)
        self.clear_to(heading)
        self.play(Write(equation), LaggedStart(*[FadeIn(n, shift=RIGHT * 0.15) for n in notes], lag_ratio=0.2))
        self.play(Create(mini_axes), Create(up_graph))
        self.next_slide()
        self.play(Transform(up_graph, down_graph), run_time=1.2)
        self.play(Create(symmetry), FadeIn(c_dot), Write(c_label))
        self.next_slide()

        # Slide 5: discriminant dynamics
        heading = self.title("4. The discriminant predicts the number of real solutions")
        disc = MathTex(r"\Delta=b^2-4ac", color=YELLOW).scale(1.2).shift(UP * 1.7)
        cases = VGroup(
            self.card(MathTex(r"\Delta>0", color=GREEN), Text("two real roots", font_size=22, color=TEXT), width=3.3, height=1.7),
            self.card(MathTex(r"\Delta=0", color=YELLOW), Text("one repeated root", font_size=22, color=TEXT), width=3.3, height=1.7),
            self.card(MathTex(r"\Delta<0", color=RED), Text("no real roots", font_size=22, color=TEXT), width=3.3, height=1.7),
        ).arrange(RIGHT, buff=0.35).shift(DOWN * 1.7)
        moving_axes = Axes(x_range=[-4, 4, 1], y_range=[-3, 6, 1], x_length=5.1, y_length=3.2, axis_config={"color": MUTED}).shift(UP * 0.15)
        tracker = ValueTracker(-2)
        curve = always_redraw(lambda: moving_axes.plot(lambda x: (x - 0.5) ** 2 + tracker.get_value(), color=BLUE))
        label_prefix = MathTex(r"y=(x-0.5)^2", color=BLUE).scale(0.7)
        label_value = DecimalNumber(
            tracker.get_value(),
            include_sign=True,
            num_decimal_places=1,
            color=BLUE,
        ).scale(0.7)
        label_value.add_updater(lambda mob: mob.set_value(tracker.get_value()))
        label = VGroup(label_prefix, label_value).arrange(RIGHT, buff=0.08).next_to(moving_axes, RIGHT)
        question = Text("How many real solutions?", font_size=22, color=MUTED).next_to(moving_axes, LEFT, buff=0.55)
        self.clear_to(heading)
        self.play(Write(disc), FadeIn(cases))
        self.next_slide()
        self.play(Create(moving_axes), Create(curve), FadeIn(label), FadeIn(question))
        self.next_slide()
        self.play(tracker.animate.set_value(0), run_time=1.5)
        self.next_slide()
        self.play(tracker.animate.set_value(2), run_time=1.5)
        self.next_slide()

        # Slide 6: derivation animation
        heading = self.title("5. Turning standard form into the quadratic formula", "Completing the square, one legal move at a time")
        steps = [
            MathTex(r"ax^2", r"+", r"bx", r"+", r"c", r"=", r"0", color=TEXT),
            MathTex(r"x^2", r"+", r"\frac{b}{a}x", r"+", r"\frac{c}{a}", r"=", r"0", color=TEXT),
            MathTex(r"x^2", r"+", r"\frac{b}{a}x", r"=", r"-\frac{c}{a}", color=TEXT),
            MathTex(
                r"x^2",
                r"+",
                r"\frac{b}{a}x",
                r"+",
                r"\left(\frac{b}{2a}\right)^2",
                r"=",
                r"-\frac{c}{a}",
                r"+",
                r"\left(\frac{b}{2a}\right)^2",
                color=TEXT,
            ),
            MathTex(r"\left(x+\frac{b}{2a}\right)^2", r"=", r"\frac{b^2-4ac}{4a^2}", color=TEXT),
            MathTex(r"x", r"+", r"\frac{b}{2a}", r"=", r"\pm", r"\frac{\sqrt{b^2-4ac}}{2a}", color=TEXT),
            MathTex(r"x", r"=", r"-\frac{b}{2a}", r"\pm", r"\frac{\sqrt{b^2-4ac}}{2a}", color=TEXT),
            MathTex(r"x", r"=", r"\frac{-b\pm\sqrt{b^2-4ac}}{2a}", color=YELLOW),
        ]
        captions = [
            "Start in standard form",
            "Divide every term by a",
            "Move c to the other side; its sign flips",
            "Add the same square-completing term to both sides",
            "Factor the left and combine the right",
            "Take square roots: ± creates two branches",
            "Move b/(2a) across; the sign flips",
            "Combine into the quadratic formula",
        ]
        equation_anchor = ORIGIN + DOWN * 0.05
        caption_anchor = ORIGIN + DOWN * 1.35
        current = steps[0].scale(1.0).move_to(equation_anchor)
        caption = Text(captions[0], font_size=23, color=MUTED).move_to(caption_anchor)
        self.clear_to(heading)
        self.play(Write(current), FadeIn(caption))
        # Divide by a.
        self.next_slide()
        divided = steps[1].scale(1.0).move_to(equation_anchor)
        self.play(
            TransformMatchingTex(current, divided, transform_mismatches=True),
            Transform(caption, Text(captions[1], font_size=23, color=MUTED).move_to(caption_anchor)),
            run_time=1.1,
        )
        current = divided

        # Move c/a across the equals sign and flip its sign.
        self.next_slide()
        moved_c = steps[2].scale(1.0).move_to(equation_anchor)
        self.play(Indicate(current[4], color=YELLOW), run_time=0.5)
        self.play(
            TransformMatchingTex(current, moved_c, transform_mismatches=True, path_arc=-PI / 2),
            Transform(caption, Text(captions[2], font_size=23, color=MUTED).move_to(caption_anchor)),
            run_time=1.25,
        )
        self.play(Indicate(moved_c[-1], color=YELLOW), run_time=0.45)
        current = moved_c

        # Add the same completing-square term to both sides.
        self.next_slide()
        completed = steps[3].scale(0.92).move_to(equation_anchor)
        square_seed = MathTex(r"\left(\frac{b}{2a}\right)^2", color=YELLOW).scale(0.78).next_to(current, UP, buff=0.48)
        self.play(FadeIn(square_seed, shift=DOWN * 0.12))
        self.play(
            TransformMatchingTex(current, completed, transform_mismatches=True),
            ReplacementTransform(square_seed.copy(), completed[4]),
            ReplacementTransform(square_seed, completed[-1]),
            Transform(caption, Text(captions[3], font_size=23, color=MUTED).move_to(caption_anchor)),
            run_time=1.35,
        )
        current = completed

        # Factor and simplify.
        self.next_slide()
        factored = steps[4].scale(1.0).move_to(equation_anchor)
        self.play(
            TransformMatchingTex(current, factored, transform_mismatches=True),
            Transform(caption, Text(captions[4], font_size=23, color=MUTED).move_to(caption_anchor)),
            run_time=1.2,
        )
        current = factored

        # Take square roots.
        self.next_slide()
        rooted = steps[5].scale(1.0).move_to(equation_anchor)
        plus_minus = rooted[4].copy().set_color(YELLOW)
        self.play(
            TransformMatchingTex(current, rooted, transform_mismatches=True),
            Transform(caption, Text(captions[5], font_size=23, color=MUTED).move_to(caption_anchor)),
            run_time=1.2,
        )
        self.play(Flash(rooted[4], color=YELLOW, flash_radius=0.35), run_time=0.6)
        current = rooted

        # Move b/(2a) across and flip the sign.
        self.next_slide()
        isolated = steps[6].scale(1.0).move_to(equation_anchor)
        self.play(Indicate(current[2], color=YELLOW), run_time=0.5)
        self.play(
            TransformMatchingTex(current, isolated, transform_mismatches=True, path_arc=-PI / 2),
            Transform(caption, Text(captions[6], font_size=23, color=MUTED).move_to(caption_anchor)),
            run_time=1.25,
        )
        self.play(Indicate(isolated[2], color=YELLOW), run_time=0.45)
        current = isolated

        # Combine into the final formula.
        self.next_slide()
        final_formula = steps[7].scale(1.0).move_to(equation_anchor)
        self.play(
            TransformMatchingTex(current, final_formula, transform_mismatches=True),
            Transform(caption, Text(captions[7], font_size=23, color=MUTED).move_to(caption_anchor)),
            run_time=1.2,
        )
        current = final_formula
        glow = SurroundingRectangle(current, color=YELLOW, buff=0.18)
        self.play(Create(glow), current.animate.scale(1.08), run_time=0.8)
        self.next_slide()

        # Slide 7: worked examples
        heading = self.title("6. Worked examples")
        ex1 = self.card(
            Text("Example A", font_size=23, color=BLUE, weight=BOLD),
            MathTex(r"x^2-5x+6=0", color=TEXT),
            MathTex(r"x=\frac{5\pm\sqrt{25-24}}{2}", color=TEXT),
            MathTex(r"x=2,3", color=GREEN),
            width=4.0,
            height=3.0,
            buff=0.18,
        )
        ex2 = self.card(
            Text("Example B", font_size=23, color=PINK, weight=BOLD),
            MathTex(r"2x^2+4x-3=0", color=TEXT),
            MathTex(r"x=\frac{-4\pm\sqrt{16+24}}{4}", color=TEXT),
            MathTex(r"x=\frac{-2\pm\sqrt{10}}{2}", color=GREEN),
            width=4.0,
            height=3.0,
            buff=0.18,
        )
        ex3 = self.card(
            Text("Example C", font_size=23, color=YELLOW, weight=BOLD),
            MathTex(r"x^2+4x+5=0", color=TEXT),
            MathTex(r"\Delta=16-20=-4", color=TEXT),
            MathTex(r"\text{No real roots}", color=RED),
            width=4.0,
            height=3.0,
            buff=0.18,
        )
        examples = VGroup(ex1, ex2, ex3).arrange(RIGHT, buff=0.28).shift(DOWN * 0.25)
        self.clear_to(heading)
        self.play(LaggedStart(*[FadeIn(ex, shift=UP * 0.2) for ex in examples], lag_ratio=0.22))
        self.next_slide()

        # Slide 8: strategy checklist
        heading = self.title("7. A reliable solving routine")
        routine = VGroup(
            Text("1. Put the equation in ax² + bx + c = 0 form.", font_size=25, color=TEXT),
            Text("2. Identify a, b, and c carefully — including signs.", font_size=25, color=TEXT),
            Text("3. Compute the discriminant b² − 4ac.", font_size=25, color=TEXT),
            Text("4. Substitute into the formula and simplify.", font_size=25, color=TEXT),
            Text("5. Interpret the roots on the graph.", font_size=25, color=TEXT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        self.clear_to(heading)
        self.play(LaggedStart(*[FadeIn(line, shift=RIGHT * 0.2) for line in routine], lag_ratio=0.16))
        self.next_slide()

        # Slide 9: practice
        heading = self.title("8. Practice")
        practice = VGroup(
            MathTex(r"1.\; x^2+7x+10=0", color=TEXT),
            MathTex(r"2.\; 3x^2-x-2=0", color=TEXT),
            MathTex(r"3.\; x^2-6x+9=0", color=TEXT),
            MathTex(r"4.\; 2x^2+2x+5=0", color=TEXT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.36).shift(LEFT * 2.5)
        prompts = VGroup(
            Text("For each one:", font_size=25, color=BLUE, weight=BOLD),
            Text("• identify a, b, c", font_size=23, color=TEXT),
            Text("• predict the number of real roots", font_size=23, color=TEXT),
            Text("• solve exactly", font_size=23, color=TEXT),
            Text("• sketch what the graph should do", font_size=23, color=TEXT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).shift(RIGHT * 2.4)
        self.clear_to(heading)
        self.play(FadeIn(practice, shift=RIGHT * 0.15), FadeIn(prompts, shift=LEFT * 0.15))
        self.next_slide()

        # Slide 10: answer key / closing
        heading = self.title("9. Practice check + big picture")
        answers = VGroup(
            MathTex(r"1.\; x=-5,-2", color=GREEN),
            MathTex(r"2.\; x=1,-\frac{2}{3}", color=GREEN),
            MathTex(r"3.\; x=3\text{ (double root)}", color=YELLOW),
            MathTex(r"4.\; \text{no real roots}", color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).shift(LEFT * 3.0)
        takeaway = self.card(
            Text("Takeaway", font_size=26, color=BLUE, weight=BOLD),
            Text("Solving a quadratic means finding where its parabola meets y = 0.", font_size=20, color=TEXT),
            Text("The formula packages every possible quadratic into one method.", font_size=20, color=TEXT),
            MathTex(r"b^2-4ac", color=YELLOW),
            Text("tells you what kind of answer to expect before you finish.", font_size=20, color=TEXT),
            width=5.4,
            height=3.2,
            buff=0.18,
        ).shift(RIGHT * 2.5)
        footer = self.footer("Roots ↔ x-intercepts ↔ solutions")
        self.clear_to(heading)
        self.play(FadeIn(answers), FadeIn(takeaway), FadeIn(footer))
        self.next_slide()
