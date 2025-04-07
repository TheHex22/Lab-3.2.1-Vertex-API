import os
import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig

from dotenv import load_dotenv

load_dotenv()

vertexai.init(project=os.environ.get("hmoreno7techx25"), location="us-central1")

st.title("Find your neighboring states")

users_state = st.text_input("Enter your state")


# Section A: Add in your Vertex AI API call below

model = GenerativeModel("gemini-1.5-flash-002" , system_instruction = f"Only include US states in your response. if {users_state} is not one of the 50 United States states do not respond.  (give answer in bullet points)")

response = model.generate_content(
    f"what are all neighboring states of {users_state}?",
    generation_config={
        "temperature": 0.2,
        "max_output_tokens": 50,
    }
)

# End of Section A


st.write("The neighboring states are:")


# Section B:  Output the results to the user below
st.write(response.text)

# End of Section B
