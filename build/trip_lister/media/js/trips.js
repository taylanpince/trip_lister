/*
*	Trips
*	Utility functions for Trip Lister
*	
*	Requires jQuery library (http://www.jquery.com)
*	
*	Taylan Pince (taylanpince at gmail dot com) - October 31, 2008
*/

$.extend($.namespace("core.Trips"), {
    
    error_template : '<p class="error">%(error)</p>',
    trip_table_template : '<tr><td>%(title)</td><td>%(start_date)</td><td>%(end_date)</td><td>%(total_days)</td></tr>',
    
    render_trips : function(data) {
        $("#StartDate").text(data.start_date);
        $("#EndDate").text(data.end_date);
        $("#LostDays").text(data.lost_days);
        
        $("#TripsTable > tbody").find("tr").remove();
        
        for (t in data.trips) {
            $("#TripsTable > tbody").append(core.render_template(this.trip_table_template, data.trips[t]));
        }
        
        $("#UpdateButton").attr("disabled", false);
    },
	
	update_trips : function() {
        $("#UpdateButton").attr("disabled", true);
        
	    $.ajax({
	        url : location.href,
            type : "get",
            processData : false,
            dataType : "json",
            contentType : "application/json",
            success : this.render_trips.bind(this)
	    });
	},
	
	parse_create_form : function(data) {
	    if (data.errors) {
	        for (error in data.errors) {
	            if (error == "__all__") {
	                for (e in data.errors[error]) {
        	            $("#TripForm").prepend(core.render_template(this.error_template, {
        	                "error" : data.errors[error][e]
        	            }));
	                }
	            } else {
    	            $("#TripForm-" + error).parent().prepend(core.render_template(this.error_template, {
    	                "error" : data.errors[error]
    	            }));
	            }
	        }
	    } else {
	        $("#TripForm")[0].reset();
	        
	        this.update_trips();
	    }
	    
	    $("#TripForm").find("input[@type=submit]").attr("disabled", false);
	},
	
	submit_create_form : function() {
	    $("#TripForm").find("p.error").remove();
	    $("#TripForm").find("input[@type=submit]").attr("disabled", true);
	    
        $.ajax({
            url : $("#TripForm").attr("action"),
            type : "post",
            processData : false,
            data : $("#TripForm").serialize(),
            dataType : "json",
            contentType : "application/json",
            success : this.parse_create_form.bind(this)
        });
        
        return false;
	},
    
    init : function() {
        core.init_markers();
        
        $("#TripForm").submit(this.submit_create_form.bind(this));
        $("#UpdateButton").click(this.update_trips.bind(this));
    }
    
});

$(function() {
    core.Trips.init();
});