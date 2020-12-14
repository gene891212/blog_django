$(document).ready(function(){
    var toolbar_br = {
        name: "br",
        title: "New line",
        className: "fa fa-level-down fa-rotate-90",
        action: function(editor) {
            var cm = editor.codemirror;
			cm.replaceSelection("<br>");
        }
    };
    
    var simplemde = new SimpleMDE({
        element: $('#id_content').html(),
        placeholder: "Type your content here...",
        spellChecker: false,
        status: false,
        tabSize: 4,
        toolbar: [
            "heading", "bold", "italic", "strikethrough", "|",
            toolbar_br, "code", "table", "horizontal-rule", "|",
            "ordered-list", "unordered-list", "quote", "|",
            "link", "image",  "|",
            "preview", "guide"
        ],
    });

    simplemde.codemirror.on("change", function(){
        $('#id_content').val(simplemde.value())
    });

    $('#id_image').on('change',function(){
        var fileName = $(this).val()
        edit = fileName.split('\\')
        $(this).next('.custom-file-label').html(edit[edit.length - 1])
    })

    $("input[type='submit']").on('click',function(){
        if ($('#id_content').val() == ''){
            $('#error_msg').html('<div class="alert alert-danger" role="alert">Content can\'t not be blank.</div>')
        }
    })
})

