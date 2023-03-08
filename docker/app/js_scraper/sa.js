function scraper_sa() {
    const $ = context.jQuery;

    // if ($('input').first().attr('value') != '')
    // {
    //     context.log.info($('input').first().attr('value'));
    // }
    // else context.log.info('MAL');

    var values = [], labels = [];
    var id = "-", nombre = "-", cp = "-", reembolso = "-", bucal = "-", premier = "-", supra = "-", plus = "-", nAseg = "-";
    for (var i = 0; i < 30; i++)
    {
        // Datos cliente
        if ($('label.control-label').eq(i).text().toLowerCase() == "nombre y apellidos")
            if ($('input').eq(i).attr('value'))
                nombre = $('input').eq(i).attr('value');
        if ($('label.control-label').eq(i).text().toLowerCase() == "codigo postal" || $('label.control-label').eq(i).text().toLowerCase() == "provincia")
            if ($('input').eq(i).attr('value'))
                cp = $('input').eq(i).attr('value');                

        // Precios
        if ($('label.control-label').eq(i).text().toLowerCase() == "reembolso")
            if ($('input').eq(i).attr('value'))
                reembolso = $('input').eq(i).attr('value');
        if ($('label.control-label').eq(i).text().toLowerCase() == "garantía bucal")
            if ($('input').eq(i).attr('value'))
                bucal = $('input').eq(i).attr('value');
        if ($('label.control-label').eq(i).text().toLowerCase() == "asistencia sanitaria premier")
            if ($('input').eq(i).attr('value'))
                premier = $('input').eq(i).attr('value');
        if ($('label.control-label').eq(i).text().toLowerCase() == "asistencia sanitaria supra")
            if ($('input').eq(i).attr('value'))
                supra = $('input').eq(i).attr('value');
        if ($('label.control-label').eq(i).text().toLowerCase() == "asistencia sanitaria plus")
            if ($('input').eq(i).attr('value'))
                plus = $('input').eq(i).attr('value');                

        if ($('label.control-label').eq(i).text().toLowerCase() == "número asegurados")
            if ($('input').eq(i).attr('value'))
                nAseg = $('input').eq(i).attr('value');

        if ($('label.control-label').eq(i).text().toLowerCase() == "codrm")
            if ($('input').eq(i).attr('value'))
                id = $('input').eq(i).attr('value');

        // Fill data
        if ($('input').eq(i).attr('value'))
            values.push($('input').eq(i).attr('value'));
        else
            values.push("");
        labels.push($('label.control-label').eq(i).text());

        // if ($('label.control-label').eq(i).text() == "Nombre y apellidos")
        //     nombre = $('input').eq(i).attr('value');

        // if ($('label.control-label').eq(i).text() == "codRM")
        //     id = $('input').eq(i).attr('value');
    }
    // context.log.info(values[18]);
    

    // await context.setValue('OUTPUT', values);

    // Return an object with the data extracted from the page.
    // It will be stored to the resulting dataset.
    return {
        id: id,
        nombre: nombre,
        cp: cp,
        nAseg: nAseg,
        reembolso: reembolso,
        bucal: bucal,
        premier: premier,
        supra: supra,
        plus: plus
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
        //     value: values[21]}
    };
}