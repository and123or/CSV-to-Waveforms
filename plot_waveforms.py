import read_data as redata
import matplotlib.pyplot as plt

def plot_waveforms(data):
    """  
    Plot the waveforms using matplotlib.  
    """
    if data is None:
        print("No data to plot")
        return

    time = data['second'].astype(float) * 1000000  # Convert seconds to microseconds
    plt.figure(figsize=(10, 6))

    colors = ["#eaea00", "#30f600", "#5274f7", "#f2007d"]
    for i, col in enumerate(data.columns[1:]):  # Skip the 'second' column
        plt.plot(time, data[col], colors[i % len(colors)], label=col)

    plt.xlabel('Time (us)')
    plt.ylabel('Amplitude (V)')
    plt.title('Waveforms')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
if __name__ == "__main__":
    data = redata.read_and_modify_csv_file()
    plot_waveforms(data)
