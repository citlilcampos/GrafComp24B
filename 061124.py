from manim import *

class VectoresOrtogonales(Scene):
    def construct(self):
        # Crear los vectores
        vector_a = np.array([3, 0, 0])
        vector_b = np.array([0, 2, 0])

        # Crear el plano cartesiano
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_color": BLACK, "stroke_opacity": 0.5}
        )
        
        # Definir los vectores en el gráfico
        vec_a = Arrow(start=plane.c2p(0, 0), end=plane.c2p(*vector_a), color=GREEN, buff=0)
        vec_b = Arrow(start=plane.c2p(0, 0), end=plane.c2p(*vector_b), color=RED, buff=0)

        # Mostrar etiquetas para los vectores
        label_a = MathTex(r"\vec{a} = (3, 0)").next_to(vec_a.get_end(), RIGHT)
        label_b = MathTex(r"\vec{b} = (0, 2)").next_to(vec_b.get_end(), UP)

        # Fórmula de ortogonalidad
        ortogonality_formula = MathTex(r"\vec{a} \cdot \vec{b} = 3 \cdot 0 + 0 \cdot 2 = 0").to_edge(UP)

        # Título indicando que son ortogonales
        titulo = Text("Vectores Ortogonales")
        titulo.to_corner(DOWN+RIGHT)

        # Agregar todos los elementos a la escena
        self.play(Create(plane))
        self.play(GrowArrow(vec_a), Write(label_a))
        self.play(GrowArrow(vec_b), Write(label_b))
        self.play(Write(ortogonality_formula))
        self.play(Write(titulo))

        # Descripción final, con fuente más pequeña y posición ajustada
        descripcion = Text("Como el resultado es 0, los vectores son ortogonales.")
        descripcion.scale(0.6)
        descripcion.to_corner(DOWN + LEFT, buff=1) 
        self.play(Write(descripcion))

        # Mostrar la escena final por unos segundos
        self.wait(3)
