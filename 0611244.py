from manim import *

class VectoresParalelos(Scene):
    def construct(self):
        # Crear los vectores
        vector_a = np.array([3, 1, 0])
        vector_b = np.array([6, 2, 0])  # Vector paralelo a `vector_a` (proporcionales)

        # Crear el plano cartesiano
        plane = NumberPlane(
            x_range=[-5, 10, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_color": BLACK, "stroke_opacity": 0.5}
        )
        
        # Definir los vectores en el gráfico
        vec_a = Arrow(start=plane.c2p(0, 0), end=plane.c2p(*vector_a), color=GREEN, buff=0)
        vec_b = Arrow(start=plane.c2p(0, 0), end=plane.c2p(*vector_b), color=BLUE, buff=0)

        # Mostrar etiquetas para los vectores
        label_a = MathTex(r"\vec{a} = (3, 1)").next_to(vec_a.get_end(), RIGHT)
        label_b = MathTex(r"\vec{b} = (6, 2)").next_to(vec_b.get_end(), UP)

        # Título indicando que son paralelos
        titulo = Text("Vectores Paralelos").to_corner(DOWN + RIGHT)

        # Descripción de la relación de paralelismo
        paralelismo_formula = MathTex(r"\vec{b} = 2 \cdot \vec{a}").to_edge(UP)
        
        # Descripción final, con fuente más pequeña y posición ajustada
        descripcion = Text("Como sus coordenadas son proporcionales, es un vector paralelo.")
        descripcion.scale(0.6)
        descripcion.to_corner(DOWN + LEFT, buff=1) 

        # Agregar todos los elementos a la escena
        self.play(Create(plane))
        self.play(GrowArrow(vec_a), Write(label_a))
        self.play(GrowArrow(vec_b), Write(label_b))
        self.play(Write(paralelismo_formula))
        self.play(Write(titulo))
        self.play(Write(descripcion))

        # Mostrar la escena final por unos segundos
        self.wait(3)
