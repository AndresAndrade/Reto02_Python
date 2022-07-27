def cliente(informacion):
    informacion2 = {"nombre": informacion["nombre"], "edad": informacion["edad"]}

    if informacion["edad"] > 18:
        informacion2["atraccion"] = "X-Treme"
        informacion2["apto"] = True
        informacion2["primer_ingreso"] = informacion["primer_ingreso"]
        if informacion["primer_ingreso"] == True:
            informacion2["total_boleta"] = 20000 * 0.95
        else:
            informacion2["total_boleta"] = 20000
    elif 15 <= informacion["edad"] <= 18:
        informacion2["atraccion"] = "Carros chocones"
        informacion2["apto"] = True
        informacion2["primer_ingreso"] = informacion["primer_ingreso"]
        if informacion["primer_ingreso"] == True:
            informacion2["total_boleta"] = 5000 * 0.93
        else:
            informacion2["total_boleta"] = 5000
    elif 7 <= informacion["edad"] < 15:
        informacion2["atraccion"] = "Sillas voladoras"
        informacion2["apto"] = True
        informacion2["primer_ingreso"] = informacion["primer_ingreso"]
        if informacion["primer_ingreso"] == True:
            informacion2["total_boleta"] = 10000 * 0.95
        else:
            informacion2["total_boleta"] = 10000
    else:
        informacion2["atraccion"] = "N/A"
        informacion2["apto"] = False
        informacion2["primer_ingreso"] = informacion["primer_ingreso"]
        informacion2["total_boleta"] = "N/A"

    return informacion2


informacion = {
    "id_cliente": 1,
    "nombre": "Johana Fernandez",
    "edad": 20,
    "primer_ingreso": False
}

print(cliente(informacion))
