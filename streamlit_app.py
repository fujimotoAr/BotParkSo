import streamlit as st
from streamlit_chat import message
from chatbot import RuleBot


def run_streamlit_app(chatbot):
    # Creating the chatbot interface
    st.title("BotParkSo (Bot Parking Solution)")

    # Storing the chat
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []

    def clear_input():
        st.session_state.user_input = st.session_state.input
        st.session_state.input = ''

    def get_text():
        if 'user_input' not in st.session_state:
            st.session_state.user_input = ''

        st.session_state.user_input = st.chat_input(placeholder='Ask your question')

        return st.session_state.user_input


    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            if i < len(st.session_state['generated']):

                with st.chat_message("user"):
                    st.write(st.session_state['past'][i])
                with st.chat_message("bot"):
                    st.write(st.session_state["generated"][i])



    user_input = get_text()
    if user_input:
        output = chatbot.get_response(chatbot, user_input)

        if chatbot.is_negative(chatbot, user_input):
            output = "Mohon Maaf kalau begitu, silakan berikan tanggapan lain?"
            pass

        if chatbot.is_exit(chatbot, user_input):
            output = "Okay, sama-sama"
            st.session_state.generated.clear()

            pass
        st.session_state.generated.append(output)
        st.session_state.past.append(user_input)
        with st.chat_message("user"):
            st.write(user_input)

        with st.chat_message("bot"):
            st.write(output)
run_streamlit_app(RuleBot)