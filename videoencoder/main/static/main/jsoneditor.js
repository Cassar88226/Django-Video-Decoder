var notes_json = {
    "key": [],
};

var questions_json = {
    "key": [],
};

var summary_json = {
    "key": [],
};

var topic_scope_json = {
    "key": [],
};

function updateJSON(data) {
    notes_json = data;
    var json_str = JSON.stringify(notes_json);
    $('#notes').val(json_str);
    // printJSON();
}

function updateQuestionJSON(data) {
    questions_json = data;
    var json_str = JSON.stringify(questions_json);
    $('#questions').val(json_str);
}

function updateSummaryJSON(data) {
    summary_json = data;
    var json_str = JSON.stringify(summary_json);
    $('#summary').val(json_str);
}

function updateTopicScopeJSON(data) {
    topic_scope_json = data;
    var json_str = JSON.stringify(topic_scope_json);
    $('#topic_scope').val(json_str);
}

function showPath(path) {
    $('#path').text(path);
}

$(document).ready(function() {

    $('#note_editor').jsonEditor(notes_json, { change: updateJSON, propertyclick: showPath });
    $('#questions_editor').jsonEditor(questions_json, { change: updateQuestionJSON, propertyclick: showPath });
    $('#summary_editor').jsonEditor(summary_json, { change: updateSummaryJSON, propertyclick: showPath });
    $('#topic_scope_editor').jsonEditor(topic_scope_json, { change: updateTopicScopeJSON, propertyclick: showPath });

});


