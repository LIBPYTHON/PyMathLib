# poly_teacher.py
import os
import openai

# Posa la teva clau d'API a la variable d'entorn OPENAI_API_KEY
# o substitueix directament aquí (no recomanat per seguretat).
openai.api_key = os.getenv("OPENAI_API_KEY")

def pretty_polynomial(p):
    if isinstance(p, str):
        return p
    # suposem llista de coeficients de major a menor grau
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
        "T'explico el següent problema i la seva solució. "
        "Ara, explica PAS A PAS com arribar a la solució, com si fossis un professor: "
        "\n\nPolinomi: " + poly_text +
        "\nSolució donada: " + str(solution) +
        "\n\nInstruccions clares per al model:\n"
        " - Dona tots els passos numèrics i algebraics necessaris.\n"
        " - Mostra càlculs intermedis (operacions amb coeficients, divisions, multiplicacions, etc.).\n"
        " - Assegura't que la seqüència de passos condueix exactament a la solució donada.\n"
        " - Evita explicar conceptes innecessaris; centra't en el procediment per arribar a la solució.\n"
        "\nResposta en text pla, pas a pas:"
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

    # Extraiem el text retornat pel model
    text = response["choices"][0]["message"]["content"].strip()
    return text
