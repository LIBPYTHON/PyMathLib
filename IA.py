# poly_teacher.py
import os
import openai
from functools import wraps

openai.api_key = os.getenv("OPENAI_API_KEY")

def pretty_polynomial(p):
    if isinstance(p, str):
        return p
    if isinstance(p, (list, tuple)):
        terms = []
        deg = len(p) - 1
        for i, c in enumerate(p):
            if c == 0:
                deg -= 1
                continue
            power = deg - i
            coeff = str(c)
            if power == 0:
                terms.append(f"{coeff}")
            elif power == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{power}")
        return " + ".join(terms) if terms else "0"
    return str(p)

def explain_polynomial_step_by_step(polynomial, solution, model="gpt-5-mini", temperature=0.0, max_tokens=800):
    poly_text = pretty_polynomial(polynomial)
    prompt = (
        "Ets un professor de matemàtiques. "
        "Et dono un polinomi i la seva solució. "
        "Explica PAS A PAS com arribar-hi, com si fossis un professor amb estudiants."
        "\n\nPolinomi: " + poly_text +
        "\nSolució donada: " + str(solution) +
        "\n\nInstruccions:\n"
        " - Dona tots els càlculs intermedis.\n"
        " - Mostra operacions amb coeficients i desenvolupament algebraic.\n"
        " - Cada pas ha de conduir exactament al resultat final.\n"
        " - Explica amb claredat, com en una classe.\n"
        "\nResposta en text pla:"
    )

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "Ets un professor de matemàtiques que explica pas a pas."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response["choices"][0]["message"]["content"].strip()

def auto_explain_polynomial(func):
    """Decorador universal: aplica explicació pas a pas a qualsevol funció de polinomis"""
    @wraps(func)
    def wrapper(*args, explain=True, **kwargs):
        result = func(*args, **kwargs)
        if explain:
            try:
                polynomial_text = f"Operació: {func.__name__}, Paràmetres: {args} {kwargs}"
                explanation = explain_polynomial_step_by_step(polynomial_text, result)
                return {"result": result, "explanation": explanation}
            except Exception as e:
                return {"result": result, "explanation": f"No s'ha pogut generar explicació: {e}"}
        return {"result": result}
    return wrapper
