
from manim import *

class Exponential_App(Scene):
    def construct(self):

        logo_green = "#87c2a5"
        light_purple = "#a64d79"
        light_yellow = "#ffe599" 
        dark_yellow = "#ff9900"
        dark_red = "#a61c00"
        green = "#54ab79"

        # # start intro
        self.camera.background_color = "#ece6e2"

        square = Square().scale(1.5).shift(1.8*UP)
        square.set_color(logo_green)
        circle = Circle(fill_opacity = 0.5).scale(1.5).shift(1.8*UP)
        circle.set_color(logo_green)
        logo = MathTex('M',' R','L', fill_color=DARK_GRAY)
        logo[0].set_color(DARK_BLUE)
        logo[1].set_color(dark_red)
        logo[2].set_color(dark_red)
        logo.next_to(circle,0,buff = 0).scale(2)
        self.play(DrawBorderThenFill(circle,run_time=5), DrawBorderThenFill(square,run_time=5), Write(logo, run_time = 5))
        self.play(Rotate(square,PI/4))

        logo_text = Tex(r"Math in Real Life", tex_to_color_map={"Math": DARK_BLUE, "in Real Life": dark_red})
        logo_text.shift(0.6*DOWN)
        self.play(FadeIn(logo_text))

        title = Text("Exponential Applications").set_color(light_purple).scale(1.3).shift(2*DOWN)
        self.play(Write(title))
        title1 = Text("Exponential Applications").set_color(light_purple).scale(1.2).to_edge(UL)
        self.play(Transform(title, title1),FadeOut(logo_text,circle,logo, square))
        # # end intro

        # # start page 1
        eq1 = Tex(r"$\dot{y} = k \, y$,").set_color(DARK_GRAY).shift(2*UP).shift(3*LEFT)
        eq1a = Tex(r"$y(t_0) = y_0 $").set_color(DARK_GRAY).shift(2*UP).shift(3*RIGHT)
        arrow1a = Arrow(start = LEFT, end  = RIGHT, max_tip_length_to_length_ratio = 0.15).set_color(light_purple).scale(0.7).next_to(eq1,DOWN)
        eq1b = Tex(r"$y(t) = y_0\, e^{k(t-t_0)}$").set_color(DARK_GRAY).next_to(arrow1a,RIGHT)
        line1a = Line([-5,1,0],[5,1,0]).set_color(dark_yellow)
        eq1c = Tex(r"$\dot{N} = k \, N$,").set_color(DARK_GRAY).next_to(eq1b,DOWN).align_to(eq1,LEFT)
        eq1d = Tex(r"$N(t_0) = N_0 $").set_color(DARK_GRAY).next_to(eq1b,DOWN).align_to(eq1a,LEFT)
        arrow1b = Arrow(start = LEFT, end  = RIGHT, max_tip_length_to_length_ratio = 0.15).set_color(light_purple).scale(0.7).next_to(eq1c,DOWN).align_to(arrow1a,LEFT)
        eq1e = Tex(r"$N(t) = N_0\, e^{k(t-t_0)}$").set_color(DARK_GRAY).next_to(arrow1b,RIGHT)
        line1b = Line([-5,-0.5,0],[5,-0.5,0]).set_color(dark_yellow)
        q1 = Tex(r"Question 1:").set_color(DARK_BLUE).next_to(line1b,DOWN).align_to(title1,LEFT)
        q1a = Tex(r"Suppose there is a collection of objects", tex_to_color_map = {r"Suppose there is a collection of objects": DARK_BROWN}).scale(0.8).next_to(q1,RIGHT).shift(0.8*RIGHT)
        q1b = Tex(r"such that per unit time on average ", r"each ", r"one splits into ", r"3.5 new objects.",tex_to_color_map = {r"such that per unit time on average ": DARK_BROWN, r"each ": green, r"one splits into ": DARK_BROWN, r"3.5": green, r"new objects.": DARK_BROWN}).scale(0.8).next_to(q1a,DOWN)
        q1c = Tex(r"Write the model describing how the number of objects is changing with time.").set_color(DARK_BROWN).scale(0.8).next_to(q1b,DOWN)
        question1 = VGroup(q1a,q1b,q1c,q1)
        sol1 = Tex(r"Solution:").set_color(DARK_BLUE).next_to(q1c,DOWN).align_to(q1,LEFT).shift(2.8*UP)
        sol1a = Tex(r"$N(t + \Delta t) - N(t) = $").set_color(DARK_GRAY).next_to(sol1,RIGHT).shift(RIGHT)
        sol1b = Tex(r"$f \cdot $").set_color(DARK_GRAY).next_to(sol1a,RIGHT)
        sol1c = Tex(r"$ 2.5\, $").set_color(DARK_GRAY).next_to(sol1b,RIGHT)
        circle1 = Circle().set_color(light_purple).scale(0.45).move_to([0.6,1.4,0])
        sol1d = Tex(r"$ N \, \Delta t$").set_color(DARK_GRAY).next_to(sol1c,RIGHT)
        sol1e = Tex(r"$\dot{N} = 2.5 N$").set_color(DARK_GRAY).shift(DOWN)
        sol1f = Tex(r"$N(t) = N(t_0) \, e^{(2.5)(t-t_0)}$").set_color(DARK_GRAY).next_to(sol1e,DOWN).shift(0.3*DOWN)
        arrow1c = Arrow(start = LEFT, end  = RIGHT, max_tip_length_to_length_ratio = 0.15).set_color(light_purple).scale(0.7).next_to(sol1f,LEFT).shift(0.5*LEFT)
        frame1 = SurroundingRectangle(sol1f,buff =0.2).set_color(dark_yellow)
       
        self.play(Write(eq1))
        self.play(Write(eq1a))
        self.play(Create(arrow1a))
        self.play(Write(eq1b))
        self.play(Create(line1a))
        self.play(Write(eq1c))
        self.play(Write(eq1d))
        self.play(Create(arrow1b))
        self.play(Write(eq1e))
        self.play(Create(line1b))
        self.play(Write(q1))
        self.play(AddTextWordByWord(q1a))
        self.play(AddTextWordByWord(q1b))
        self.play(AddTextWordByWord(q1c))
        self.play(FadeOut(eq1,eq1a,eq1b,eq1c,eq1d,eq1e,arrow1a,arrow1b,line1a,line1b))
        self.play(question1.animate.shift(3*UP))

        self.play(Write(sol1))
        self.play(Write(sol1a))
        self.play(Write(sol1b))
        self.play(Write(sol1c))
        self.play(Indicate(q1b[1],scale_factor= 1.2,color = green,run_time = 2))
        self.play(FadeOut(sol1b))
        self.play(Write(sol1d))
        self.play(Write(sol1e))
        self.play(Create(arrow1c))
        self.play(Write(sol1f))
        self.play(Create(frame1))
        self.play(FadeOut(q1,q1a,q1b,q1c,question1,sol1,sol1a,sol1c,sol1d,sol1e,sol1f,arrow1c,frame1))
        # # end page 1
