$(document).ready(function(){

    function get_timesheet(){
        var member = $('#member').val()
        var client = $('#client').val()
        var status = $('#Status').val()
        var from_date = $('#from_date').val()
        var to_date = $('#to_date').val()

        html = ''

        $.ajax({
            url : '/filter-timesheet/',
            type : 'POST',
            data : {
                'member' : member,
                'client' : client,
                'status' : status,
                'from_date' : from_date,
                'to_date' : to_date
            },

            success : function(response){
                for (let i = 0; i < response.timesheets.length; i++) {
                    var timesheet = response.timesheets[i]
                    html += `
                    <tr class="intro-x" data-id="${timesheet.id}">

                        <td class="text-center whitespace-nowrap">
                            ${i}
                        </td>

                        <td class="text-center whitespace-nowrap">
                            ${ timesheet.Added_By }
                        </td>

                        <td class="text-center whitespace-nowrap">
                            <span class="text-warning">
                                ${ timesheet.Client }
                            </span>
                            <br>
                            ${ timesheet.Location } - ${ timesheet.Mode }
                        </td>

                        <td class="text-center whitespace-nowrap">
                            ${ timesheet.Date }<br>
                            <span style="color: #5e72e4;">
                                ${ timesheet.Start_Time } to ${ timesheet.End_Time }
                            </span><br>
                            <span class="text-success">${ timesheet.Duration }</span>
                        </td>

                        <td class="text-center whitespace-nowrap">
                            ${ timesheet.Remarks } 
                        </td>

                        <td class="text-center whitespace-nowrap">
                            <span class="text-warning">${timesheet.Status}</span>
                        </td>

                        <td class="table-report__action">
                            <div class="flex justify-center items-center">
                                <a class="flex items-center text-success whitespace-nowrap mr-5" title="approve" style="cursor: pointer;">
                                <i class="fa-regular fa-thumbs-up" class="w-4 h-4 mr-1 approve" onclick="approve(${timesheet.id})"></i>
                                </a>
                                <a class="flex items-center text-danger whitespace-nowrap mr-5" title="reject" style="cursor: pointer;">
                                    <i class="fa-regular fa-thumbs-down" class="w-4 h-4 mr-1 reject" onclick="reject(${timesheet.id})"></i>
                                </a>
                            </div>
                        </td>
                        
                    </tr>`
                }

                $('#response').html(html)
            }
        })
    }

    $('.approve').on('click' , function(){
        id = $(this).data('id')

        $.ajax({
            url : '/approve/',
            type : 'POST',
            data : {'id':id},

            success : function(response){
                alert(response.status)
                get_timesheet()
            }
        })
    })

    $('.reject').on('click' , function(){
        id = $(this).data('id')

        $.ajax({
            url : '/reject/',
            type : 'POST',
            data : {'id':id},

            success : function(response){
                get_timesheet()
            }
        })
    })
})