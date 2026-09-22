import pandas as pd

def f(x):
    return pow(x, 3) - (3*x) - 1

a = 1.0
print(f"f({a}) = {a}^3 - 3*{a} - 1 = {f(a)}")
b = 2.0
print(f"f({b}) = {b}^3 - 3*{b} - 1 = {f(b)}")
res = f(a)*f(b)
print(f"f({a})*f({b}) = {res}\n")

if res >= 0:
    print(f"Metode Bisection gagal: f({a})*f({b}) tidak bernilai negatif!")
else:
    print(f"Syarat awal terpenuhi: f({a})*f({b}) < 0 (interval [{a}, {b}] mengandung akar).\n")

fc_old = None
tabel = []
i = 1
tl = 0.0001

while True:
    c = (a+b)/2
    fa = f(a)
    fb = f(b)
    fc = f(c)
    lI = (1/2)*abs(b-a)

    if fc_old is None:
        diff = "-"
    else:
        diff = abs(fc-fc_old)

    tabel.append({
        "Iterasi": i,
        "a": round(a, 5),
        "b": round(b, 5),
        "c": round(c, 5),
        "f(a)": round(fa, 5),
        "f(b)": round(fb, 5),
        "f(c)": round(fc, 5),
        "1/2|b-a|": round(lI, 5),
        "|f(k+1)-f(k)|": round(diff, 5) if diff != "-" else "-"
    })

    if diff != "-" and diff < tl:
        print(f"Berhenti pada iterasi ke-{i} karena |f(k+1)-f(k)| = {diff:.5f} < {tl}\n")
        break

    fc_old = fc

    if fa*fc < 0:
        b = c
    else:
        a = c

    i += 1

df = pd.DataFrame(tabel)
print(df.to_string(index=False))

final_i = tabel[-1]["Iterasi"]
final_c = tabel[-1]["c"]
print(f"\nNilai hampiran akar deviasi temperatur (c{final_i}) = {final_c} °C")
