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

				var chartDataHyper = {'over systolic':0,'under systolic':0,'over diastolic':0,'under diastolic':0, 'total':0}
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

							if(serviceRequestList[request].resource.measures.systolic > 140){
								chartDataHyper['over systolic'] += 1
							} else {
								chartDataHyper['under systolic'] += 1
							}

							if(serviceRequestList[request].resource.measures.diastolic > 90){
								chartDataHyper['over diastolic'] += 1
							} else {
								chartDataHyper['under diastolic'] += 1
							}
							chartDataHyper['total'] += 1
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

				if(measures[0] === 'systolic'){

					var ctx = document.getElementById('myChart')
					ctx.innerHTML = ''

					var label = []
					var dataset = []

					var label = ['Hypertension Control Systolic <140', 'Hypertension Control Diastolic <90', 'Hypertension Control, <140/90 (18-85 y/o)']
					var totProportion = 1-((chartDataHyper['over systolic'] + chartDataHyper['over diastolic'])/chartDataHyper['total'])
					var sysProportion = chartDataHyper['under systolic'] / chartDataHyper['total']
					var diaProportion = chartDataHyper['under diastolic'] / chartDataHyper['total']
					var dataset = [sysProportion, diaProportion, totProportion]

					var myChart = new Chart(ctx, {
					        type: 'bar',
					        data: {
					            labels: label,
					            datasets: [{
					                label: 'hypertension control',
					                data: dataset,
					                backgroundColor: [
					                    'rgba(255, 99, 132, 0.2)',
					                    'rgba(54, 162, 235, 0.2)',
					                    'rgba(255, 206, 86, 0.2)',
					                    'rgba(75, 192, 192, 0.2)',
					                    'rgba(153, 102, 255, 0.2)',
					                    'rgba(255, 159, 64, 0.2)'
					                ],
					                borderColor: [
					                    'rgba(255, 99, 132, 1)',
					                    'rgba(54, 162, 235, 1)',
					                    'rgba(255, 206, 86, 1)',
					                    'rgba(75, 192, 192, 1)',
					                    'rgba(153, 102, 255, 1)',
					                    'rgba(255, 159, 64, 1)'
					                ],
					                borderWidth: 1
					            }]
					        },
					        options: {
					            scales: {
					                yAxes: [{
					                    ticks: {
					                        beginAtZero: true
					                    }
					                }]
					            }
					        }
					    });
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
