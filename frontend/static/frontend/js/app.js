// document ready function requires the page to be loaded before jquery
$(document).ready(function () {
	//the below toggles the sidebar on click
	$('.left-collapse').on('click', function () {
		$('.sidebar').toggleClass('active');
		$(this).toggleClass('active');
	});
});

buildSidebarDropdowns()

function populateTable(measures){
	//grab table wrapper where data will be inserted
	var tableWrapper = document.getElementById('tableWrapper')
	//django rest API url for service requests
	var url = 'http://localhost:8000/api/v1/servicerequest/'
	//reset current display
	tableWrapper.innerHTML = ''

	fetch(url)
	.then((resp) => resp.json())
	.then(function(data){
		console.log('Data:', data)
			//list of all service requests
			var serviceRequestList = data
			//for each request create a row for that request
			for(var request in serviceRequestList){
				console.log(serviceRequestList[request].resource.subject.id)
				if(serviceRequestList[request].resource.disease==='Hypertension' && measures[0]==='hypertension control'){
					var tableRow = `
						<tr>
							<td>
								${ serviceRequestList[request].resource.subject.id}
							</td>
							<td>
								${ serviceRequestList[request].resource.date}
							</td>
							<td>
								${ serviceRequestList[request].resource.measures.value}
							</td>
						</tr>
					`
					tableWrapper.innerHTML += tableRow
				}

			}
	})
}

function populateHeaders(measures){
	var head = document.getElementById('columns')
	head.innerHTML = ''
	head.innerHTML += '<th>Patient ID</th><th>Date</th>'
	for(var i in measures){
		var th = `
			<th>
				${ measures[i] }
			</th>
		`
		head.innerHTML += th
	}
	populateTable(measures)
}


function buildSidebarDropdowns(){

	var conditionListWrapper = document.getElementById('conditionListWrapper')
	conditionListWrapper.innerHTML = ''
	var url = 'http://localhost:8000/api/v1/clinicalmeasures/'

	fetch(url)
	.then((resp) => resp.json())
	.then(function(data){
		console.log('Data:', data)

		var clinicalmeasureconditions = data


		// for each condition in the Clinical Measure table create a list item
		for(var i in clinicalmeasureconditions){
			var condition = `
					<li id="${clinicalmeasureconditions[i].id}Listener">
						<a href="#${clinicalmeasureconditions[i].id}"
							class="dropdown-toggle"
							data-toggle="collapse"
							aria-expanded="false">${clinicalmeasureconditions[i].id.toUpperCase()}</a>
						<ul class="collapse list-unstyled" id="${clinicalmeasureconditions[i].id}">
						</ul>
					</li>
			`
			conditionListWrapper.innerHTML += condition

			var conditionListItem = document.getElementById(clinicalmeasureconditions[i].id)
			// for each clinical measure pertaining to this condition create a nested list item
			for(var j in clinicalmeasureconditions[i].resource.clinicalMeasures){
				var clinicalMeasure = `
					<li>
						<a href="#">${clinicalmeasureconditions[i].resource.clinicalMeasures[j].toUpperCase()}</a>
					</li>
				`

				conditionListItem.innerHTML+=clinicalMeasure
			}

		}

		var diabetesListener=document.getElementById('diabetesListener')
		diabetesListener.addEventListener("click", function() {
			populateHeaders(clinicalmeasureconditions[0].resource.clinicalMeasures)
			}, false)



		document.getElementById('hypertensionListener').addEventListener("click", function() {
			populateHeaders(clinicalmeasureconditions[1].resource.clinicalMeasures)
			}, false)


	})
}
