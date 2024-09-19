import openai
from api.settings import OPENAI_API_KEY


def diagnosisControl(chunk, patient):
    openai.api_key = OPENAI_API_KEY

    prompt = f"""```

    Você é uma inteligência artificial feita para analisar exames médicos, ou seja, baseado no exame abaixo, você precisa gerar um pré-diagnóstico.
    Traga um resultado com números do exame.

    {chunk}

    Paciente: {patient}
    ```"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=500,
        temperature=0.5,
    )

    return response["choices"][0]["message"]["content"].strip()