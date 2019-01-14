import matplotlib.pyplot as plt


def plot_trace(trace, enlarge=False, xlim=None, savedir=None):
    start_time = trace.stats.starttime
    pick_time = trace.picks[0].time - start_time
    pick_phase = trace.picks[0].phase_hint
    time_stamp = start_time.isoformat()

    subplot = 2
    fig = plt.figure(figsize=(8, subplot * 2))

    ax = fig.add_subplot(subplot, 1, 1)
    plt.title(time_stamp + " " + trace.id)
    if enlarge:
        if xlim:
            plt.xlim(xlim)
        else:
            plt.xlim((pick_time - 1, pick_time + 2))
    ax.plot(trace.times(reftime=start_time), trace.data, "k-", label=trace.id)
    y_min, y_max = ax.get_ylim()
    ax.vlines(pick_time, y_min, y_max, color='r', lw=2, label=pick_phase)
    ax.legend()

    ax = fig.add_subplot(subplot, 1, subplot)
    ax.plot(trace.times(reftime=start_time), trace.picks[0].pdf, "b-", label=pick_phase + " pdf")
    if enlarge:
        if xlim:
            plt.xlim(xlim)
        else:
            plt.xlim((pick_time - 1, pick_time + 2))
    plt.ylim((-0.1, 1.1))
    ax.legend()

    if savedir:
        plt.savefig(savedir + "/" + time_stamp + "_" + trace.id + ".pdf")
        plt.close()
    else:
        plt.show()
