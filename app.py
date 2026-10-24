import streamlit as st
from pathlib import Path
HISTORY_FILE=Path("history.txt")

st.set_page_config(
    page_title="Smart Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Smart Calculator")
st.caption("A simple web app built with Python")

with st.sidebar:
    st.title("About")
    st.write("Welcome to my calculator!")
    st.write("Built with Python and Streamlit.")
    st.divider()
    st.write("Features:")
    st.write("- Addition")
    st.write("- Subtraction")
    st.write("- Multiplication")
    st.write("- Division")

if "history" not in st.session_state:
    if HISTORY_FILE.exists():
        st.session_state.history = (
HISTORY_FILE.read_text(encoding="utf-8").splitlines()
        )
    else:
        st.session_state.history = []
st.subheader("Enter your numbers")

col1, col2 = st.columns(2)

with col1:
    number1 = st.number_input(
        "First number",
        value=0.0
    )

with col2:
    number2 = st.number_input(
        "Second number",
        value=0.0
    )

operation = st.selectbox(
    "Choose an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate", type="primary", use_container_width=True):
    if operation == "Addition":
        answer = number1 + number2
    elif operation == "Subtraction":
        answer = number1 - number2
    elif operation == "Multiplication":
        answer = number1 * number2
    else:
        if number2 == 0:
            st.error("You cannot divide by zero!")
            st.stop()
        answer = number1 / number2

    st.success(f"Answer: {answer}")

    entry = f"{number1} {operation} {number2} = {answer}"

    st.session_state.history.insert(0, entry)

    HISTORY_FILE.write_text(
        "\n".join(st.session_state.history) + "\n",
        encoding="utf-8"
    )

st.divider()
st.subheader("📜 Calculation History")

if st.session_state.history:
    for item in st.session_state.history:
        st.write(item)

    if st.button("Clear History"):
        st.session_state.history = []
        HISTORY_FILE.write_text("",encoding="utf-8")
        st.rerun()
else:
    st.info("No calculations yet. Try your first calculation!")