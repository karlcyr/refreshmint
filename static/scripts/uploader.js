$("#editmode").click(function() {
	$("#tabledata").hide();
	$("#edittabledata").show();
});

$("#cancel").click(function() {
	$("#tabledata").show();
	$("#edittabledata").hide();
});

$(document).ready(function($)
  {
	$('tr th,td').hover(function()
	{
		var columnNum = $(this).parent('tr').children().index($(this));
		var $wholeColumn =  $(this).parents('table').find('td:nth-child(' + (columnNum + 1) + ')');
		$wholeColumn.addClass('columnhover');
	},
	function()
	{
		$('table').find('td').removeClass('columnhover');
	});

	$('tr th,td').click(function()
	{
	   var columnNum = $(this).parent('tr').children().index($(this));
	   var $wholeColumn =  $(this).parents('table').find('td:nth-child(' + (columnNum + 1) + ')');
	   if (!($(this).hasClass('columnselect'))) {            	
		   $wholeColumn.addClass('columnselect');
	   } else {
		   $wholeColumn.removeClass('columnselect');
	   }
   });
});

$('#edit-data-form').on('submit', function(event){
	event.preventDefault();
	edit_data();
});

function edit_data() {
	console.log($('#editdata').val())
	$.ajax({
		url : "/upload/edit_data/", // the endpoint
		type : "POST", // http method
		data : { editdata : $('#editdata').val() }, // data sent with the post request

		// handle a successful response
		success : function(text) {
			//$('#editdata').val(''); // remove the value from the input
			console.log(text); // log the returned json to the console
		},

		// handle a non-successful response
		error : function(xhr,errmsg,err) {
			$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
				" <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
			console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
		}
	});
};

	// This function gets cookie with a given name
	// https://github.com/realpython/django-form-fun/blob/master/part1/post_ajax/talk_project/static/scripts/main.js
	// https://docs.djangoproject.com/en/dev/ref/csrf/#ref-contrib-csrf
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	var csrftoken = getCookie('csrftoken');

	/*
	The functions below will create a header with csrftoken
	*/

	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}
	function sameOrigin(url) {
		// test that a given url is a same-origin URL
		// url could be relative or scheme relative or absolute
		var host = document.location.host; // host + port
		var protocol = document.location.protocol;
		var sr_origin = '//' + host;
		var origin = protocol + sr_origin;
		// Allow absolute or scheme relative URLs to same origin
		return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
		(url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
			// or any other URL that isn't scheme relative or absolute i.e relative.
			!(/^(\/\/|http:|https:).*/.test(url));
		}

		$.ajaxSetup({
			beforeSend: function(xhr, settings) {
				if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
				// Send the token to same-origin, relative URLs only.
				// Send the token only if the method warrants CSRF protection
				// Using the CSRFToken value acquired earlier
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});