/**
 * Created by bryan on 11/09/2015.
 */

var clock_list = [];
var subastas_list = [];

function start_clocks(clocks) {
    $.each(clocks, function (index, clock) {
        clocks[String(clock)].start();
    });
}

function actualizar_subastas(lista_subasta_id) {
    lista_subasta_json = [];
    for (var i = 0; i < lista_subasta_id.length; i++) {
        subasta_id = lista_subasta_id[i];
        obtener_datos_subasta(subasta_id);
    }
    return lista_subasta_json;
}

function actualizar_subasta_vendida(subasta_id) {
    // ponerle al reloj finalizado
    $("#clock"+subasta_id).html("Terminada");
    // poner la imagen de vendida a la subasta
    imagen_vendida = $('<div/>').attr('class', "sold_container");
    $("<div/>").attr('class', "sold_out").appendTo(imagen_vendida);
    $(imagen_vendida).appendTo($("div#subasta"+subasta_id).find('div.product_inside'));
    // al boton pujar ponerle Vendida, y desenlazar eventos
    // es posible q alguien pueda inhibir esta operacion, pero en el server se valida de todas formas si la subasta esta activa
    // por si alguien quiere seguir pujando una subasta terminada
    $("div#subasta"+subasta_id).find("div.cart").find(".boton_pujar").unbind().html("Vendida");
}

function actualizar_subasta_dom(subasta) {
    //console.log(subasta);
    if (subasta.fields.ganador != null){
        $('#ganador' + subasta.pk).html(subasta.fields.ganador);
    }else{
        $('#ganador' + subasta.pk).html("&nbsp;");
    }
    precio_actual = parseFloat(subasta.fields.precio_actual);
    $('#subasta' + subasta.pk).find('.price-new').html(Math.round(precio_actual * 100) / 100);
    time = obtener_tiempo_de_subasta(subasta);
    actualizar_reloj_subasta(subasta, time);
}

function actualizar_reloj_subasta(subasta) {
    console.log(subasta);
    fecha = obtener_tiempo_de_subasta(subasta);
    clock_list['clock' + subasta.pk].countdown(fecha);
}

function obtener_datos_subasta(subasta_id) {
    //digo precio en DOM pq no tiene pq ser igual al de la base de datos
    //ya que otros usuarios estan pujando tambien
    //este precio se comparara contra base de datos en el server
    //de modo que si hay cambios actualizamos la subasta aqui en el html
    precio_en_dom = obtener_precio_actual_de_subasta_en_dom(subasta_id);
    //alert('Precio subasta ' + precio_en_dom);
    $.ajax({
        type: 'GET',
        url: 'xhr/data/subasta/' + subasta_id,
        data: {'precio_actual': precio_en_dom},
        success: function (data, txtStatus) {
            data = JSON.parse(data);
            //console.log(data.subasta);
            if (data.actualizar) {
                actualizar_subasta_dom(data.subasta);
            }
        },
        error: function (xhr, txtStatus, thrown) {
            //alert("ERROR F5 PUJA");
            return null;
        }
    });
}

function obtener_precio_actual_de_subasta_en_dom(subasta_id) {
    return $("#subasta" + subasta_id).find(".price-new").html();
}

function obtener_tiempo_de_subasta(subasta_json) {
    future_day = new Date(subasta_json.fields.fecha_expiracion);
    //console.log("Future: " + future_day);
    //futureDateUTC = new Date(future_day.getUTCFullYear(), future_day.getUTCMonth(), future_day.getUTCDate(), future_day.getUTCHours(), future_day.getUTCMinutes(), future_day.getUTCSeconds());
    futureDateUTC = new Date(future_day.getFullYear(), future_day.getMonth(), future_day.getDate(), future_day.getHours(), future_day.getMinutes(), future_day.getSeconds());
    //console.log("FutureUTC: " + futureDateUTC);
    return futureDateUTC;
}

function pujar(subasta_id) {
    /*alert("Pujando a " + subasta_id);*/
    $.ajax({
        type: 'GET',
        url: 'xhr/pujar/' + subasta_id,
        async: true,
        dataType: 'json',
        //data: {'id':$(this).attr('id')},
        success: function (data, textStatus) {
            /*alert("SUCCESS " + data.subasta);*/
            //buscar ahora el reloj de la subasta corresponsiente y actualizar el tiempo
            actualizar_reloj_subasta(data.subasta);
            //actualizar la subasta en el documento html
            actualizar_subasta_dom(data.subasta);
        },
        error: function (xhr, textStatus, errorThrown) {
            //console.log(textStatus + " " + errorThrown);
            if (xhr.status == 403){
                $( "#dialog-message" ).dialog( "open" );
            }
        }
    });
}

function inicializar_actualizacion() {
    actualizar_subastas(subastas_list);
}

$(document).ready(function () {
    start_clocks(clock_list);
    //actualizar los datos cada 1 segundo
    setInterval(inicializar_actualizacion, 1000);
});