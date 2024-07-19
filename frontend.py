import streamlit as st
import pandas as pd
import requests
import json
import os

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


# Sidebar for input specifications and selections
st.sidebar.title("Input Specifications")
entity = st.sidebar.selectbox("Entity", ["Brands", "Products", "Users"], index=0)

# Move programming language and data model to sidebar
language = st.sidebar.selectbox(
    "Choose programming language",
    ["C#", "Python", "Java", "JavaScript"],
    key="language_selection",
)
data_models = os.listdir(
    "/home/lbeylouni/Documents/newGen/newdocs"
)  # Adjust path as needed
data_model = st.sidebar.selectbox(
    "Choose Data Model", data_models, key="data_model_selection"
)

# Editable tables for Properties and Relations
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
    st.session_state["relations_data"] = add_row(st.session_state["relations_data"])

# Button to trigger backend processing and display JSON in main panel
st.title("Language Model Output")
if st.button("Generate JSON"):
    json_data = {
        "Entity": entity,
        "Properties": st.session_state["properties_data"].to_dict("records"),
        "Relations": st.session_state["relations_data"].to_dict("records"),
        "Programming Language": language,
        "Data Model": data_model,
    }
    json_output = json.dumps(json_data, indent=4)
    st.text_area(
        "Generated code", json_output, height=300
    )  # Display JSON in main panel
    # Optionally send to backend
    response = requests.post("http://localhost:5000/process_json", json=json_data)
    if response.status_code == 200:
        st.success("JSON sent successfully!")
        st.json(response.json())  # Display the response from the backend
    else:
        st.error("Failed to send JSON")
