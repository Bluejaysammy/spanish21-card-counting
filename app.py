import streamlit as st
import random

# Spanish 21 Shoe (8 Decks)
DECKS = 8
TOTAL_ACES = 4 * DECKS  # 32 Aces
TOTAL_FACE_CARDS = 12 * DECKS  # 96 Face Cards (J, Q, K)

# Initialize Streamlit session state
if "remaining_aces" not in st.session_state:
    st.session_state.remaining_aces = TOTAL_ACES
    st.session_state.remaining_faces = TOTAL_FACE_CARDS
    st.session_state.round = 0

st.title("🃏 Spanish 21 Card Counting Drill: Aces & Face Cards")

# Deal next round
if st.button("Deal Next Round"):
    st.session_state.round += 1
    aces_drawn = random.randint(0, min(st.session_state.remaining_aces, 2))
    faces_drawn = random.randint(0, min(st.session_state.remaining_faces, 4))

    st.session_state.remaining_aces -= aces_drawn
    st.session_state.remaining_faces -= faces_drawn

    # Store last round data
    st.session_state.last_aces_drawn = aces_drawn
    st.session_state.last_faces_drawn = faces_drawn

# Display game info
st.write(f"### Round {st.session_state.round}")
if "last_aces_drawn" in st.session_state:
    st.write(f"- **Aces Drawn:** {st.session_state.last_aces_drawn}")
    st.write(f"- **Face Cards Drawn:** {st.session_state.last_faces_drawn}")

st.write(f"### Remaining Cards in Shoe:")
st.write(f"- **Aces Left:** {st.session_state.remaining_aces} / 32")
st.write(f"- **Face Cards Left:** {st.session_state.remaining_faces} / 96")

# User Input for Counting
user_aces_guess = st.number_input("Enter your guess for remaining Aces:", min_value=0, max_value=32, step=1)
user_faces_guess = st.number_input("Enter your guess for remaining Face Cards:", min_value=0, max_value=96, step=1)

# Check Accuracy
if st.button("Check My Count"):
    ace_accuracy = abs(user_aces_guess - st.session_state.remaining_aces)
    face_accuracy = abs(user_faces_guess - st.session_state.remaining_faces)

    st.write("### 🎯 Results:")
    st.write(f"- Your **Ace Count** was **{'accurate' if ace_accuracy == 0 else f'off by {ace_accuracy}'}**.")
    st.write(f"- Your **Face Card Count** was **{'accurate' if face_accuracy == 0 else f'off by {face_accuracy}'}**.")

    # Betting Advice
    if st.session_state.remaining_aces > TOTAL_ACES * 0.5 and st.session_state.remaining_faces > TOTAL_FACE_CARDS * 0.5:
        st.success("🟢 Betting Advice: **Increase Bet** – High chance of strong hands & blackjacks.")
    elif st.session_state.remaining_aces < TOTAL_ACES * 0.3 or st.session_state.remaining_faces < TOTAL_FACE_CARDS * 0.3:
        st.error("🔴 Betting Advice: **Lower Bet** – Deck is running low on high-value cards.")
    else:
        st.info("🔵 Betting Advice: **Play Normal** – Balanced deck.")

"Initial commit - Spanish 21 Counting Drill"
