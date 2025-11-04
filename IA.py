# ai_explainer.py
import openai
from typing import Optional, List

# 🔹 Importamos tus funciones desde tu librería
from PyMathLib import Polynomials as poly

# 🔹 Configura tu clave de OpenAI
openai.api_key = "TU_API_KEY_AQUI"  # Reemplaza con tu clave

def explain_with_ai(operation: str,
                    p1: List[float],
                    p2: Optional[List[float]] = None,
                    x: Optional[float] = None,
                    n: Optional[int] = None,
                    candidate_root: Optional[float] = None,
                    nivel: str = "intermedio") -> str:
    """
    Aplica las funciones REALES de tu librería PyMathLib y usa IA
    para explicar los pasos y el resultado.
    """

    # 1️⃣ Ejecutar la función real de tu librería
    result = None
    raw_steps = []

    if operation == "add":
        result = poly.add(p1, p2)
        raw_steps.append(f"Suma de {p1} + {p2} = {result}")

    elif operation == "sub":
        result = poly.subtraction(p1, p2)
        raw_steps.append(f"Resta de {p1} - {p2} = {result}")

    elif operation == "mul":
        result = poly.multiplication(p1, p2)
        raw_steps.append(f"Multiplicación de {p1} × {p2} = {result}")

    elif operation == "div":
        result = poly.division(p1, p2)
        raw_steps.append(f"División de {p1} ÷ {p2} = {result}")

    elif operation == "ruffini":
        if candidate_root is None:
            raise ValueError("Falta el valor para aplicar Ruffini.")
        result = poly.Ruffini(p1, candidate_root)
        raw_steps.append(f"Ruffini con raíz candidata {candidate_root} → {result}")

    elif operation == "eval":
        if x is None:
            raise ValueError("Falta valor x para evaluar el polinomio.")
        result = poly.evaluate(p1, x)
        raw_steps.append(f"Evaluación P({x}) = {result}")

    elif operation == "pow":
        if n is None:
            raise ValueError("Falta exponente para la potenciación.")
        result = poly.Pow(p1, n)
        raw_steps.append(f"Potencia ({p1})^{n} = {result}")

    elif operation == "roots":
        result = poly.PolyRoot(p1)
        raw_steps.append(f"Raíces aproximadas de {p1}: {result}")

    else:
        raise ValueError(f"Operación no reconocida: {operation}")

    # 2️⃣ Preparamos el prompt para la IA
    prompt = f"""
Eres un profesor de matemáticas explicando paso a paso cómo se realiza
la operación '{operation}' con polinomios a un estudiante de nivel {nivel}.

Aquí tienes los datos y resultados generados por la librería PyMathLib:

Operación: {operation}
Polinomio 1: {p1}
Polinomio 2: {p2}
Valor x (si aplica): {x}
Exponente n (si aplica): {n}
Candidato Ruffini (si aplica): {candidate_root}
Resultado devuelto: {result}

Explica paso a paso lo que ocurre en el cálculo y qué significa cada número
de manera comprensible y motivadora para el estudiante.
Incluye ejemplos o analogías simples si son útiles.
"""

    # 3️⃣ Llamamos a la IA para transformar los datos en explicación didáctica
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Usa gpt-4o o gpt-5 si lo tienes disponible
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    explanation = response.choices[0].message["content"]
    return explanation
