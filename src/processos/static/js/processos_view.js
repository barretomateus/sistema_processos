(function () {
    var checked = $('#id_tipo_processo').html().split(','),
        len = checked.length, i;

    for (i = 0; i < len; i++) {
        if (checked[i].startsWith('outros')) { continue; }

        $('#' + checked[i]).attr('checked', 'checked');
    }

    if (checked[len - 1].startsWith('outros')) {
        $('#outros').attr('checked', 'checked');

        $('#outros_justificativa').html(checked[len - 1].substr(7));
    }
    
    $('#btn-imprimir').on('click', function () {
        window.location.href = 'requerimento/'
    });
}());
