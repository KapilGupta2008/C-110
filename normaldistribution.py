import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
result=[]

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result.append(dice1 + dice2)


#calculating mean
mean = sum(result)/len(result)
print("Mean of the data is: {}".format(mean))


#calculating mode
mode = statistics.mode(result)
print("Mode of the data is: {}".format(mode))

#calculating median
median = statistics.median(result)
print("Median of the data is: {}".format(median))

std_deviation = statistics.stdev(result)
print("standard deviation of the data is: {}".format(std_deviation))
 
#levels od stdev
first_std_deviation_start , first_std_deviation_end = mean-std_deviation, mean+std_deviation
print("first standard deviation of the data is: {}".format(first_std_deviation_start))
print("first standard deviation of the data is: {}".format(first_std_deviation_end))

second_std_deviation_start , second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
print("second standard deviation of the data is: {}".format(second_std_deviation_start))
print("second standard deviation of the data is: {}".format(second_std_deviation_end))

third_std_deviation_start , third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
print("third standard deviation of the data is: {}".format(third_std_deviation_start))
print("third standard deviation of the data is: {}".format(third_std_deviation_end))


#checking the number of data members in a particular range

list_of_data_within_1_std_deviation = [total for total in result if total >first_std_deviation_start and total< first_std_deviation_end]
a= len(list_of_data_within_1_std_deviation) * 100.0 / len(result)
print("Percent of data members lie in 1 std dev is: {}%".format(a))

list_of_data_within_2_std_deviation = [total for total in result if total >second_std_deviation_start and total< second_std_deviation_end]
b= len(list_of_data_within_2_std_deviation) * 100.0 / len(result)
print("Percent of data members lie in 2 std dev is: {}%".format(b))

list_of_data_within_3_std_deviation = [total for total in result if total >third_std_deviation_start and total< third_std_deviation_end]
c= len(list_of_data_within_3_std_deviation) * 100.0 / len(result)
print("Percent of data members lie in 3 std dev is: {}%".format(c))


#plotting the graph

fig= ff.create_distplot([result],["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()