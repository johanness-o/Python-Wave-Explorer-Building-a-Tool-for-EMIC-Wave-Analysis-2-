# Creating multiple subplots using plt.subplots
import matplotlib.pyplot as plt
import numpy as np

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# A figure with just one subplot
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('A single plot')

# Stacking subplots in one direction
fig, axs = plt.subplots(4)
fig.suptitle('Vertically Stacked Subplots')
axs[0].plot(x, y)
axs[1].plot(x, -y)
axs [2].plot(-x, y)
axs [3].plot(-x, -y)

#     #  we can use ax1 instead of the more verbose axs[0].
# fig, (ax1, ax2) = plt.subplots(2)
# fig.suptitle('Vertically stacked subplots')
# ax1.plot(x, y)
# ax2.plot(x, -y)
#
#     # To obtain side-by-side subplots, pass parameters 1, 2 for one row and two columns.
# fig, (ax1, ax2) = plt.subplots(1, 2)
# fig.suptitle('Horizontally stacked subplots')
# ax1.plot(x, y)
# ax2.plot(x, -y)
#
#
# # Stacking subplots in two directions
# fig, axs = plt.subplots(2, 2)
# axs[0, 0].plot(x, y)
# axs[0, 0].set_title('Axis [0, 0]')
# axs[0, 1].plot(x, y, 'tab:orange')
# axs[0, 1].set_title('Axis [0, 1]')
# axs[1, 0].plot(x, -y, 'tab:green')
# axs[1, 0].set_title('Axis [1, 0]')
# axs[1, 1].plot(x, -y, 'tab:red')
# axs[1, 1].set_title('Axis [1, 1]')
#
# for ax in axs.flat:
#     ax.set(xlabel='x-label', ylabel='y-label')
#
# # Hide x labels and tick labels for top plots and y ticks for right plots.
# for ax in axs.flat:
#     ax.label_outer()
#
#     # You can use tuple-unpacking also in 2D to assign all subplots to dedicated variables:
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
# fig.suptitle('Sharing x per column, y per row')
# ax1.plot(x, y)
# ax2.plot(x, y**2, 'tab:purple')
# ax3.plot(x, -y, 'tab:pink')
# ax4.plot(x, -y**2, 'tab:cyan')
#
# for ax in fig.get_axes():
#     ax.label_outer()
#
#
# # Sharing axes
# fig, (ax1, ax2) = plt.subplots(2)
# fig.suptitle('Axes values are scaled individually by default')
# ax1.plot(x, y)
# ax2.plot(x + 1, -y)
#
#     # You can use sharex or sharey to align the horizontal or vertical axis
# fig, (ax1, ax2) = plt.subplots(2, sharex = True)
# fig.suptitle('Aligning x-axis using sharex')
# ax1.plot(x, y)
# ax2.plot(x + 1, -y)
#
#     # Setting sharex or sharey to True enables global sharing across the whole grid, i.e. also the y-axes of vertically stacked subplots have the same scale when using sharey=True.
# fig, axs = plt.subplots(3, sharex = True, sharey = True)
# fig.suptitle('Sharing both axes')
# axs[0].plot(x, y ** 2)
# axs[1].plot(x, 0.3 * y, 'o')
# axs[2].plot(x, y, '+')
#
# # To precisely control the positioning of the subplots, one can explicitly create a GridSpec with Figure.add_gridspec, and then call its subplots method. For example, we can reduce the height between vertical subplots using add_gridspec(hspace=0).
# #
# # label_outer is a handy method to remove labels and ticks from subplots that are not at the edge of the grid.
# fig = plt.figure()
# gs = fig.add_gridspec(3, hspace=0)
# axs = gs.subplots(sharex=True, sharey=True)
# fig.suptitle('Sharing both axes')
# axs[0].plot(x, y ** 2)
# axs[1].plot(x, 0.3 * y, 'o')
# axs[2].plot(x, y, '+')
#
# # Hide x labels and tick labels for all but bottom plot.
# for ax in axs:
#     ax.label_outer()
#
#     # Apart from True and False, both sharex and sharey accept the values 'row' and 'col' to share the values only per row or column.
# fig = plt.figure()
# gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
# (ax1, ax2), (ax3, ax4) = gs.subplots(sharex='col', sharey='row')
# fig.suptitle('Sharing x per column, y per row')
# ax1.plot(x, y)
# ax2.plot(x, y**2, 'tab:orange')
# ax3.plot(x + 1, -y, 'tab:green')
# ax4.plot(x + 2, -y**2, 'tab:red')
#
# for ax in axs.flat:
#     ax.label_outer()
#
# # Polar Axis
# fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw=dict(projection='polar'))
# ax1.plot(x, y)
# ax2.plot(x, y ** 2)

plt.show()