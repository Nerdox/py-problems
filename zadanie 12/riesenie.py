try:
    value = input("zadaj samohlásky: ")
    sh = ["a", "ä", "e", "i", "y", "o", "u", "á", "é", "í", "ý", "ó", "ú", "ô"]

    for x in range(len(value)):
        p = value[x]

        if p in sh:
            print(f"S{p}d{p} m{p}ch{p} n{p} st{p}n{p}, s{p}d{p} {p} sp{p}")
        else:
            print(f"{p} neni samohlaska, bude preskocena")
except:
    print("Zadaj platne samohlasky")