import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def simulador_SIS(M, start, time):
    log_S = [start[0]]
    log_I = [start[1]]
    pop = start
    for i in range(time -1):
        pop = np.dot(M, pop)
        log_S.append(pop[0])
        log_I.append(pop[1])
    return log_S, log_I

TIME = 100
default_inf_rate = 0.5
default_recov_rate = 0.5
pop_inicial = np.array([500, 0])

fig,ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

tm = np.array([[1 - default_inf_rate, default_inf_rate], [default_recov_rate, 1 - default_recov_rate]])
tm = tm.transpose()

t = np.linspace(0.0, TIME, TIME)
samp_S, samp_I = simulador_SIS(tm, pop_inicial, TIME)
l1, = ax.plot(t,samp_S,lw=2,label='S')
l2, = ax.plot(t,samp_I,lw=2,label='I')

ax_slider_a = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_slider_b = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_a = Slider(ax_slider_a, 'Alpha', 0.0, 1.0, valinit=default_inf_rate)
slider_b = Slider(ax_slider_b, 'Beta', 0.0, 1.0, valinit=default_recov_rate)

ax.set_title('SIS Model')
ax.set_xlabel("Time")
ax.set_ylabel("Population")
ax.legend()


def update(val):
    inf_prob = slider_a.val
    recov_prob = slider_b.val

    M = np.array([[1 - inf_prob, inf_prob], [recov_prob, 1 - recov_prob]])
    M = M.transpose()

    new_samp_S, new_samp_I = simulador_SIS(M, pop_inicial, TIME)

    l1.set_ydata(new_samp_S)
    l2.set_ydata(new_samp_I)
    fig.canvas.draw_idle()

slider_a.on_changed(update)
slider_b.on_changed(update)

plt.show()