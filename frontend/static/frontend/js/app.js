// document ready function requires the page to be loaded before jquery
$(document).ready(function() {
  //the below toggles the sidebar on click
  $('.left-collapse').on('click', function() {
    $('.sidebar').toggleClass('active');
    $(this).toggleClass('active');
  });
});

buildSidebarDropdowns()

function populateTable(measures) {
  //grab table wrapper where data will be inserted
  var tableWrapper = document.getElementById('tableWrapper')
  //django rest API url for service requests
  var url = 'http://localhost:8000/api/v1/servicerequest/'
  //reset current display
  tableWrapper.innerHTML = ''

  fetch(url)
    .then((resp) => resp.json())
    .then(function(data) {
        console.log('Data:', data)
        //list of all service requests
        var serviceRequestList = data

				var patientID = {}
        //for each request create a row for that request
        for (var request in serviceRequestList) {
          // console.log(serviceRequestList[request].resource.subject.id)
          /*
          1st check to see which condition we are looking at by checking the first
          item in the measures array.
          2nd. Build out the table w/ data corresponding to the condition we are
          looking at
          */
          if (measures[0] === 'systolic') {
            if (serviceRequestList[request].resource.disease === 'Hypertension') {
              var tableRow = `
							<tr>
								<td>
									${ serviceRequestList[request].resource.subject.id}
								</td>
								<td>
									${ serviceRequestList[request].resource.date}
								</td>
								<td>
									${ serviceRequestList[request].resource.measures.systolic}
								</td>
								<td>
									${ serviceRequestList[request].resource.measures.diastolic}
								</td>
							</tr>
						`
              tableWrapper.innerHTML += tableRow
            }
          } else {
            	if(serviceRequestList[request].resource.disease === 'Diabetes') {
              var id = serviceRequestList[request].resource.subject.id
              if(!(id in patientID)) {
                patientID[id] = {
                  'id': id,
                  'foot exam': {
										'date': 0,
										'value': 0
									},
                  'hgba1c': {
										'date': 0,
										'value': 0
									},
                  'reinal eye exam': {
										'date': 0,
										'value': 0
									}
                }
                patientID[id][serviceRequestList[request].resource.measures.measure_perfomed]['value'] = serviceRequestList[request].resource.measures.value
								patientID[id][serviceRequestList[request].resource.measures.measure_perfomed]['date'] = serviceRequestList[request].resource.date

              } else {
								console.log(serviceRequestList[request].resource.measures.measure_perfomed)
								patientID[id][serviceRequestList[request].resource.measures.measure_perfomed]['value'] = serviceRequestList[request].resource.measures.value
								patientID[id][serviceRequestList[request].resource.measures.measure_perfomed]['date'] = serviceRequestList[request].resource.date
              }
            }
          }
        }
				//TODO: add conditional to ensure this only runs if the diabetesListener was clicked
				if(measures[0]==='hgba1c'){
					console.log("hello")
					for(id in patientID){
						var tableRow = `
							<tr>
								<td>
									${ id }
								</td>
								<td>
									${ patientID[id]['hgba1c']['date']}
								</td>
								<td>
									${ patientID[id]['hgba1c']['value']}
								</td>
								<td>
									${ patientID[id]['reinal eye exam']['date']}
								</td>
								<td>
									${ patientID[id]['reinal eye exam']['value']}
								</td>
								<td>
									${ patientID[id]['foot exam']['date']}
								</td>
								<td>
									${ patientID[id]['foot exam']['value']}
								</td>
							</tr>
						`

						tableWrapper.innerHTML += tableRow
					}

				}
    })
}

function populateHeaders(measures) {
  var head = document.getElementById('columns')
  head.innerHTML = ''
  head.innerHTML += '<th>Patient ID</th>'
  if (measures[0] === 'systolic') {
    var th = `
			<th>
				Date
			</th>
			<th>
				systolic
			</th>
			<th>
				diastolic
			</th>
		`
    head.innerHTML += th
  } else {
    for (var i in measures) {
      var th = `
				<th>
					Date
				</th>
				<th>
					${ measures[i] }
				</th>
			`
      head.innerHTML += th
    }
  }
  populateTable(measures)
}


function buildSidebarDropdowns() {

  var conditionListWrapper = document.getElementById('conditionListWrapper')
  conditionListWrapper.innerHTML = ''
  var url = 'http://localhost:8000/api/v1/clinicalmeasures/'

  fetch(url)
    .then((resp) => resp.json())
    .then(function(data) {
      console.log('Data:', data)

      var clinicalmeasureconditions = data


      // for each condition in the Clinical Measure table create a list item
      for (var i in clinicalmeasureconditions) {
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
        for (var j in clinicalmeasureconditions[i].resource.clinicalMeasures) {
          var clinicalMeasure = `
					<li>
						<a href="#">${clinicalmeasureconditions[i].resource.clinicalMeasures[j].toUpperCase()}</a>
					</li>
				`

          conditionListItem.innerHTML += clinicalMeasure
        }

      }

      var diabetesListener = document.getElementById('diabetesListener')
      diabetesListener.addEventListener("click", function() {
        populateHeaders(clinicalmeasureconditions[0].resource.clinicalMeasures)
      }, false)



      var hypertensionListener = document.getElementById('hypertensionListener').addEventListener("click", function() {
        populateHeaders(clinicalmeasureconditions[1].resource.clinicalMeasures)
      }, false)


    })
}
