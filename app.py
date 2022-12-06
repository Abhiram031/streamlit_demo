import streamlit as st
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# input signal 1
st.sidebar.subheader("Signal 1")
s1_len = st.sidebar.slider("Length", 1, 10, 5)
s1 = st.sidebar.selectbox("Type", ["Impulse", "Step", "Ramp"], key="slider1")
if s1 == "Impulse":
    s1 = np.zeros(s1_len)
    s1[0] = 1
elif s1 == "Step":
    s1 = np.ones(s1_len)
elif s1 == "Ramp":
    s1 = np.array(range(1, s1_len+1))

# input signal 2
st.sidebar.subheader("Signal 2")
s2_len = st.sidebar.slider("Length", 1,10,5,key="len2")
s2 = st.sidebar.selectbox("Type", ["Impulse", "Step", "Ramp"],key="slider2")
if s2 == "Impulse":
    s2 = np.zeros(s2_len)
    s2[0] = 1
elif s2 == "Step":
    s2 = np.ones(s2_len)
elif s2 == "Ramp":
    s2 = np.array(range(1, s2_len+1))

# convolution result
result = signal.convolve(s1, s2,)

# plot
st.subheader("Plot")
st.line_chart(result)

# show input signals
st.subheader("Input Signals")
st.line_chart(s1)
st.line_chart(s2)