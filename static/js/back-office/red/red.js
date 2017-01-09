/**
 * Created by lion on 3/28/16.
 */

obtener_red_de_usuario = function (usuario_username, root) {
    $("#OrganiseChart6").html("");
    build_url = "/usuarios/back-office/xhr/data/red/red";
    if (usuario_username != null) {
        build_url = "/usuarios/back-office/xhr/data/red/red?username=" + usuario_username;
    }
    $.ajax({
        type: 'GET',
        url: build_url,
        success: function (response) {
            data = response;
            /*console.log(data);*/
            arrays_object = new Array()
            $.each(data.first_generation, function (index, item) {
                var obj = {
                    image: "/static/back_office/images/user.png",
                    text: {
                        name: item.username,
                        desc: item.membresia,
                        contact: {val: "Details", href: "#"}
                    },
                    HTMLclass: "user_tree_node",
                };
                arrays_object.push(obj);
            });
            root.children = arrays_object;
            new Treant(tree_structure);
            /*enlazamos los eventos a cada nodo*/
            $(".user_tree_node > img").click(function (event) {
                username = $(this).parent().find('p.node-name').html();
                var node_object = buscar_usuario_en_arbol(username, tree_structure.nodeStructure);
                //alert(node_object);
                obtener_red_de_usuario(node_object.text.name, node_object);
            });
            $(".user_tree_node > a").click(function (event) {
                event.preventDefault();
                username = $(this).parent().find('p.node-name').html();
                console.log("Asking profile of " + username);
                popup = $("<div/>").attr('id', 'modal').attr('title', "Details of " + username);
                $.getJSON("/usuarios/back-office/xhr/data/profile?username="+username, function(result){
                    //result = JSON.parse(response);
                    //console.log(result);
                    $("<p/>").html("Email: " + result.user_profile.email).appendTo(popup);
                    $("<p/>").html("Membresia: " + result.user_profile.membresia).appendTo(popup);
                    $("<p/>").html("Pais: " + result.user_profile.pais).appendTo(popup);
                    $("<p/>").html("Provincia: " + result.user_profile.provincia).appendTo(popup);
                    $("<p/>").html("Skype-ID: " + result.user_profile.skype).appendTo(popup);
                    $("<p/>").html("Whatsapp-ID: " + result.user_profile.whatsapp).appendTo(popup);
                    $("<p/>").html("Telefono: " + result.user_profile.telefono).appendTo(popup);
                });
                $('body').append(popup);
                $(popup).dialog();
            });
        },
        error: function (response) {
            alertify.error("Error al obtener red du usuario");
        }
    });
}

buscar_usuario_en_arbol = function (username, node_object) {
    if (node_object.text.name == username) {
        return node_object;
    }
    if (node_object.children == null) {
        return null;
    }
    found_elem = null;
    for (i = 0; i < node_object.children.length && found_elem == null; i++) {
        node_user = node_object.children[i];
        found_elem = buscar_usuario_en_arbol(username, node_user);
        if (found_elem != null) {
            return found_elem;
        }
    }
    return found_elem;
}