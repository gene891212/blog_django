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
        element: document.getElementById("content"),
        placeholder: "Type your content here...",
        spellChecker: false,
        status: false,
        tabSize: 4,
        // autosave: {
        //     enabled: true,
        //     uniqueId: "MyUniqueID",
        //     delay: 1000,
        // },
        toolbar: [
            "heading", "bold", "italic", "strikethrough", "|",
            toolbar_br, "code", "table", "horizontal-rule", "|",
            "ordered-list", "unordered-list", "quote", "|",
            "link", "image",  "|",
            "preview", "guide"
        ],
    });

    simplemde.codemirror.on("change", function(){
        document.getElementById('id_content').value = simplemde.value();
    });

    $('#id_image').on('change',function(){
        var fileName = $(this).val()
        edit = fileName.split('\\')
        $(this).next('.custom-file-label').html(edit[edit.length - 1])
    })
})

