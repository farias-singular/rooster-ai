from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_template(filename):
    """Load the data model template from a file."""
    try:
        with open(f"/home/lbeylouni/Documents/newGen/newdocs/{filename}", "r") as file:
            return file.read()
    except FileNotFoundError:
        return None


def generate_code_with_openai(template, data):
    """Generate code using OpenAI based on the template and JSON data."""
    rules = [
        "Você é um agente de IA especializado em desenvolvimento back-end, com proficiência em C# e JavaScript.",
        "Seu conhecimento é derivado de diversos arquivos markdown que servem como gabaritos.",
        "O arquivo markdown a ser especificado será fornecido pelo usuário.",
        "Você trabalha recebendo entradas em JSON, lendo as informações nelas contidas e desenvolvendo código na linguagem ali especificada.",
        "Sempre retorne código na linguagem especificada pelo usuário.",
        "Você irá desenvolver código baseado somente nos inputs JSON, detalhando cada especificidade necessária.",
        "Use todos os detalhes contidos nos JSON de entrada. Não ignore nenhuma informação.",
        "Toda informção advinda das entradas JSON é extremamente importante.",
        "Sempre preste muita atenção aos gabaritos, sem desviar o seu foco.",
        "Use todas as estruturas disponíveis em cada gabarito para garantir respostas completas e corretas.",
        "Nunca, em nenhuma circunstância, retorne textos e parágrafos em linguagem natural.",
        'Na chave "code" da resposta, jamais, nunca, de forma alguma retorne JSON.',
        "Você é obrigado a retornar scripts.",
    ]

    if template is None:
        return "Template not found", False
    prompt = f"{template}\n# Entity: {data['Entity']}\n"
    for prop in data["Properties"]:
        prompt += f"# Property: {prop['Property']} of type {prop['Type']}\n"
    for rel in data["Relations"]:
        prompt += f"# Relation: {rel['Entity1']} {rel['Relation']} {rel['Entity2']}\n"
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": rules,
            },
            {"role": "user", "content": prompt},
        ],
        model="gpt-4-turbo",
        max_tokens=4096,
    )
    return response.choices[0].message.content, True


@app.route("/process_json", methods=["POST"])
def process_json():
    data = request.json
    template_content = load_template(data["Data Model"])
    code, success = generate_code_with_openai(template_content, data)
    if success:
        return jsonify({"status": "Code generated successfully", "code": code})
    else:
        return jsonify({"status": "Failed to generate code", "reason": code}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)
