
function scraper_mt() {    
    const $ = context.jQuery;

    // if ($('input').first().attr('value') != '')
    // {
    //     context.log.info($('input').first().attr('value'));
    // }
    // else context.log.info('MAL');

    var values = [];
    var id = "-", dni = "-", cp = "-", fechaPermiso = "-", fechaNacimiento = "-", vehicle = "", fechaMatricula = "-";
    var codPresup = "-", rli = "-", sf = "-", basica = "-";
    const MAX_INPUT_NUM = 53;

    for (var i = 0; i < MAX_INPUT_NUM; i++)
    {
        // Datos cliente
        if ($('label.control-label').eq(i).text().toLowerCase() == "documento" || $('label.control-label').eq(i).text().toLowerCase() == "numero documento")
            if ($('input').eq(i).attr('value'))
                dni = $('input').eq(i).attr('value');        
        if ($('label.control-label').eq(i).text().toLowerCase() == "codigo postal")
            if ($('input').eq(i).attr('value'))
                cp = $('input').eq(i).attr('value');
        if ($('label.control-label').eq(i).text().toLowerCase() == "fecha de nacimiento")
            if ($('input').eq(i).attr('value'))
                fechaNacimiento = $('input').eq(i).attr('value');
        
        // Datos vehiculo
        if ($('label.control-label').eq(i).text().toLowerCase() == "marca")
            if ($('input').eq(i).attr('value'))
            {
                vehicle += " ";
                vehicle += $('input').eq(i).attr('value');
            }
        if ($('label.control-label').eq(i).text().toLowerCase() == "modelo")
            if ($('input').eq(i).attr('value'))
            {
                vehicle += " ";
                vehicle += $('input').eq(i).attr('value');
            }
        if ($('label.control-label').eq(i).text().toLowerCase() == "version")
            if ($('input').eq(i).attr('value'))
            {
                vehicle += " ";
                vehicle += $('input').eq(i).attr('value');
            }
        if ($('label.control-label').eq(i).text().toLowerCase() == "fecha 1 matriculacion" || $('label.control-label').eq(i).text().toLowerCase() == "1ª de matriculacion")
            if ($('input').eq(i).attr('value'))
                fechaMatricula = $('input').eq(i).attr('value');

        // Datos internos
        if ($('label.control-label').eq(i).text().toLowerCase() == "codrm")
            if ($('input').eq(i).attr('value'))
                id = $('input').eq(i).attr('value');
        if ($('label.control-label').eq(i).text().toLowerCase() == "cod presupuesto")
            if ($('input').eq(i).attr('value'))
                codPresup = $('input').eq(i).attr('value');      

        if ($('label.control-label').eq(i).text().toLowerCase() == "fecha permiso" || $('label.control-label').eq(i).text().toLowerCase() == "fecha de permiso")
            if ($('input').eq(i).attr('value'))
                fechaPermiso = $('input').eq(i).attr('value');          

        // Precios
        if ($('label.control-label').eq(i).text().toLowerCase().includes("terceros ampliado -"))
            if ($('input').eq(i).attr('value'))
                rli = $('input').eq(i).attr('value');
        if ($('label.control-label').eq(i).text().toLowerCase() == "terceros básico + seguro al conductor + asistencia en viaje")
            if ($('input').eq(i).attr('value'))
                basica = $('input').eq(i).attr('value');
        if ($('label.control-label').eq(i).text().toLowerCase().includes("todo riesgo"))
            if ($('input').eq(i).attr('value'))
                sf = $('input').eq(i).attr('value');
    }    

    // await context.setValue('OUTPUT', values);

    // Return an object with the data extracted from the page.
    // It will be stored to the resulting dataset.
    return {
        id: id,
        dni: dni,
        cp: cp,
        fchPermiso: fechaPermiso,
        fchNacimiento: fechaNacimiento,
        codPresup: codPresup,
        rli: rli,
        basica: basica,
        sf: sf,
        vehicle: vehicle,
        fchmatricula: fechaMatricula
    };
}