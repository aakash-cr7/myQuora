QSearch =(function() {
    var el;
    function updateResults(questions) {
        $('#results').show();
        if( questions.length === 0) {
            $('.collection-header').html('No Results');
            $('#results').hide();
        } else {
            $('.collection-header').html(questions.length + ' questions found ');
        }
        $('.collection-item').remove();
        for (var i = 0; i < questions.length; i++) {
            var el = $('<li class="collection-item"></li>');
            el.html(questions[i].title);
            $('.collection').append(el);
        }
    }
    function search() {
        var term = $(this).val();
        $.ajax({
            url: '/question/search/',
            data: { 'q': term },
            type: 'GET',
            success: function(data, status, xhr) {
                console.log(data);
                updateResults(data['question']);
            }
        });
    }
    function init(id) {
        el = $('#' + id);
        el.on('input', search);
    }
    return {
        'init' : init,
    };

})();
