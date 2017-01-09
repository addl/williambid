/**
 * Created by bryan on 28/09/2015.
 */

array_retos = [];

$(function () {
    obtener_retos();
});

obtener_retos = function () {
    $.ajax({
        type: 'GET',
        url: '/usuarios/back-office/xhr/data/retos',
        success: function (response) {
            //console.log(response);
            crear_elementos_dom_retos(response.retos);
            obtener_estado_retos_usuario();
            setInterval(obtener_estado_retos_usuario, 5000);
        },
        error: function (response) {
            alertify.error('Error recuperando retos del servidor ' + response);
        }
    });
}

obtener_estado_retos_usuario = function () {
    $.ajax({
        type: 'GET',
        url: '/usuarios/back-office/xhr/data/retos/estado',
        success: function (response) {
            //console.log(response);
            actualizar_estado_retos(response.retos_usuarios);
        },
        error: function (response) {
            alertify.error(response);
        }
    });
}


crear_elementos_dom_retos = function (lista_retos) {
    //lista_json = JSON.parse(lista_retos);
    lista_json = lista_retos;
    contenedor = $('#contenedor_retos');
    if (lista_retos.length == 0) {
        $('<h3/>').html('No existen retos actualmente!!!').appendTo('#contenedor_retos');
    } else {
        //console.log(lista_retos);
        ul_dom = $('<ul/>');
        $.each(lista_json, function (index, reto) {
            array_retos['reto-' + reto.reto.pk] = reto;
            //console.log(index + ' - ' + reto);
            desc = $('<label>').html(reto.descripcion);
            action = $('<a/>').addClass('button');
            if (reto.participa) {
                $(action).html('Participando');
            } else {
                $(action).html('Participar').click(function () {
                    inscribir_en_reto(this, reto.reto.pk);
                });
            }
            estado_user = crear_elementos_dom_estado_en_reto(reto);
            etiqueta = $('<div/>').append(desc).append(action).append(estado_user);
            $('<li/>').addClass('reto').append(etiqueta).appendTo(ul_dom);
        });
        $(ul_dom).appendTo('#contenedor_retos');
    }
}

actualizar_estado_retos = function (retos_usuarios_json) {
    lista_estado = JSON.parse(retos_usuarios_json);
    $.each(lista_estado, function (index, estado_reto) {
        cant_personas = estado_reto.fields.cantidad_personas;
        dinero_pktes_de_pujas = estado_reto.fields.dinero_paquetes_de_pujas;
        id = estado_reto.fields.reto;
        //contenedor_estado_reto = $('#estado_en_reto'+id);
        personas = $('#cantidad_personas' + id);

        try {
            $(personas).html(cant_personas);
        } catch (err) {
        }
        dinero = $('#dinero_paquetes_de_pujas' + id);
        try {
            $(dinero).html(dinero_pktes_de_pujas);
        } catch (err) {
        }
        reto = array_retos['reto-' + id];
        console.log('Resto is ' + reto + ' id ' + id);
        progreso = 0
        if (reto.reto.fields.personas != null) {
            total_personas = reto.reto.fields.personas;
            progreso = cant_personas * 100 / total_personas;
        } else {
            total_dinero = reto.reto.fields.dinero_pktes_de_pujas;
            progreso = dinero_pktes_de_pujas * 100 / total_dinero;
        }
        progreso_dom = $('#progreso_en' + id).html(progreso + ' %');
    });
}

crear_elementos_dom_estado_en_reto = function (reto_json) {
    id = reto_json.reto.pk;
    container = $('<div/>').attr('id', 'estado_en_reto' + id).addClass('estado_reto');
    if (reto_json.reto.fields.dinero_pktes_de_pujas != null) {
        label = $('<span/>').html('Dinero en paquetes de pujas:');
        valor = $('<span/>').attr('id', 'dinero_paquetes_de_pujas' + id);
        container.append(label);
        container.append(valor);
    }
    if (reto_json.reto.fields.personas != null) {
        label = $('<span/>').html('Cantidad de personas:');
        valor = $('<span/>').attr('id', 'cantidad_personas' + id);
        container.append(label);
        container.append(valor);
    }
    if (reto_json.reto.fields.tiempo != null) {
        label = $('<span/>').html('Tiempo restante:');
        valor = $('<span/>').attr('id', 'reto_countdown' + id);
        container.append(label);
        container.append(valor);
        fecha = new Date(reto_json.reto.fields.tiempo);
        //console.log(fecha + " desde " + reto_json.reto.fields.tiempo)
        $(valor).countdown(obtener_fecha_utc_from(fecha), function (event) {
            $(this).text(event.strftime('%d dias, %H:%M:%S'));
        }).on('finish.countdown', function () {

        });
    }
    progreso_label = $('<span />').html('Progreso:');
    progreso_valor = $('<span/>').attr('id', 'progreso_en' + id);
    container.append(progreso_label).append(progreso_valor);
    return container;
}

inscribir_en_reto = function (elem, reto_id) {
    //console.log(reto_id);
    $.ajax({
        type: 'GET',
        data: {reto_id: reto_id},
        url: '/usuarios/back-office/xhr/data/retos/inscripcion',
        success: function (response) {
            //console.log(response);
            alertify.success('Inscrito en el reto');
            $(elem).html('Participando').unbind();
        },
        error: function (response) {
            alertify.error('No podemos inscribirle en estos momentos');
        }
    });
}

obtener_fecha_utc_from = function (fecha) {
    future_day = fecha;
    futureDateUTC = new Date(future_day.getUTCFullYear(), future_day.getUTCMonth(), future_day.getUTCDate(), future_day.getUTCHours(), future_day.getUTCMinutes(), future_day.getUTCSeconds());
    return futureDateUTC;
}