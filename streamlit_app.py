import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮", layout="centered")

st.title("Tic Tac Toe")

# Initialize board state
if "board" not in st.session_state:
    st.session_state.board = chess.Board()

board = st.session_state.board

# Render board as SVG
board_svg = chess.svg.board(board=board, size=400)
components.html(board_svg, height=500)

# Move input
st.subheader("Make a move (UCI notation, e.g. e2e4):")
move_input = st.text_input("Enter your move:")

# Process move
if move_input:
    try:
        move = chess.Move.from_uci(move_input.strip())
        if move in board.legal_moves:
            board.push(move)
            st.success(f"Move played: {move_input}")
        else:
            st.error("Illegal move!")
    except ValueError:
        st.error("Invalid input format. Use UCI notation (like e2e4).")

# Game state messages
if board.is_checkmate():
    st.warning("Checkmate! Game over.")
elif board.is_stalemate():
    st.info("Stalemate.")
elif board.is_insufficient_material():
    st.info("Draw due to insufficient material.")
elif board.is_check():
    st.warning("Check!")

# Restart button
if st.button("Restart Game"):
    st.session_state.board = chess.Board()
    st.experimental_rerun()
