# =============================================================================
# PYTHON Line Plots
# =============================================================================

# DESCRIPTION
#The line plot is a fairly common plot type that is used
#to plot the trend of one numeric variable against values of a second variable.
#In contrast to a scatterplot, where all data points are plotted,
#in a line plot, only one point is plotted for every unique x-value
#or bin of x-values (like a histogram)
#
#If there are multiple observations in an x-bin,
#then the y-value of the point plotted in the line plot will be a summary stat.
#(like mean or median) of the data in the bin.
#
#The plotted points are connected with a line that emphasizes the sequential
#or connected nature of the x-values.
#
#Use of Matplotlib's errorbar function, performing some processing on the data
#in order to get it into its necessary form.
plt.errorbar(data = df, x = 'num_var1', y = 'num_var2')

