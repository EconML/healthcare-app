
$(document).ready(function () {
	let columns = {};
	$('.left-collapse').on('click', function () {
		$('.sidebar').toggleClass('active');
		$(this).toggleClass('active');
	});
	$('.dropdown-toggle').click( function() {
		if( $(this).attr( 'aria-expanded' ) == "false" ){
			let id = $(this).attr( 'href' );
			if( !columns[id] ){
				$(id + " li a").each(function(item){
					$("#columns").append( "<th class="+id.substring(1)+">"+$(this).html()+"</th>" );
				} );
				columns[id] = true;
			}
		} else {
			let id = $(this).attr( 'href' );
			if( columns[id] ){
				$("."+id.substring(1)).remove();
				columns[id] = false;
			}
		}
	} );
});