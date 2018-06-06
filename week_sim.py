import numpy as np
import matplotlib.pyplot as plt

def week_simulate(means, vars, weeks):
    week_data = np.empty([7, weeks])
    for i in range(7):
        week_data[i] = np.random.normal(means[i], vars[i], weeks)
    return week_data


def resample(week_data, weeks):
    size_new = int(7*weeks/3)
    data_3day = np.ones([size_new*3])
    for i in range(size_new):
        ii = i*3
        average = (week_data[ii] + week_data[ii+1] + week_data[ii+2])/3
        #print(ii, week_data[ii], week_data[ii+1] , week_data[ii+2], average)
        data_3day[ii] = average
        data_3day[ii+1] = average
        data_3day[ii+2] = average
    # compute mean of each day in a week
    mean_3day = np.zeros([7])
    mean_count = np.zeros([7])
    for i in range(7):
        for j in range(size_new):
            if (i+j*7 < len(data_3day)):
                mean_3day[i] += data_3day[i+j*7]
                mean_count[i] += 1
            else:
                break
    mean_3day /= mean_count
    return data_3day, mean_3day


if __name__ == "__main__":
    # set print format
    float_formatter = lambda x: "%.3f" % x
    np.set_printoptions(formatter={'float_kind': float_formatter})
    num_weeks = 100

    means = np.asarray([35.5123, 44.3578, 48.0436, 43.5154, 34.7159, 28.6967, 29.7039])
    variance = np.asarray([1]*7)
    week_data = week_simulate(means, variance, num_weeks)
    # compute mean of each day in a week
    mean_original = np.mean(week_data, axis=1)
    print("Sample mean for each day in a week: \n\t", mean_original)
    # flatten (2d -> 1d): from [7, weeks] to [7*weeks]
    week_data = week_data.flatten('F')
    # re-sample, 3 continues days
    print("Re-sample data by a group of 3 continues days....")

    data_3day, mean_3day = resample(week_data, num_weeks)
    print("Original means: \n\t", mean_original)
    print("Resampled means: \n\t", mean_3day)

    # draw
    plt.plot(range(7), mean_original, '-o')
    plt.plot(range(7), mean_3day, '-o')
    plt.legend(['original', '3day re-sample'])
    plt.show()

    print(variance)