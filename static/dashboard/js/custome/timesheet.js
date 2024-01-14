$(document).ready(function(){
    $('#project').on('change',function(){
        var client_id = $('#project').val()

        $.ajax({
            url : '/timesheet/get/tasks/',
            type : 'POST',
            data : {'client_id':client_id},

            success : function(response){
                for (let i = 0; i < response.tasks.length; i++) {
                    html += '<option value="'+response.tasks[i].id+'">'+response.tasks[i].title+'</option>'
                }

                $('#task').html(html)
            }
        })
    })
})