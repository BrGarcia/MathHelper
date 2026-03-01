from modules.visual_engine.geometria import RightTriangle

def generate_sample_exercise():
    print("🚀 MathHelper: Gerando protótipo de geometria...")
    
    # Criamos um triângulo retângulo clássico (3, 4, x)
    # Aqui você pode mudar os valores para testar!
    exercicio = RightTriangle(base=4, altura=3, labels={"a": "6 cm", "b": "8 cm", "h": "x"})
    
    exercicio.draw()
    path = exercicio.save("test_pitagoras")
    
    print(f"✅ Sucesso! Imagem gerada em: {path}")

if __name__ == "__main__":
    generate_sample_exercise()
