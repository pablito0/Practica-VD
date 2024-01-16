# Corrigiendo el error y completando los datos
datos = {
    "AL": {"poblacion": 5074296, "valor": 94072},
    "AZ": {"poblacion": 7359197, "valor": 147618},
    "AR": {"poblacion": 3045637, "valor": 17397},
    "CA": {"poblacion": 39029342, "valor": 1519230},
    "CO": {"poblacion": 5839926, "valor": 81217},
    "CT": {"poblacion": 3626205, "valor": 61942},
    "DE": {"poblacion": 1018396, "valor": 12690},
    "FL": {"poblacion": 22244823, "valor": 746904},
    "GA": {"poblacion": 10912876, "valor": 153019},
    "ID": {"poblacion": 1939033, "valor": 8831},
    "IL": {"poblacion": 12582032, "valor": 160048},
    "IN": {"poblacion": 6833037, "valor": 59969},
    "IA": {"poblacion": 3200517, "valor": 23134},
    "KS": {"poblacion": 2937150, "valor": 15441},
    "KY": {"poblacion": 4512310, "valor": 31328},
    "LA": {"poblacion": 4590241, "valor": 134067},
    "ME": {"poblacion": 1385340, "valor": 2640},
    "MD": {"poblacion": 6164660, "valor": 98509},
    "MA": {"poblacion": 6981974, "valor": 58658},
    "MI": {"poblacion": 10034113, "valor": 150027},
    "MN": {"poblacion": 5717184, "valor": 168505},
    "MS": {"poblacion": 2940057, "valor": 13396},
    "MO": {"poblacion": 6177957, "valor": 66045},
    "MT": {"poblacion": 1122867, "valor": 20814},
    "NE": {"poblacion": 1967923, "valor": 27928},
    "NV": {"poblacion": 3177772, "valor": 19360},
    "NH": {"poblacion": 1395231, "valor": 10021},
    "NJ": {"poblacion": 9261699, "valor": 118913},
    "NM": {"poblacion": 2113344, "valor": 9687},
    "NY": {"poblacion": 19677151, "valor": 306880},
    "NC": {"poblacion": 10698973, "valor": 305078},
    "ND": {"poblacion": 779261, "valor": 2195},
    "OH": {"poblacion": 11756058, "valor": 109606},
    "OK": {"poblacion": 4019800, "valor": 80681},
    "OR": {"poblacion": 4240137, "valor": 159445},
    "PA": {"poblacion": 12972008, "valor": 254195},
    "RI": {"poblacion": 1093734, "valor": 16008},
    "SC": {"poblacion": 5282634, "valor": 343272},
    "SD": {"poblacion": 5909824, "valor": 225},
    "TN": {"poblacion": 7051339, "valor": 150855},
    "TX": {"poblacion": 30029572, "valor": 534202},
    "UT": {"poblacion": 3380800, "valor": 81646},
    "VT": {"poblacion": 647064, "valor": 886},
    "VA": {"poblacion": 8683619, "valor": 243956},
    "WA": {"poblacion": 7785786, "valor": 101367},
    "WV": {"poblacion": 5892539, "valor": 10603},
    "WI": {"poblacion": 1775156, "valor": 31234},
    "WY": {"poblacion": 2581381, "valor": 2480}
}

# Realizando el cálculo solicitado: (valor / población) * 100
resultados = {estado: (datos[estado]["valor"] / datos[estado]["poblacion"]) * 100 
              for estado in datos}

for resultado in resultados:
    print(resultado,resultados[resultado])

