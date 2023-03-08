
function scraper_hg(url) {
    // jQuery is handy for finding DOM elements and extracting data from them.
    // To use it, make sure to enable the "Inject jQuery" option.
    const $ = context.jQuery;

    // if ($('input').first().attr('value') != '')
    // {
    //     context.log.info($('input').first().attr('value'));
    // }
    // else context.log.info('MAL');

    var values = [], labels = [];
    var id = "-", dni = "-", fechaNacimiento = "-", nombre = "-", cp = "-", hipoteca = "-", anoConst = "-", contenido = "-", continente = "-";
    var uso = "-", metros = "-", tipo = "-", hb = "-", hf = "-", hp = "-", ht = "-", codFam = "-", codPlat = "-", codBas = "-";
    for (var i = 0; i < 56; i++)
    {
        // Datos cliente
        if ($('label.control-label').eq(i).text().toLowerCase() == "nombre y apellidos")
            if ($('input').eq(i).attr('value'))
                nombre = $('input').eq(i).attr('value');
        if ($('label.control-label').eq(i).text().toLowerCase() == "documento" || $('label.control-label').eq(i).text().toLowerCase() == "numero documento")
            if ($('input').eq(i).attr('value'))
                dni = $('input').eq(i).attr('value');
        if ($('label.control-label').eq(i).text().toLowerCase() == "fecha de nacimiento")
            if ($('input').eq(i).attr('value'))
                fechaNacimiento = $('input').eq(i).attr('value');
        if ($('label.control-label').eq(i).text().toLowerCase() == "codigo postal")
            if ($('input').eq(i).attr('value'))
                cp = $('input').eq(i).attr('value');   

        // Datos vehiculo
        if ($('label.control-label').eq(i).text().toLowerCase() == "uso" || $('label.control-label').eq(i).text().toLowerCase() == "uso vivienda")
            if ($('input').eq(i).attr('value'))
                uso = $('input').eq(i).attr('value');   

        // Datos vivienda     
        if ($('label.control-label').eq(i).text().toLowerCase() == "hipoteca")
            if ($('input').eq(i).attr('value'))
                hipoteca = $('input').eq(i).attr('value');   
        if ($('label.control-label').eq(i).text().toLowerCase() == "metros construidos")
            if ($('input').eq(i).attr('value'))
                metros = $('input').eq(i).attr('value');   
        if ($('label.control-label').eq(i).text().toLowerCase() == "edificio")
            if ($('input').eq(i).attr('value'))
                tipo = $('input').eq(i).attr('value'); 
        if ($('label.control-label').eq(i).text().toLowerCase() == "año construccion" || $('label.control-label').eq(i).text().toLowerCase() == "anio construccion")
            if ($('input').eq(i).attr('value'))
                anoConst = $('input').eq(i).attr('value');   

        // Datos poliza
        if ($('label.control-label').eq(i).text().toLowerCase() == "capital continente propuesto")
            if ($('input').eq(i).attr('value'))
                continente = $('input').eq(i).attr('value');   
        if ($('label.control-label').eq(i).text().toLowerCase() == "capital contenido propuesto")
            if ($('input').eq(i).attr('value'))
                contenido = $('input').eq(i).attr('value');           

        // Datos internos
        if ($('label.control-label').eq(i).text().toLowerCase() == "codrm")
            if ($('input').eq(i).attr('value'))
                id = $('input').eq(i).attr('value');        

        // Codigos presupuesto
        if ($('label.control-label').eq(i).text().toLowerCase() == "referencia nse platino")
            if ($('input').eq(i).attr('value'))
                codPlat = $('input').eq(i).attr('value');      
        if ($('label.control-label').eq(i).text().toLowerCase() == "referencia nse tú eliges")
            if ($('input').eq(i).attr('value'))
                codBas = $('input').eq(i).attr('value');      
        if ($('label.control-label').eq(i).text().toLowerCase() == "referencia nse familia")
            if ($('input').eq(i).attr('value'))
                codFam = $('input').eq(i).attr('value');                                              

        // Precios
        if ($('label.control-label').eq(i).text().toLowerCase() == "modalidad tú eliges" || $('label.control-label').eq(i).text().toLowerCase() == "hogar basico")
            if ($('input').eq(i).attr('value'))
                hb = $('input').eq(i).attr('value');     
        if ($('label.control-label').eq(i).text().toLowerCase() == "modalidad familiar" || $('label.control-label').eq(i).text().toLowerCase() == "hogar familiar")
            if ($('input').eq(i).attr('value'))
                hf = $('input').eq(i).attr('value');     
        if ($('label.control-label').eq(i).text().toLowerCase() == "modalidad platino" || $('label.control-label').eq(i).text().toLowerCase() == "hogar platino")
            if ($('input').eq(i).attr('value'))
                hp = $('input').eq(i).attr('value');     
        if ($('label.control-label').eq(i).text().toLowerCase() == "modalidad total" || $('label.control-label').eq(i).text().toLowerCase() == "hogar total")
            if ($('input').eq(i).attr('value'))
                ht = $('input').eq(i).attr('value');       

        // Fill data
        // if ($('input').eq(i).attr('value'))
        //     values.push($('input').eq(i).attr('value'));
        // else
        //     values.push("");
        // labels.push($('label.control-label').eq(i).text());
    }

    // await context.setValue('OUTPUT', values);

    // Return an object with the data extracted from the page.
    // It will be stored to the resulting dataset.
    return {
        id: id,
        dni: dni,
        fechaNacimiento: fechaNacimiento,
        nombre: nombre,
        cp: cp,
        uso: uso,
        hipoteca: hipoteca,
        metros: metros,
        tipo: tipo,
        anoConst: anoConst,
        contenido: contenido,
        continente: continente,
        codBas: codBas,
        codFam: codFam,
        codPlat: codPlat,
        hb: hb,
        hf: hf,
        hp: hp,
        ht: ht
        // data0: {label: labels[0],
        //     value: values[0]},
        // data1: {label: labels[1],
        //     value: values[1]},
        // data2: {label: labels[2],
        //     value: values[2]},
        // data3: {label: labels[3],
        //     value: values[3]},
        // data4: {label: labels[4],
        //     value: values[4]},
        // data5: {label: labels[5],
        //     value: values[5]},
        // data6: {label: labels[6],
        //     value: values[6]},
        // data7: {label: labels[7],
        //     value: values[7]},
        // data8: {label: labels[8],
        //     value: values[8]},
        // data9: {label: labels[9],
        //     value: values[9]},
        // data10: {label: labels[10],
        //     value: values[10]},
        // data11: {label: labels[11],
        //     value: values[11]},
        // data12: {label: labels[12],
        //     value: values[12]},
        // data13: {label: labels[13],
        //     value: values[13]},
        // data14: {label: labels[14],
        //     value: values[14]},
        // data15: {label: labels[15],
        //     value: values[15]},
        // data16: {label: labels[16],
        //     value: values[16]},
        // data17: {label: labels[17],
        //     value: values[17]},
        // data18: {label: labels[18],
        //     value: values[18]},
        // data19: {label: labels[19],
        //     value: values[19]},
        // data20: {label: labels[20],
        //     value: values[20]},
        // data21: {label: labels[21],
        //     value: values[21]},
        // data22: {label: labels[22],
        //     value: values[22]},
        // data23: {label: labels[23],
        //     value: values[23]},
        // data24: {label: labels[24],
        //     value: values[24]},
        // data25: {label: labels[25],
        //     value: values[25]},
        // data26: {label: labels[26],
        //     value: values[26]},
        // data27: {label: labels[27],
        //     value: values[27]},
        // data28: {label: labels[28],
        //     value: values[28]},
        // data29: {label: labels[29],
        //     value: values[29]},
        // data30: {label: labels[30],
        //     value: values[30]},
        // data31: {label: labels[31],
        //     value: values[31]},
        // data32: {label: labels[32],
        //     value: values[32]},
    };
}