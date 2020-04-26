// document ready function requires the page to be loaded before jquery
$(document).ready(function () {
	//the below toggles the sidebar on click
	$('.left-collapse').on('click', function () {
		$('.sidebar').toggleClass('active');
		$(this).toggleClass('active');
	});
});

buildSidebarDropdowns()









function buildSidebarDropdowns(){
	var conditionListWrapper = document.getElementById('conditionListWrapper')
	conditionListWrapper.innerHTML = ''
	var url = 'http://localhost:8000/api/v1/clinicalmeasures/'

	fetch(url)
	.then((resp) => resp.json())
	.then(function(data){
		console.log('Data:', data)

		var clinicalmeasureconditions = data
		// for each row in the Clinical Measure table create a list item
		for(var i in clinicalmeasureconditions){
			var condition = `
					<li>
						<a href="#${clinicalmeasureconditions[i].id}" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">${clinicalmeasureconditions[i].id.toUpperCase()}</a>
						<ul class="collapse list-unstyled" id="${clinicalmeasureconditions[i].id}">
						</ul>
					</li>
			`
			conditionListWrapper.innerHTML += condition

			var conditionListItem = document.getElementById(clinicalmeasureconditions[i].id)
			// for each clinical measure pertaining to this chronic condition create a nested list item
			for(var j in clinicalmeasureconditions[i].resource.clinicalMeasures){
				var clinicalMeasure = `
					<li>
						<a href="#">${clinicalmeasureconditions[i].resource.clinicalMeasures[j].toUpperCase()}</a>
					</li>
				`

				conditionListItem.innerHTML+=clinicalMeasure
			}



		}
	})
}