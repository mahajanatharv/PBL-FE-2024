from manim import*

class Conditions(Scene):
    def construct(self):
        t1 = Text("Let f : [a , b]")
        t2 = Text("* a and b are 'Real Numbers'", font_size=35)
        t3 = Text("* The function must be continuous and differentiable in the range (a,b)", font_size=35)
        t4 = Text("The Conditions")
        t1.shift(2*UP + 5*LEFT)
        t2.shift(4*LEFT)
        t3.shift(1*DOWN)
        t4.shift(3*UP)
        
        self.play(Write(t4))
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
       
class m_s_lmvt(Scene):
    def construct(self):
        t1 = Text("Then, there must exist some number 'c',")
        t2 = Text("where c ∈ (a,b) such that")
        formula =  MathTex("f'(c)=" , "\\frac{f(b)-f(a)}{b-a}" , font_size=110)
        t1.shift(3*UP + 1*LEFT)
        t2.shift(2*UP+ 3*LEFT)
        formula.shift(1*DOWN)
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(formula))

class graph(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 5],
            y_range=[0, 6],
            x_axis_config={"numbers_to_include": [1 , 2, 3, 4]},
            tips=False)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")
        curve = ax.plot(lambda x: 0.8 * x ** 2 - 3 * x + 4, x_range=[1, 4], color=GREEN_B,)
        
        

        line_1 = ax.get_vertical_line(ax.input_to_graph_point(1, curve), color=MAROON)
        line_2 = ax.get_vertical_line(ax.input_to_graph_point(4, curve), color=MAROON)

        x_vals = [1, 4]
        y_vals = [1.7999999999999998 , 4.800000000000001 ]
        secant = ax.plot_line_graph(x_values=x_vals, y_values=y_vals)

        x_valss = [1.0042 , 2.5018 , 4.5]
        y_valss = [0 , 1.5021 , 3.3056]
        tangent = ax.plot_line_graph(x_values=x_valss, y_values=y_valss)

        t = Text("c (2.501 , 1.502)", font_size=30)
        t.shift(2*DOWN + 1*RIGHT)
        
        self.play(Create(ax), Create(labels))
        self.play(Create(curve))
        self.play(Create(line_1), Create(line_2))
        self.play(Create(secant))
        self.play(Create(tangent))
        self.play(Write(t))







