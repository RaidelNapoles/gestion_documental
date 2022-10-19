window.setTimeout(function () {
	$("#message_container")
		.fadeTo(400, 0)
		.slideUp(400, function () {
			$(this).remove();
		});
}, 1500);
