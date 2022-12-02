def procesar_planilla(composers, works, sheet):
    d = {}
    artists_d = {}
    comp = open(composers)
    songs = open(works)
    songsheet = open(sheet)
    line1 = 0 # para solo usar la primera línea de los archivos de planilla
    songscounter = 0 # contador de canciones total para después saber en cuánto repartir el total
    for artists in comp:
        templ = artists.strip().split(";")
        artists_d[templ[0]] = templ[1]
    for line in songsheet:
        if line1 == 0:
            eventdetails = line.strip().split(";")
            line1 += 1
        else:
            songcode = line.strip()
            if songcode not in d:
                d[songcode] = songcode
            songscounter += 1
    budget = round(int(eventdetails[-1])/songscounter)
    for songvalues in songs:
        nlist = songvalues.strip().split(";")
        if nlist[0] in d and d[nlist[0]] == nlist[0]:
            d[nlist[0]] = []
            d[nlist[0]].append(nlist[1])
            nnlist = nlist[2:]
            for artistcode1 in nnlist:
                if artistcode1 in artists_d:
                    artistname = artists_d[artistcode1]
                    namebudgetlist = [artistname, round(budget/len(nnlist))]
                d[nlist[0]].append(namebudgetlist)
    comp.close()
    songs.close()
    songsheet.close()
    return d
d = {}
arch = open("planillas.txt")
newfile = open("liquidación.txt", "w")
newfile.write("Liquidación por derechos de autor\n")
for line in arch:
    nline = line.strip()
    d1 = procesar_planilla('autores.csv', 'obras.csv', nline)
    for key in d1:
        nlist = d1[key][1:]
        for pos in range(0,len(nlist)):
            name = nlist[pos][0]
            money = nlist[pos][1]
            if name not in d:
                d[name] = []
            d[name].append(money)
nlist = []
for name in d:
    nlist.append([sum(d[name]),name])
    nlist.sort(reverse=True)
for money, name in nlist:
    lol = "Compositor(a): {0}, Monto consolidado: ${1}.\n"
    newfile.write(lol.format(name,money))
arch.close()
newfile.close()

# Código hecho por Felipe Bustos, aka half_pipes.