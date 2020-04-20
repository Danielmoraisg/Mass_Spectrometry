import os
import PyPDF2
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    f = [item for item in filenames if item.count('.pdf')>= 1]
for file_name in f:
    print(file_name)
    file = open(file_name, 'rb')
    pdf = PyPDF2.PdfFileReader(file,strict=False)
    pgs = pdf.getNumPages()
    lista = []
    peak = []
    for pg in range(pdf.getNumPages()):
        page = pdf.getPage(pg)
        text = str(page.extractText())
        data = text.split("NIST11.L")[1][0:207]
        metadata = text.split("NIST11.L")[0]
        for i in metadata.split("\n"):
            if "min" in i:
                peak.append(i)
        for linha in data.split("\n"):
            if "  " in linha:
                lista.append(linha)
        lista.append("!")
    file.close()
    compostos = 0
    cont = 1
    ref = []
    qual = []
    comp = []
    cas = []
    for i in lista[5:]:
        if i == "!":
            compostos+=1
            cont = 1
        elif cont%2 != 0:
            cont+=1
            composto = i
        elif cont%2 == 0:
            ref.append(composto[-8:-2])
            comp.append(composto[2:-8])
            qual.append(int(i[-2:]))
            cas1 = composto[-1]
            casr = i[:-2]
            cas.append(cas1+casr)
            cont +=1
    cont = 1
    rel_peak = {}
    for _ in range(len(ref)):
        subref = ref[0:3]
        subqual = qual[0:3]
        subcomp = comp[0:3]
        subcas = cas[0:3]
        if len(qual) == 0:
            break
        if max(subqual) >=85:
            pos = subqual.index(max(subqual))
            rel_peak[peak[0]] = subcomp[pos]
        del peak[0]
        del qual[0:3]
        del ref[0:3]
        del comp[0:3]
        del cas[0:3]
    import csv
    with open("%s.csv"%file_name[:-4], "w") as csv_file:
        csv_file.write("compound;peak\n")
        for key in rel_peak:
            csv_file.write("%s;%s\n"%(rel_peak[key],key))
print('Finished process')
