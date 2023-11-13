def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(v):
    if v.find("ft") != -1 :
        v = v.replace("ft", "")
    m = float(v)
    m *= 0.3048
    return m
main()