var json = {
    "cigreport": [],
};

function printJSON() {
    $('#json').val(JSON.stringify(json));

}

function updateJSON(data) {
    json = data;
   
    var json_str = JSON.stringify(json);
    console.log(json_str);
    $('#json_value').val(json_str);
    printJSON();
}

function showPath(path) {
    $('#path').text(path);
}

$(document).ready(function() {

    $('#rest > button').click(function() {
        var url = $('#rest-url').val();
        $.ajax({
            url: url,
            dataType: 'jsonp',
            jsonp: $('#rest-callback').val(),
            success: function(data) {
                json = data;
                $('#editor').jsonEditor(json, { change: updateJSON, propertyclick: showPath });
                printJSON();
            },
            error: function() {
                alert('Something went wrong, double-check the URL and callback parameter.');
            }
        });
    });

    $('#json').change(function() {
        var val = $('#json').val();
        $('')

        if (val) {
            try { json = JSON.parse(val); }
            catch (e) { alert('Error in parsing json. ' + e); }
        } else {
            json = {};
        }
        
        $('#editor').jsonEditor(json, { change: updateJSON, propertyclick: showPath });
    });

    $('#expander').click(function() {
        var editor = $('#editor');
        editor.toggleClass('expanded');
        $(this).text(editor.hasClass('expanded') ? 'Collapse' : 'Expand all');
    });
    
    printJSON();
    $('#editor').jsonEditor(json, { change: updateJSON, propertyclick: showPath });
});

