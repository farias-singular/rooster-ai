from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_template(filename):
    """Load the data model template from a file that is used by our backend squad"""
    try:
        with open(f"/home/lbeylouni/Documents/newGen/newdocs/{filename}", "r") as file:
            content = file.read()
            print(f"Loaded template content from {filename}: {content}...")
            return content
    except FileNotFoundError:
        print(f"Template file {filename} not found.")
        return None


def generate_code_with_openai(template, data):
    """Generates code using OpenAI based on the template and JSON data inputted in the frontend"""
    rules = (
        "Você é um agente de IA especializado em desenvolvimento back-end, com proficiência em C# e JavaScript. "
        "Seu conhecimento é derivado de diversos arquivos markdown que servem como gabaritos. "
        "O conteúdo em código do arquivo markdown será fornecido pelo usuário. "
        "Você trabalha recebendo entradas em JSON, lendo as informações nelas contidas e desenvolvendo código na linguagem especificada. "
        "Sempre retorne código na linguagem especificada pelo usuário. "
        "Você irá desenvolver código baseado somente nos inputs JSON, detalhando cada especificidade necessária. "
        "Use todos os detalhes contidos nos JSON de entrada. Não ignore nenhuma informação. "
        "Toda informação advinda das entradas JSON é extremamente importante. "
        "Refira-se somente ao conteúdo provindo dos markdowns. "
        "Preste atenção em todos os detalhes do arquivo modelo selecionado para montar a sua resposta."
        "Nunca, em nenhuma circunstância, retorne textos e parágrafos em linguagem natural. "
        'Na chave "code" da resposta, jamais, nunca, de forma alguma retorne JSON. '
    )

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


def validate_code_with_openai(code):
    """Validates the generated code using OpenAI"""
    validation_prompt = (
        "Você é um especialista em revisão de código. Verifique o código a seguir em busca de erros comuns, incluindo:\n"
        "- Certifique-se que o código gerado está de acordo com o arquivo modelo selecionado\n"
        "- Erros de sintaxe\n"
        "- Tipos de dados incorretos\n"
        "- Relações ausentes ou incorretas\n"
        "- Manipulação de erros adequada\n"
        "- Conformidade com as melhores práticas para a linguagem especificada\n"
        "- Qualquer outra melhoria que possa ser feita\n\n"
        "Código:\n"
        f"{code}\n\n"
        # "Se houver erros, reescreva o código corrigido. Se não houver, apenas confirme que o código está correto."
        "Corrija o código, se necessário."
        "Retorne apenas código, jamais linguagem natural."
    )

    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": validation_prompt},
        ],
        model="gpt-4-turbo",
        max_tokens=4096,
    )
    return response.choices[0].message.content


@app.route("/process_json", methods=["POST"])
def process_json():
    data = request.json
    template_content = load_template(data["Data Model"])
    code, success = generate_code_with_openai(template_content, data)
    if success:
        validated_code = validate_code_with_openai(code)
        return jsonify(
            {
                "status": "Code generated and validated successfully",
                "code": validated_code,
            }
        )
    else:
        return jsonify({"status": "Failed to generate code", "reason": code}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)
