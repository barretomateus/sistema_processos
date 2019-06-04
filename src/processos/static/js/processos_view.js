(function () {
    var checked = $('#id_tipo_processo').html().split(','),
        len = checked.length, i;

    for (i = 0; i < len - 1; i++) {
        $('#' + checked[i]).attr('checked', 'checked');
    }
    
    $('#btn-imprimir').on('click', function () {
        window.location.href = 'requerimento/'
    });
}());
