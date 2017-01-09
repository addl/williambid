 /**
 * Created by bryan on 27/09/2015.
 */
var cuentas_creadas = false;

obtener_estado_de_cuentas = function () {
    $.ajax({
        type: 'GET',
        url: "/usuarios/back-office/xhr/data/cuenta",
        success: function (response) {
            data = response;
            //console.log(data);
            lista_cuentas = JSON.parse(data.cuentas);
            if (!cuentas_creadas) {
                crear_elementos_div_de_cuenta(lista_cuentas);
                actualizar_cuentas(lista_cuentas);
            } else {
                actualizar_cuentas(lista_cuentas);
            }
        },
        error: function (response) {
            alertify.error("Error al recuperar datos de cuentas");
        }
    });
}


actualizar_cuentas = function (lista_cuentas) {
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
        $(deposito_dom).html(ultimo_deposito == saldo_actual ? 0:ultimo_deposito);
    });
}

crear_elementos_div_de_cuenta = function (lista_cuentas) {
    $.each(lista_cuentas, function (index, cuenta_json) {
        id = cuenta_json.fields.tipo_plan;
        row = $("<tr />").attr("id", "cuenta" + id);
        plan_td = $('<td align="center"></td>').html(cuenta_json.fields.tipo_plan).appendTo(row);
        amount_td = $('<td align="center"><a href="#" title="" class="amount"></a></td>').addClass('webStatsLink').appendTo(row);
        description_td = $("<td />").html("Plan de compensacion: " + cuenta_json.fields.tipo_plan + ":").appendTo(row);
        deposit_td = $('<td/>');
        deposit_span = $('<span class="statsPlus deposit"></span>').appendTo(deposit_td);
        deposit_td.appendTo(row);
        $('#bank_table').append(row);
    });
    cuentas_creadas = true;
}