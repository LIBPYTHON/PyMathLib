import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import json, random

# Importar la teva llibreria (ajusta noms/mòduls si cal)
from PyMathLib.Polinomials import (
    PolyAddition,
    PolySubtraction,
    PolyMultiplication,
    PolyDivision,
    PolyRoot,
    PolyPow
)
from PyMathLib.Statistics import stats_summary  # per exemple
from PyMathLib.Equations import solve_quadratic    # per exemple

def parse_coeffs(text):
    parts = [p.strip() for p in text.replace(';', ',').replace('|', ',').split(',') if p.strip()]
    coeffs = [float(p) for p in parts]
    return coeffs

def poly_to_str(poly):
    deg = len(poly)-1
    terms = []
    for i,c in enumerate(poly):
        power = deg - i
        if abs(c) < 1e-12:
            continue
        coef = f"{c:.6g}"
        if power==0:
            terms.append(f"{coef}")
        elif power==1:
            terms.append(f"{coef}x")
        else:
            terms.append(f"{coef}x^{power}")
    return " + ".join(terms).replace("+ -", "- ") if terms else "0"

class PyMathApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyMathLib - App (versió real)")
        self.geometry("900x650")
        self.create_widgets()

    def create_widgets(self):
        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True)

        # Polinomis
        tab_poly = ttk.Frame(nb)
        nb.add(tab_poly, text="Polinomis")
        pnl = ttk.Frame(tab_poly, padding=10)
        pnl.pack(fill="both", expand=True)
        ttk.Label(pnl, text="Polinomi A (coeficients separats per coma):").grid(row=0, column=0, sticky="w")
        self.polyA_entry = ttk.Entry(pnl, width=60)
        self.polyA_entry.grid(row=0, column=1, sticky="w")
        ttk.Label(pnl, text="Polinomi B:").grid(row=1, column=0, sticky="w")
        self.polyB_entry = ttk.Entry(pnl, width=60)
        self.polyB_entry.grid(row=1, column=1, sticky="w")

        btns = ttk.Frame(pnl)
        btns.grid(row=2, column=0, columnspan=2, pady=8)
        ops = [("A+B", self.do_add),
               ("A-B", self.do_sub),
               ("A*B", self.do_mul),
               ("A/B (quot, residu)", self.do_div),
               ("A^n", self.do_pow),
               ("Arrels A", self.do_roots)]
        for i,(lab,cmd) in enumerate(ops):
            ttk.Button(btns, text=lab, command=cmd).grid(row=0, column=i, padx=4)

        self.poly_output = scrolledtext.ScrolledText(pnl, height=18)
        self.poly_output.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=6)
        pnl.rowconfigure(3, weight=1)
        pnl.columnconfigure(1, weight=1)

        # Equacions
        tab_eq = ttk.Frame(nb)
        nb.add(tab_eq, text="Equacions")
        p = ttk.Frame(tab_eq, padding=10)
        p.pack(fill="both", expand=True)
        ttk.Label(p, text="Equació 2n grau (a,b,c):").grid(row=0, column=0, sticky="w")
        self.eq_entry = ttk.Entry(p, width=40)
        self.eq_entry.grid(row=0, column=1, sticky="w")
        ttk.Button(p, text="Resol", command=self.solve_quad).grid(row=0, column=2, padx=6)
        ttk.Separator(p, orient="horizontal").grid(row=1, column=0, columnspan=3, sticky="ew", pady=6)
        self.eq_output = scrolledtext.ScrolledText(p, height=20)
        self.eq_output.grid(row=2, column=0, columnspan=3, sticky="nsew", pady=6)
        p.rowconfigure(2, weight=1)
        p.columnconfigure(1, weight=1)

        # Estadística
        tab_stats = ttk.Frame(nb)
        nb.add(tab_stats, text="Estadística")
        ps = ttk.Frame(tab_stats, padding=10)
        ps.pack(fill="both", expand=True)
        ttk.Label(ps, text="Dades (números separats per coma):").grid(row=0, column=0, sticky="w")
        self.stats_entry = ttk.Entry(ps, width=60)
        self.stats_entry.grid(row=0, column=1, sticky="w")
        ttk.Button(ps, text="Resum", command=self.do_stats).grid(row=0, column=2, padx=6)
        self.stats_output = scrolledtext.ScrolledText(ps, height=20)
        self.stats_output.grid(row=1, column=0, columnspan=3, sticky="nsew", pady=6)
        ps.rowconfigure(1, weight=1)
        ps.columnconfigure(1, weight=1)

        # Menú
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Guardar informe", command=self.save_report)
        filemenu.add_separator()
        filemenu.add_command(label="Sortir", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)

    # Callbacks
    def out_poly(self, text):
        self.poly_output.insert("end", text + "\n\n")
        self.poly_output.see("end")

    def do_add(self):
        try:
            A = parse_coeffs(self.polyA_entry.get())
            B = parse_coeffs(self.polyB_entry.get())
            R = PolyAddition(A, B)
            self.out_poly(f"A = {poly_to_str(A)}\nB = {poly_to_str(B)}\nA+B = {poly_to_str(R)}\nCoefficients: {R}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def do_sub(self):
        try:
            A = parse_coeffs(self.polyA_entry.get())
            B = parse_coeffs(self.polyB_entry.get())
            R = PolySubtraction(A, B)
            self.out_poly(f"A-B = {poly_to_str(R)}\nCoefficients: {R}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def do_mul(self):
        try:
            A = parse_coeffs(self.polyA_entry.get())
            B = parse_coeffs(self.polyB_entry.get())
            R = PolyMultiplication(A, B)
            self.out_poly(f"A*B = {poly_to_str(R)}\nCoefficients: {R}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def do_div(self):
        try:
            A = parse_coeffs(self.polyA_entry.get())
            B = parse_coeffs(self.polyB_entry.get())
            q, r = PolyDivision(A, B)
            self.out_poly(f"Quocient: {poly_to_str(q)}\nResiduu: {poly_to_str(r)}\nQuotients: {q}\nResidus: {r}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def do_pow(self):
        try:
            A = parse_coeffs(self.polyA_entry.get())
            n = int(simple_prompt("Exponent", "Introdueix exponent (entero ≥ 0):", "2"))
            R = PolyPow(A, n)
            self.out_poly(f"A^{n} = {poly_to_str(R)}\nCoefficients: {R}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def do_roots(self):
        try:
            A = parse_coeffs(self.polyA_entry.get())
            roots = PolyRoot(A)
            self.out_poly(f"Polinomi: {poly_to_str(A)}\nArrels: {roots}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def solve_quad(self):
        try:
            parts = [p.strip() for p in self.eq_entry.get().split(',') if p.strip()]
            if len(parts) < 3:
                messagebox.showinfo("Info", "Introdueix a, b, c separats per coma")
                return
            a, b, c = map(float, parts[:3])
            sols = solve_quadratic(a, b, c)
            self.eq_output.insert("end", f"Equació: {a}x² + {b}x + {c}\nSolucions: {sols}\n\n")
            self.eq_output.see("end")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def do_stats(self):
        try:
            parts = [p.strip() for p in self.stats_entry.get().replace(';', ',').split(',') if p.strip()]
            nums = [float(p) for p in parts]
            summary = stats_summary(nums)
            out = json.dumps(summary, indent=2)
            self.stats_output.insert("end", out + "\n\n")
            self.stats_output.see("end")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_report(self):
        text = "===== PyMathLib App Report =====\n\n"
        text += "Polinomis output:\n" + self.poly_output.get("1.0", "end") + "\n"
        text += "Equacions output:\n" + self.eq_output.get("1.0", "end") + "\n"
        text += "Estadística output:\n" + self.stats_output.get("1.0", "end") + "\n"
        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files","*.txt")])
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            messagebox.showinfo("Guardat", f"Informe guardat a: {path}")

def simple_prompt(title, prompt, default=""):
    root = tk.Toplevel()
    root.title(title)
    root.transient()
    tk.Label(root, text=prompt).pack(padx=8, pady=6)
    ent = ttk.Entry(root, width=30)
    ent.insert(0, default)
    ent.pack(padx=8, pady=6)
    result = {"value": None}
    def ok():
        result["value"] = ent.get()
        root.destroy()
    def cancel():
        root.destroy()
    ttk.Button(root, text="OK", command=ok).pack(side="left", padx=6, pady=6)
    ttk.Button(root, text="Cancel", command=cancel).pack(side="right", padx=6, pady=6)
    root.wait_window()
    return result["value"]

if __name__ == "__main__":
    app = PyMathApp()
    app.mainloop()
