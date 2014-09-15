function togglePrestacion(self) {
    var $ = django.jQuery,
        checkbox = $(self),
        hidden_input = $("#"+checkbox.attr('data-hidden-id'));
    
    var current_list = JSON.parse(hidden_input.val());
    var should_add = checkbox.is(':checked');
    
    if ( should_add == true ){
        already_added = false;
        for (var i=0;i<current_list.length;i++){
            if (checkbox.val() == current_list[i]){
                already_added = true;
            }
        }
        
        if ( !already_added ){
            current_list.push(checkbox.val());
            hidden_input.val(JSON.stringify(current_list));
        }
    }
    
    else {
        var new_list = [];

        for (var i=0;i<current_list.length;i++){
            if (checkbox.val() != current_list[i]){
                new_list.push(current_list[i]);
            }
        }
        hidden_input.val(JSON.stringify(new_list));
    }
};
