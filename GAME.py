import tkinter as tk
import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def lagrange_interpolation(x, y, t):
    """
    Вычисляет значение интерполяционного многочлена Лагранжа в точке t.
    """
    poly = lagrange(x, y)
    return poly(t)


def plot_interpolation(x, y):
    """
    Строит график интерполяции.
    """
    t_values = np.linspace(min(x), max(x), 1000)
    y_values = lagrange_interpolation(x, y, t_values)

    plt.plot(x, y, 'o', label='Data Points')
    plt.plot(t_values, y_values, label='Lagrange Interpolation')
    plt.xlabel('t')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


def draw_circle(x, y, canvas):
    """
    Рисует круг в окне Tkinter с использованием точек интерполяции.
    """
    for i in range(len(x)):
        canvas.create_oval(x[i] - 5, y[i] - 5, x[i] + 5, y[i] + 5, fill='blue')


def main():
    # Задаем точки для интерполяции
    x_points = np.array([1, np.sqrt(2)/2, 0, -np.sqrt(2)/2, -1, -np.sqrt(2)/2, 0, np.sqrt(2)/2, 1])
    y_points = np.array([0, np.sqrt(2)/2, 1, np.sqrt(2)/2, 0, -np.sqrt(2)/2, -1, -np.sqrt(2)/2, 0])

    # Строим график интерполяции
    plot_interpolation(x_points, y_points)

    # Создаем окно Tkinter
    root = tk.Tk()
    root.title('Interpolation Circle')

    # Создаем холст для отображения графики в окне Tkinter
    figure, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(figure, master=root)
    widget = canvas.get_tk_widget()
    widget.pack()

    # Рисуем круг на холсте
    draw_circle(x_points, y_points, canvas)

    root.mainloop()


if __name__ == "__main__":
    main()