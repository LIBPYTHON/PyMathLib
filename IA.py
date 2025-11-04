# poly_explainer_universal.py
import os
import openai

# Importamos tus funciones ya existentes
from PyPil.Polinomials.addition import addition
from PyPil.Polinomials.subtraction import subtraction
from PyPil.Polinomials.multiplication import multiplication
from PyPil.Polinomials.division import division
from PyPil.Polinomials.ruffini import ruffini

openai.api_key = os.getenv("OPENAI_API_KEY")

def explain_polynomial_operation(operation_name, *args, model="gpt-5-mini"):
    """
    Usa las funciones ya creadas de PyPil.Polinomials para calcular el resultado,
    y genera una explicación paso a paso con ChatGPT.
    """

    # Ejecutamos la operación real según el nombre indicado
    if operation_name == "addition":
        result = addition(*args)
    elif operation_name == "subtraction":
        result = subtraction(*args)
    elif operation_name == "multiplication":
        result = multiplication(*args)
    elif operation_name == "division":
        result = division(*args)
    elif operation_name == "ruffini":
        result = ruffini(*args)
    else:
        raise ValueError(f"Operació '{operation_name}' no reconeguda.")

    # Creamos el mensaje que se enviará a ChatGPT
    prompt = (
        f"Ets un professor de matemàtiques.\n"
        f"T'explico una operació amb polinomis realitzada amb Python.\n\n"
        f"Operació: {operation_name}\n"
        f"Polinomis d'entrada: {args}\n"
        f"Resultat obtingut pel programa: {result}\n\n"
        "Ara explica pas a pas com s'arriba a aquest resultat, "
        "mostrant els càlculs intermedis i la lògica de cada pas, "
        "com si fossis un professor explicant-ho a classe."
    )

    # Llamada al model
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "Ets un professor de matemàtiques que explica pas a pas."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        max_tokens=900
    )

    explanation = response["choices"][0]["message"]["content"].strip()

    return {
        "operation": operation_name,
        "inputs": args,
        "result": result,
        "explanation": explanation
    }
