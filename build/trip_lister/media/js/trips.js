/*
*	Trips
*	Utility functions for Trip Lister
*	
*	Requires jQuery library (http://www.jquery.com)
*	
*	Taylan Pince (taylanpince at gmail dot com) - October 31, 2008
*/

$.extend($.namespace("core.Trips"), {
    
    init_markers : function() {
		$("html").addClass("has-js");
		
		$("li:last-child").addClass("last-child");
		$("li:first-child").addClass("first-child");
        
		$("input[@type=text]").addClass("text");
		$("input[@type=submit], input[@type=button]").addClass("submit");
		$("input[@type=password]").addClass("text");
		$("input[@type=file]").addClass("file");
		$("input[@type=radio]").addClass("radio");
		$("input[@type=checkbox]").addClass("checkbox");
		$("input[@type=image]").addClass("image");
        
		$("hr").wrap('<div class="hr"></div>');
	},
	
	init_create_form : function() {
	    $("#TripForm").submit(function() {
	        $.ajax({
	            url : $(this).attr("action"),
	            type : "post",
	            processData : false,
	            data : $(this).serialize(),
	            dataType : "json",
	            contentType : "application/json",
	            success : function(data) {
	                console.log(data.errors);
	            }
	        });
	        
	        return false;
	    });
	},
    
    init : function() {
        this.init_markers();
        this.init_create_form();
    }
    
});

$(function() {
    core.Trips.init();
});