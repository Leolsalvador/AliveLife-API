import openai
from api.settings import OPENAI_API_KEY


def diagnosisControl(chunk, patient):
    openai.api_key = OPENAI_API_KEY

    prompt = f"""```

    Você é uma inteligência artificial feita para analisar exames médicos, ou seja, baseado no exame abaixo, você precisa gerar um pré-diagnóstico.
    Traga um resultado com números do exame.

    Abaixo é um exemplo de diagnóstico, traga com a mesma estrutura, baseado no documento enviado
    
    Resultados do Exame:
    Hemoglobina (Hb): 12,5 g/dL (Valores de referência: 13,8 - 17,2 g/dL)
    Hematócrito (Htc): 37% (Valores de referência: 40 - 52%)
    Eritrócitos (RBC): 4,2 milhões/mm³ (Valores de referência: 4,7 - 6,1 milhões/mm³)
    Volume Corpuscular Médio (VCM): 81 fL (Valores de referência: 80 - 100 fL)
    Hemoglobina Corpuscular Média (HCM): 29 pg (Valores de referência: 27 - 31 pg)
    Concentração de Hemoglobina Corpuscular Média (CHCM): 35 g/dL (Valores de referência: 32 - 36 g/dL)
    Leucócitos (WBC): 10,500 /mm³ (Valores de referência: 4,500 - 11,000 /mm³)
    Neutrófilos: 50% (Valores de referência: 40 - 60%)
    Linfócitos: 50% (Valores de referência: 20 - 40%)
    Monócitos: 6% (Valores de referência: 2 - 8%)
    Eosinófilos: 3% (Valores de referência: 1 - 4%)
    Basófilos: 1% (Valores de referência: 0,5 - 1%)
    Plaquetas: 175,000 /mm³ (Valores de referência: 150,000 - 400,000 /mm³)

    Interpretação dos Resultados:
    1. Hemoglobina e Hematócrito: Ambos estão ligeiramente abaixo do valor de referência, o que pode indicar uma leve anemia. A diabetes pode contribuir para a anemia devido a complicações renais ou deficiências nutricionais comuns em pacientes diabéticos.
    2. Eritrócitos: O nível de eritrócitos está um pouco abaixo do normal, corroborando a presença de anemia leve.
    3. Leucócitos: O nível de leucócitos está no limite superior do valor de referência. Isso pode ser um sintoma de uma infecção ou inflamação, condizente com a possível presença de diabetes.
    4. Plaquetas: O nível de plaquetas está no limite inferior do valor de referência. A trombocitopenia leve pode estar relacionada a complicações diabéticas ou ao uso de certos medicamentos.

    Considerações Finais:
    Os resultados indicam a necessidade de monitoramento contínuo dos níveis hematológicos da paciente, especificamente em relação à anemia e à função imunológica. Recomendamos que Jane Ramos siga rigorosamente a terapia hematológica prescrita para diabetes e mantenha uma dieta balanceada rica em nutrientes essenciais. A consulta com um hematologista pode ser indicada para avaliar as causas subjacentes da anemia e qualquer outra condição associada.

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