import streamlit as st
# st.write("Hello world")
import numpy as np
import matplotlib.pyplot as plt
st.title('Ilustrating Central Limit Theorem with Streamlit')
st.subheader('An App by Joel Orellana.')
st.write(('This app simulates a thousand coin flips using the chance of heads input below, ',
    'and then displays a histogram of the resulting means.',
    'The mean and standard deviation are calculated using the Central Limit Theorem.'))
perc_heads = st.number_input(label='Chance of Coins Landing on Heads: ', min_value=0.0, max_value=1.0, value=0.5)
graph_title = st.text_input(label='Title of Graph: ', value='Coin Flip Graph')
binom_dist = np.random.binomial(1, perc_heads, 1000)
list_of_means = []
for i in range(1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())
fig1, ax1 = plt.subplots()
ax1 = plt.hist(list_of_means, range=[0,1])
plt.title(graph_title)
st.pyplot(fig1)
# fig2, ax2 = plt.subplots()
# ax2 = plt.hist([1,1,1,1])
# st.pyplot(fig2)