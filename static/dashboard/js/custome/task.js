$('#task-view-btn').on('click',function(){
    var id = $('#task-view-id').val()
    alert('task id : '+id)

    $.ajax({
        url : '/task/view/',
        type : 'POST',
        data : {'task_id':id},

        success : function(response){
            alert(response.title)
        }
    })
})