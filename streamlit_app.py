import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮", layout="centered")

st.title("Tic Tac Toe")

# Initialize board state
if "board" not in st.session_state:
    st.session_state.board = [""] * 9
if "player" not in st.session_state:
    st.session_state.player = "X"
if "winner" not in st.session_state:
    st.session_state.winner = None

def check_winner(board):
    combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in combos:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# Draw the board buttons
cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        if st.button(st.session_state.board[i] or " ", key=i, use_container_width=True):
            if not st.session_state.board[i] and not st.session_state.winner:
                st.session_state.board[i] = st.session_state.player
                winner = check_winner(st.session_state.board)
                if winner:
                    st.session_state.winner = winner
                else:
                    st.session_state.player = "O" if st.session_state.player == "X" else "X"

st.divider()

# Display status
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.info("It's a draw!")
    else:
        st.success(f"Player {st.session_state.winner} wins!")
else:
    st.write(f"Current turn: {st.session_state.player}")

# Restart button (no experimental functions)
if st.button("Restart Game"):
    for key in ["board", "player", "winner"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()  # new, stable rerun command
