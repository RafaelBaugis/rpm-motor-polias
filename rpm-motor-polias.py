import tkinter as tk

def calculate():
    f = float(frequency_entry.get())
    p = int(poles_entry.get())
    d1 = float(d1_entry.get())
    d2 = float(d2_entry.get())
    ns = (120 * f) / p
    d2_result.set((ns * d1) / d2)
    ns_result.set(ns)

root = tk.Tk()
root.title("Cálculo de Velocidade de Motor Trifásico")

frequency_label = tk.Label(root, text="Frequência (Hz):")
frequency_label.grid(row=0, column=0)

frequency_entry = tk.Entry(root)
frequency_entry.grid(row=0, column=1)

poles_label = tk.Label(root, text="Número de polos do motor:")
poles_label.grid(row=1, column=0)

poles_entry = tk.Entry(root)
poles_entry.grid(row=1, column=1)

d1_label = tk.Label(root, text="Diâmetro da polia do motor (mm):")
d1_label.grid(row=2, column=0)

d1_entry = tk.Entry(root)
d1_entry.grid(row=2, column=1)

d2_label = tk.Label(root, text="Diâmetro da segunda polia (mm):")
d2_label.grid(row=4, column=0)

d2_entry = tk.Entry(root)
d2_entry.grid(row=4, column=1)

calculate_button = tk.Button(root, text="Calcular", command=calculate)
calculate_button.grid(row=5, columnspan=2)

ns_result_label = tk.Label(root, text="Velocidade da primeira polia (RPM):")
ns_result_label.grid(row=6, column=0)

ns_result = tk.DoubleVar()
ns_result.set(0.0)
ns_result_label_value = tk.Label(root, textvariable=ns_result)
ns_result_label_value.grid(row=6, column=1)

d2_result_label = tk.Label(root, text="Velocidade da segunda polia (RPM):")
d2_result_label.grid(row=7, column=0)

d2_result = tk.DoubleVar()
d2_result.set(0.0)
d2_result_label_value = tk.Label(root, textvariable=d2_result)
d2_result_label_value.grid(row=7, column=1)

root.mainloop()