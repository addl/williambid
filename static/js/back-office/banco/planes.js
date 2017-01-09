/**
 * Created by lion on 5/8/16.
 */

estado_planes = false;

obtener_estado_de_usuario_x_planes = function () {
    $.ajax({
        type: 'GET',
        url: "/usuarios/back-office/xhr/data/planes_estado",
        success: function (response) {
            console.log(response.estado_planes);
            data = response;
            lista_estado_planes = data.estado_planes;
            if (!estado_planes) {
                crear_elementos_div_de_estado_planes(lista_estado_planes);
                //actualizar_estado_de_planes(lista_estado_planes);
            } else {
                //actualizar_estado_de_planes(lista_estado_planes);
            }
        },
        error: function (response) {
            alertify.error("Error al recuperar el estado de los planes de compensacion");
        }
    });
}

actualizar_estado_de_planes = function (lista_cuentas) {
    $.each(lista_cuentas, function (index, cuenta_json) {
        id = "cuenta" + cuenta_json.fields.tipo_plan;
        saldo_dom = $("#" + id).find('.amount');
        saldo_anterior = parseFloat(saldo_dom.html());
        if (isNaN(saldo_anterior)) {
            saldo_anterior = 0;
        }
        saldo_actual = parseFloat(cuenta_json.fields.monto_total);
        $(saldo_dom).html(saldo_actual);
        deposito_dom = $("#" + id).find('.deposit');
        ultimo_deposito = saldo_actual - saldo_anterior;
        $(deposito_dom).html(ultimo_deposito == saldo_actual ? 0 : ultimo_deposito);
    });
}

crear_elementos_div_de_estado_planes = function (lista_estado_planes) {
    $.each(lista_estado_planes, function (index, estado_plan) {
        id = index;
        row = $("<tr />").attr("id", "estado_plan" + id);
        running_class = "taskPr";
        if (!estado_plan.estado) {
            running_class = "taskD";
        }
        no_plan_td = $('<td />').addClass(running_class);
        span_plan = $("<a />").html(index).attr("href", "#").appendTo(no_plan_td);
        no_plan_td.appendTo(row);
        descripcion_td = $('<td />').html(lista_estado_planes[index].descripcion).appendTo(row);
        row.append(construir_td_para_estado_plan(estado_plan.tipo_usuario));
        row.append(construir_td_para_estado_plan(estado_plan.tipo_membresia));
        row.append(construir_td_para_estado_plan(estado_plan.usuarios_en_red));
        row.append(construir_td_para_estado_plan(estado_plan.cantidad_de_dinero));
        row.append(construir_td_para_estado_plan(estado_plan.cantidad_de_puntos));
        $('#estado_planes_table').append(row);
    });
    estado_planes = true;
}

construir_td_para_estado_plan = function (lista_estado) {
    td = $('<td />');
    running_class = "uNotice";
    if (lista_estado[0] < 0) {
        running_class = "uAlert";
    }
    if (lista_estado[0] > 0) {
        running_class = "uDone";
    }
    span_check = $('<span />').addClass(running_class).appendTo(td);
    status_class = "";
    if (lista_estado[0] > 0) {
        status_class = "statsPlus";
    }
    if (lista_estado[0] < 0) {
        status_class = "statsMinus";
    }
    html_info = lista_estado[1] + "/" + lista_estado[2];
    /*validar si pide requisitios, === 0*/
    if(lista_estado[0] == 0){
        html_info = "-";
    }
    span_user = $('<span />').addClass(status_class).html(html_info).appendTo(td);
    return td;
}