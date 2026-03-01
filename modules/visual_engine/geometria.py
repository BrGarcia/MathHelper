import matplotlib.pyplot as plt
import os

class Shape:
    """Classe base para gerenciar a renderização e salvamento de figuras."""
    def __init__(self):
        # Criamos a figura e o eixo (canvas)
        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        
    def setup_canvas(self):
        """Configura o visual 'limpo' para listas de exercícios."""
        self.ax.set_aspect('equal')
        self.ax.axis('off')  # Remove bordas e números dos eixos

    def save(self, filename):
        """Salva a imagem na pasta output."""
        if not os.path.exists('output'):
            os.makedirs('output')
            
        path = f"output/{filename}.png"
        plt.savefig(path, bbox_inches='tight', dpi=300)
        plt.close()
        return path

class RightTriangle(Shape):
    """Gera um Triângulo Retângulo para Teorema de Pitágoras."""
    def __init__(self, base=4, altura=3, labels=None):
        super().__init__()
        self.base = base
        self.altura = altura
        # Labels padrão: catetos 'a', 'b' e hipotenusa 'x'
        self.labels = labels or {"a": "3", "b": "4", "h": "x"}

    def draw(self):
        self.setup_canvas()
        
        # Coordenadas dos vértices: (0,0), (base, 0), (0, altura)
        x = [0, self.base, 0, 0]
        y = [0, 0, self.altura, 0]
        
        # Desenha o triângulo
        self.ax.plot(x, y, color='black', linewidth=2.5)
        
        # Adiciona os textos (rótulos) dos lados
        self.ax.text(self.base/2, -0.4, self.labels["b"], fontsize=14, ha='center')
        self.ax.text(-0.5, self.altura/2, self.labels["a"], fontsize=14, va='center')
        self.ax.text(self.base/2 + 0.3, self.altura/2 + 0.3, self.labels["h"], fontsize=14)

        # Desenha o símbolo do ângulo reto (quadradinho de 90°)
        s = min(self.base, self.altura) * 0.12
        self.ax.plot([0, s, s], [s, s, 0], color='black', linewidth=1.5)
        self.ax.plot(s/2, s/2, 'ko', markersize=2) # O pontinho interno
