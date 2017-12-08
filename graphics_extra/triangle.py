import trianglesolver
import math
import graphics
from collections import namedtuple

Medidas = namedtuple('Medidas', 'lado_a lado_b lado_c angulo_a angulo_b angulo_c')


class Triangle(graphics.GraphicsObject):
    def __init__(self, vertice_b, **dados):
        super().__init__(options=["outline", "width", "fill"])
        self.vertice_b = vertice_b
        self.dados = dict(dados)

    def __repr__(self):
        return 'Triangle()'.format()

    def _move(self, dx, dy):
        self.vertice_b._move(dx, dy)

    def _draw(self, canvas, options):
        vertices = [(canvas.toScreen(p.getX(), p.getY())) for p in self.vertices]
        return canvas.create_polygon(*vertices)

    @property
    def medidas(self):
        a, b, c, aA, aB, aC = trianglesolver.solve(
            a=self.dados.get('lado_a'),
            b=self.dados.get('lado_b'),
            c=self.dados.get('lado_c'),
            A=self.dados.get('angulo_a'),
            B=self.dados.get('angulo_b'),
            C=self.dados.get('angulo_c')
        )
        return Medidas(lado_a=a, lado_b=b, lado_c=c, angulo_a=aA, angulo_b=aB, angulo_c=aC)

    @property
    def vertice_c(self):
        return graphics.Point(
            self.vertice_b.getX() + self.medidas.lado_a * math.cos(self.medidas.angulo_b),
            self.vertice_b.getY() - self.medidas.lado_a * math.sin(self.medidas.angulo_b)
        )

    @property
    def vertice_a(self):
        return graphics.Point(
            self.vertice_b.getX() + self.medidas.lado_c,
            self.vertice_b.getY()
        )

    @property
    def vertices(self):
        """
        C
          |\
          | \
        a |  \ b
          |   \
          |____\
        B    c   A

        """
        return (self.vertice_a, self.vertice_b, self.vertice_c)
