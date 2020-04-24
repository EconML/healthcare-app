// document ready function requires the page to be loaded before jquery
$(document).ready(function () {
	let columns = {};
	//the below toggles the sidebar on click
	$('.left-collapse').on('click', function () {
		$('.sidebar').toggleClass('active');
		$(this).toggleClass('active');
	});
});

buildList()

function buildList(){
	var conditionList = document.getElementById('conditionList')
	conditionList.innerHTML = ''
	var url = 'http://localhost:8000/api/v1/clinicalmeasures/'

	fetch(url)
	.then((resp) => resp.json())
	.then(function(data){
		console.log('Data:', data)

		var clinicalmeasureconditions = data
		for(var i in clinicalmeasureconditions){
			var condition = `
					<li>
						<a href="#diabeticSubmenu" data-toggle="collapse" aria-expanded="false" class="dropdown-toggle">${clinicalmeasureconditions[i].id}</a>
						<ul class="collapse list-unstyled" id="diabeticSubmenu">
							<li>
								<a href="#">Diabetes HgbA1c testing</a>
							</li>
							<li>
								<a href="#">Diabetes Retinal Eye Exam</a>
							</li>
							<li>
								<a href="#">Diabetes Foot Exam</a>
							</li>
						</ul>
					</li>
			`

			conditionList.innerHTML += condition


			console.log(clinicalmeasureconditions[i].id)
			console.log(clinicalmeasureconditions[i].resource)

		}
	})
}
