$(document).ready(function(){


    function removeRow(){
        $(".removeRow").click(function(e){
            e.preventDefault() ;
            var parent = $(this).parent().parent() ;
            // parent.html("").addClass("removed") ;
            parent.fadeOut(500) ;
        }) ;
    }
   
    var cpt = 0 ;
    var newEntry = "<tr id=\"" + cpt + "\" class='entry'>\
                    <td contenteditable=\"true\" class=\"weight\"></td>\
                    <td contenteditable=\"true\" class=\"value\"></td>\
                </tr>" ;


    $("#addRow").click(function(){
        $("table").append(newEntry) ;
        cpt = cpt + 1 ;
        newEntry = "<tr id=\"" + cpt + "\" class='entry'>\
        <td contenteditable=\"true\" class=\"weight\"></td>\
        <td contenteditable=\"true\" class=\"value\"></td>\
    </tr>" ;
    }) ;
        
})