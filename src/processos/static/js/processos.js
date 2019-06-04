(function () {
    $('.btn-view').on('click', function () {
        var attr_id = $(this).attr('id').split('-')[1],
            url = attr_id + '/view';
        
        window.location.href = url;
    });

    $('.btn-clone').on('click', function () {
        var csrfCookie = Cookies.get('csrftoken'),
            attr_id = $(this).attr('id').split('-')[1],
            url = 'clone/';

        $.ajax({
            url: url,
            type: 'POST',
            headers: { 'X-CSRFToken': csrfCookie },
            data: {id: attr_id},
            success: function (data) {
                window.location.href = data.url;
            },
            error: function (data) {
                alert('Erro ao clonar entidade!\n' + data);
            }
        });
    });

    $('.btn-edit').on('click', function () {
        var attr_id = $(this).attr('id').split('-')[1],
            url = attr_id + '/edit';
        
        window.location.href = url;
    });

    $('.btn-delete').on('click', function () {
        var attr_id = $(this).attr('id').split('-')[1];

        $('#modal-remove').modal('show');
        $('#confirmar-remove').off('click').on('click', function () {
            var csrfCookie = Cookies.get('csrftoken'),
                url = 'remove/';

            $.ajax({
                url: url,
                type: 'POST',
                headers: { 'X-CSRFToken': csrfCookie },
                data: {id: attr_id},
                success: function (data) {
                    window.location.href = data.url;
                },
                error: function (data) {
                    alert('Erro ao apagar entidade!\n' + data);
                }
            });
        });
    });
}());