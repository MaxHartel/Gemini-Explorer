import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = "gemini-explorer-425322"
vertexai.init(project = project)

config = generative_models.GenerationConfig(
    temperature=0.4
)

#Load Model With Config
model = GenerativeModel(
    "gemini-pro",
    generation_config = config
)
chat = model.start_chat()

#helper function to display and send streamlit messeges
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    with st.chat_message("model"):
        st.markdown(output)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )


st.title("Gemini Explorer")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display and load to chat history
for index, message in enumerate(st.session_state.messages):
    content = Content(
        role = message["role"],
        parts = [ Part.from_text(message["content"])]
    )

    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    chat.history.append(content)

# Input field to capture user's name
user_name = st.text_input("Enter your name")


#Check for initial message and display introduction
if len(st.session_state.messages) == 0:
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You are a second grade substitute teacher that has clearly lost control of her classroom, you are kind hearted but also clueless, the user is your star student and their name is " + user_name
    llm_function(chat, initial_prompt)

# For capture user input
query = st.chat_input("Gemini Explorer")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)


# user_input = "Hello Gemini!"
# response = chat.send_message(user_input)
# #print("Gemini: " + str(response))

# st.write("Gemini: " + response.text)