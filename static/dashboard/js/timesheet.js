$(document).ready(function(){
    $('#add-time').on('click' , function(){
        $('#form-div').show()
    })

    $('#add-timesheet').on('click' , function(){

        var start_time = $('#from_time').val()
        var end_time = $('#to_time').val()
        var location = $('#location').val()
        var mode = $('#mode').val()
        var type = $('#type').val()
        var project = $('#project').val()
        var remarks = $('#remarks').val()

        $.ajax({
            url : '/add-timesheet/',
            type : 'POST',
            data : {
                'start_time' : start_time,
                'end_time' : end_time,
                'location' : location,
                'mode' : mode,
                'type' : type,
                'project' : project,
                'remarks' : remarks
            },

            success : function(response){
                var form = document.getElementById("timesheet-form");
                if(response.response == 'success'){
                    form.reset();
                    $('#response').append(
                        `<tr class="intro-x">

                        <td class="text-center whitespace-nowrap">
                            #
                        </td>

                        <td class="text-center whitespace-nowrap">
                            <span class="text-warning">
                                ${response.time_sheet.Client}
                            </span>
                            <br>
                            {{ timesheet.Location }} - {{ timesheet.Mode }}
                        </td>

                        <td class="text-center whitespace-nowrap">
                            {{ timesheet.Date | date:'d M Y' }}<br>
                            <span style="color: #5e72e4;">
                                {{ timesheet.Start_Time | time:"h:i A" }} to {{ timesheet.End_Time | time:"h:i A" }}
                            </span><br>
                            <span class="text-success">{{ timesheet.formatted_duration }}</span>
                        </td>

                        <td class="text-center whitespace-nowrap">
                            {{ timesheet.Remarks }} 
                        </td>

                        <td class="text-center whitespace-nowrap">
                            {% if timesheet.Status == 'Rejected' %}
                                <span class="text-danger">REJECTED</span>
                            {% elif timesheet.Status == 'Approved' %}
                                <span class="text-success">APPROVED</span>
                            {% else %}
                                <span class="text-warning">PENDING</span>
                            {% endif %}
                        </td>

                        <td class="table-report__action">
                            <div class="flex justify-center items-center">
                                <a class="flex items-center text-primary whitespace-nowrap mr-5" href="" title="edit">
                                    <i data-lucide="edit" class="w-4 h-4 mr-1"></i> 
                                </a>
                                <a onclick="delete_client('{{client.id}}')" class="flex items-center text-danger whitespace-nowrap" href="javascript:;" data-tw-toggle="modal" data-tw-target="#delete-confirmation-modal" title="delete">
                                    <i data-lucide="trash" class="w-4 h-4 mr-1"></i> 
                                </a>
                            </div>
                        </td>
                        
                    </tr>`
                    )
                }else{

                }
            }
        })
    })
})