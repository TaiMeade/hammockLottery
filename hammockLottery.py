import streamlit as st
import random
import time

numPeople = [2, 3]
weights = [4, 1]

numSelections = random.choices(numPeople, weights=weights, k=1)[0]

fullList = ['Rose', 'RaeDawn', 'Raena', 'Christina', 'Lily S', 'Veda', 'Zoe', 'Kim', 'Emily', 'Alexia', 'Dakota', 'Lily H', 'Raiden', 'Logan', 'Matthew', 'Andrew', 'Cary', 'Gavin']

st.title("Hammock Lottery")

if st.button("Generate"):

    st.write(f"{numSelections} people have been selected!")
    st.write("---")

    selections = random.sample(fullList, numSelections)

    # Select a third if needed
    if numSelections > 2:
        st.write("Congratulations to...")
        time.sleep(1.5)
        st.write(selections[2])
    else: 
        st.write("Congratulations to...")
    time.sleep(1.5)
    st.write(selections[0])

    time.sleep(1.5)
    st.write(selections[1])
    
    time.sleep(1.5)
    st.write("Enjoy your hammocking together!")
    st.balloons()