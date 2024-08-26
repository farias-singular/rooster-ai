import streamlit as st
import pandas as pd
from openai import OpenAI
import os
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def load_template(filename):
    """Load the data model template from a file that is used by our backend squad"""
    try:
        with open(f"./newdocs/{filename}", "r") as file:
            content = file.read()
            st.write(f"Loaded template content from {filename}: {content[:100]}...")
            return content
    except FileNotFoundError:
        st.error(f"Template file {filename} not found.")
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


# Initialize if not already in session state
if "properties_data" not in st.session_state:
    st.session_state["properties_data"] = pd.DataFrame(columns=["Property", "Type"])
if "relations_data" not in st.session_state:
    st.session_state["relations_data"] = pd.DataFrame(
        columns=["Entity1", "Relation", "Entity2"]
    )


# Function to add a row to a dataframe
def add_row(df):
    new_row = pd.DataFrame({col: [""] for col in df.columns}, index=[len(df)])
    return pd.concat([df, new_row], ignore_index=True)


st.sidebar.title("Input Specifications")
entity = st.sidebar.text_input("Type Entity", "Entity")


language = st.sidebar.selectbox(
    "Choose programming language",
    ["C#", "Python", "Java", "JavaScript"],
    key="language_selection",
)
data_models = os.listdir("./newdocs")
data_model = st.sidebar.selectbox(
    "Choose Data Model", data_models, key="data_model_selection"
)


template_content = load_template(data_model)
st.title("Template Content")
st.text_area("Template Content", template_content, height=300)


if "properties_data" not in st.session_state:
    st.session_state["properties_data"] = pd.DataFrame(columns=["Property", "Type"])
if "relations_data" not in st.session_state:
    st.session_state["relations_data"] = pd.DataFrame(
        columns=["Entity1", "Relation", "Entity2"]
    )

st.sidebar.subheader("Properties")
for i in range(len(st.session_state["properties_data"])):
    for col in st.session_state["properties_data"].columns:
        st.session_state["properties_data"].iat[
            i, st.session_state["properties_data"].columns.get_loc(col)
        ] = st.sidebar.text_input(
            f"{col} {i}",
            value=st.session_state["properties_data"].iat[
                i, st.session_state["properties_data"].columns.get_loc(col)
            ],
        )

if st.sidebar.button("Add Property"):
    st.session_state["properties_data"] = add_row(st.session_state["properties_data"])

st.sidebar.subheader("Relations")
for i in range(len(st.session_state["relations_data"])):
    for col in st.session_state["relations_data"].columns:
        st.session_state["relations_data"].iat[
            i, st.session_state["relations_data"].columns.get_loc(col)
        ] = st.sidebar.text_input(
            f"{col} {i}",
            value=st.session_state["relations_data"].iat[
                i, st.session_state["relations_data"].columns.get_loc(col)
            ],
        )

if st.sidebar.button("Add Relation"):
    st.session_state["relations_data"] = st.session_state["relations_data"]

st.title("Language Model Output")
if st.button("Generate Code"):
    json_data = {
        "Entity": entity,
        "Properties": st.session_state["properties_data"].to_dict("records"),
        "Relations": st.session_state["relations_data"].to_dict("records"),
        "Programming Language": language,
        "Data Model": data_model,
    }

    code, success = generate_code_with_openai(template_content, json_data)

    if success:
        validated_code = validate_code_with_openai(code)
        st.success("Code generated and validated successfully!")
        st.text_area("Generated Code", validated_code, height=300)
    else:
        st.error(f"Failed to generate code: {code}")
