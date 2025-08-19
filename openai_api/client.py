import openai

client = openai.OpenAI(
    api_key="sk-proj-xxx")


def get_car_ai_bio(model, brand, year):
    prompt = f'''
    Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. 
    Fale coisas específicas sobre esse modelo de carro.
    '''

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "Você é um especialista em vendas de carros."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=250,
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
