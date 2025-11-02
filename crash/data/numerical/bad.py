# @title Setup - Install relevant modules

!pip install matplotlib~=3.10.0 \
  pandas~=2.2.0

#========================================
# @title Setup - Import relevant modules

# The following code imports relevant modules that
# enable you to run the Colab.
# If you encounter technical issues running some of the code sections
# that follow, try running this section again.

import pandas as pd
from matplotlib import pyplot as plt
import io

# The following lines adjust the granularity of reporting.
pd.options.display.max_rows = 10
pd.options.display.float_format = "{:.1f}".format

#========================================
# @title Load the dataset into a DataFrame
training_df = pd.read_csv('dataset.csv', on_bad_lines='warn')

#========================================
# Task 1: Examine basic statistics
# @title Generates basic statistics on the dataset

training_df.describe()

#========================================
#@title Define the plotting functions { display-mode: "form" }

# The following code defines the plotting functions that can be used to
# visualize the data.

def plot_the_dataset(feature, label, number_of_points_to_plot):
  """Plot N random points of the dataset."""

  # Label the axes.
  plt.xlabel(feature)
  plt.ylabel(label)

  # Create a scatter plot from n random points of the dataset.
  random_examples = training_df.sample(n=number_of_points_to_plot)
  plt.scatter(random_examples[feature], random_examples[label])

  # Render the scatter plot.
  plt.show()

def plot_a_contiguous_portion_of_dataset(feature, label, start, end):
  """Plot the data points from start to end."""

  # Label the axes.
  plt.xlabel(feature + "Day")
  plt.ylabel(label)

  # Create a scatter plot.
  plt.scatter(training_df[feature][start:end], training_df[label][start:end])

  # Render the scatter plot.
  plt.show()


print("Defined the following functions:")
print("  * plot_the_dataset")
print("  * plot_a_contiguous_portion_of_dataset")

#========================================
# Task 2: Visualize the dataset
#@title 

plot_the_dataset("calories", "test_score", number_of_points_to_plot=50)

#========================================
# @title Task 2: Solution (run this code block to view) { display-mode: "form" }

print("""Visualizing 50 data points doesn't imply any outliers.
However, as you increase the number of random data points to plot, a
clump of outliers appears. Notice the points with high test scores but less
than 200 calories.""")

#========================================
# Task 3: Get statistics for each week
#@title 

# Get statistics on Week 0
training_df[0:350].describe()

# Get statistics on Week 1
training_df[350:700].describe()

# Get statistics on Week 2
training_df[700:1050].describe()

# Get statistics on Week 3
training_df[1050:1400].describe()

#========================================
# @title Task 3: Solution (run this code block to view) { display-mode: "form" }

print("""The basic statistics for each week are pretty similar, so weekly
differences aren't a likely explanation for the outliers.""")

#========================================
# Task 4: Visualize by day of week
# @title

for i in range(0,7):
  start = i * 50
  end = start + 49
  print("\nDay %d" % i)
  plot_a_contiguous_portion_of_dataset("calories", "test_score", start, end+1)

#========================================
# @title Task 4: Solution (run this code block to view) { display-mode: "form" }

print("""Wait a second--the calories value for Day 4 spans 0 to 200, while the
calories value for all the other Days spans 0 to 400. Something is wrong
with Day 4, at least on the first week.""")

#========================================
# @title Task 5: Solution (expand this code block to view) { display-mode: "form" }

# You could use a variety of metrics to fully compare Thursday to the other
# six days, but this answer simply focuses on the mean.

running_total_of_thursday_calories = 0
running_total_of_non_thursday_calories = 0
count = 0
for week in range(0,4):
  for day in range(0,7):
    for subject in range(0,50):
      position = (week * 350) + (day * 50) + subject
      if (day == 4):  # Thursday
        running_total_of_thursday_calories += training_df['calories'][position]
      else:  # Any day except Thursday
        count += 1
        running_total_of_non_thursday_calories += training_df['calories'][position]

mean_of_thursday_calories = running_total_of_thursday_calories / 200
mean_of_non_thursday_calories = running_total_of_non_thursday_calories / 1200

print("The mean of Thursday calories is %.0f" % (mean_of_thursday_calories))
print("The mean of calories on days other than Thursday is %.0f" % (mean_of_non_thursday_calories))

