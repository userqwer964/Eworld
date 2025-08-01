#
from mean_var_std import calculate

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
#



#
from demographic_data_analyzer import calculate_demographic_data

calculate_demographic_data()
#



#
from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

fig1 = draw_cat_plot()
fig1.savefig('catplot.png')

fig2 = draw_heat_map()
fig2.savefig('heatmap.png')

plt.show()
#


#
import time_series_visualizer as ts

ts.draw_line_plot()
ts.draw_bar_plot()
ts.draw_box_plot()

#