import streamlit as st

# giving this thing a title - can only have one of these
st.title("welcome to the little project")

# providing more context
st.write("this is the prototype little project")


# premade grid making fn
def make_grid(cols, rows):
    grid = [0] * cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid


# sidebar for the image
with st.sidebar:
    st.image('https://www.qtraxweb.com/p/67974-331778-us/AR/50220337_85894922.JPG')

# header for plano-gram
st.header('Plano-gram')

# making the grid
mygrid = make_grid(3, 8)

# position 0,0
mygrid[0][0].write('Duracell 10pk')

position00 = st.selectbox(
    'select product in 00',
    ('Duracell 10pk', 'Energizer 10pk'))

# position 0,1
mygrid[0][1].write('Duracell 4pk')

position01 = st.selectbox(
    'select product in 00',
    ('Duracell 4pk', 'Energizer 4pk'))
