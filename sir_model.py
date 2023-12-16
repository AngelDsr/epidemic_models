import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def simulador_SIR(M, start, time):
    log_S = [start[0]]
    log_I = [start[1]]
    log_R = [start[2]]
    pop = start
    for i in range(time -1):
        pop = np.dot(M, pop)
        log_S.append(pop[0])
        log_I.append(pop[1])
        log_R.append(pop[2])
    return log_S, log_I, log_R

TIME = 50
default_alpha = 0.5
default_beta = 0.5
pop_inicial = np.array([1000, 0, 0])

fig,ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

trans_matrix = np.array([[1 - default_alpha, default_alpha, 0], [0, 1 - default_beta, default_beta], [0, 0, 1]])
trans_matrix = trans_matrix.transpose()

t = np.linspace(0.0, TIME, TIME)
samp_S, samp_I, samp_R = simulador_SIR(trans_matrix, pop_inicial, TIME)
l1, = ax.plot(t,samp_S,lw=2,label='S')
l2, = ax.plot(t,samp_I,lw=2,label='I')
l3, = ax.plot(t,samp_R,lw=2,label='R')


ax_slider_a = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_slider_b = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_a = Slider(ax_slider_a, 'Alpha', 0.0, 1.0, valinit=default_alpha)
slider_b = Slider(ax_slider_b, 'Beta', 0.0, 1.0, valinit=default_beta)

ax.set_title('SIR Model')
ax.set_xlabel("Time")
ax.set_ylabel("Population")
ax.legend()


def update(val):
    alpha = slider_a.val
    beta = slider_b.val

    M = np.array([[1 - alpha, alpha, 0], [0, 1 - beta, beta], [0, 0, 1]])
    M = M.transpose()

    new_samp_S, new_samp_I, new_samp_R = simulador_SIR(M, pop_inicial, TIME)

    l1.set_ydata(new_samp_S)
    l2.set_ydata(new_samp_I)
    l3.set_ydata(new_samp_R)
    fig.canvas.draw_idle()

slider_a.on_changed(update)
slider_b.on_changed(update)

plt.show()