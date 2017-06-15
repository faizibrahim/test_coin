from __future__ import print_function
from CurrencyData import CurrencyData
import matplotlib.pyplot as plt

# trying a small change

def main():
    ethereum = CurrencyData()
    data = ethereum.get_data("06/10/2017-20:00:00","06/10/2017-23:00:00")

    #data = ethereum.get_data_for_last_hour()

    print(data)
    x,y = zip(*data)
    plt.plot(x,y)
    plt.show()


if __name__ == "__main__":
    main()