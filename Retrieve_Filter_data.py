import PyPDF2
file = open('Qual_FAMEQuant_Levedura_050620191570821539_labeled.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(file)
pgs = pdf.getNumPages()
lista = []
for pg in range(pdf.getNumPages()):
    page = pdf.getPage(pg)
    text = str(page.extractText())
    data = text.split("NIST11.L")[1][0:207]
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
arquivo = open("compostos_do_MS_amostra.txt","w")
arquivo.write("Composto;Ref;CAS;Qual\n")
cont = 1
for _ in range(len(ref)):
    subref = ref[0:3]
    subqual = qual[0:3]
    subcomp = comp[0:3]
    subcas = cas[0:3]
    if len(qual) == 0:
        break
    if max(subqual) >=85:
        pos = subqual.index(max(subqual))
        if " " in subref[pos]:
            arquivo.write('%s;%s;%s;%i\n'%(subcomp[pos].replace(" ",""),subref[pos][1:],subcas[pos].replace(" ",""),subqual[pos]))
            cont+=1
        else:
            arquivo.write('%s;%s;%s;%i\n'%(subcomp[pos].replace(" ",""),subref[pos],subcas[pos].replace(" ",""),subqual[pos]))
            cont+=1
    del qual[0:3]
    del ref[0:3]
    del comp[0:3]
    del cas[0:3]
arquivo.close()

#fazer o mesmo pro Qual_FAMEQuant_Levedura_050620191571235213_sim
file = open('Qual_FAMEQuant_Levedura_050620191571235213_sim.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(file)
pgs = pdf.getNumPages()
lista = []
for pg in range(pdf.getNumPages()):
    page = pdf.getPage(pg)
    text = str(page.extractText())
    data = text.split("NIST11.L")[1][0:207]
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
arquivo = open("compostos_do_MS_Qual_FAMEQuant_Levedura_050620191571235213_sim.txt","w")
arquivo.write("Composto;Ref;CAS;Qual\n")
cont = 1
for _ in range(len(ref)):
    subref = ref[0:3]
    subqual = qual[0:3]
    subcomp = comp[0:3]
    subcas = cas[0:3]
    if len(qual) == 0:
        break
    if max(subqual) >=85:
        pos = subqual.index(max(subqual))
        if " " in subref[pos]:
            arquivo.write('%s;%s;%s;%i\n'%(subcomp[pos].replace(" ",""),subref[pos][1:],subcas[pos].replace(" ",""),subqual[pos]))
            cont+=1
        else:
            arquivo.write('%s;%s;%s;%i\n'%(subcomp[pos].replace(" ",""),subref[pos],subcas[pos].replace(" ",""),subqual[pos]))
            cont+=1
    del qual[0:3]
    del ref[0:3]
    del comp[0:3]
    del cas[0:3]
arquivo.close()

