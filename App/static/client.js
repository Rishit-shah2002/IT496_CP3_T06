// Javascript code that runs on the client side
// To send the request to backend and update the view accordingly
team1 = null
team2 = null
venue = null
loadingView = document.getElementById('loadingView')
resultView = document.getElementById('resultView')
errorView = document.getElementById('errorView')

function showErrorMessage(message) {
  errorView.innerHTML = message
  errorView.style.display = 'block'
}

document.getElementById('team1Select').addEventListener('change', (event) => {
  team1 = event.target.value
  if (team1 == team2 && team1 != 0 && team1 != null) {
    showErrorMessage('Team 1 and Team 2 should not be same!!')
  }
})

document.getElementById('team2Select').addEventListener('change', (event) => {
  team2 = event.target.value
  if (team1 == team2 && team2 != 0 && team2 != null) {
    showErrorMessage('Team 1 and Team 2 should not be same!!')
  }
})

document.getElementById('venueSelect').addEventListener('change', (event) => {
  venue = event.target.value
})

async function sendRequest() {

  // hide previou results and show loading
  // loadingView.style.display = 'block'
  resultView.style.display = 'none'
  loadingView.style.display = 'block'
  errorView.style.display = 'none'

  // verify the inputs
  if ((team1 == "0" || team1 == null) || (team2 == "0" || team2 == null) || (venue == "0" || venue == null)) {
    loadingView.style.display = 'none'
    showErrorMessage("Please select all the inputs!!")
    return
  }

  if (team1 == team2) {
    loadingView.style.display = 'none'
    showErrorMessage("Team 1 and Team 2 should not be same!!")
    return
  }

  // send the request and get the response
  const host = window.location.protocol + '//' + window.location.host;
  const response = await fetch(`${host}/predict`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ team1, team2, venue })
  })

  let json = await response.json()

  // update the view accordingly
  document.getElementById('winnerTeam').innerHTML = json['winner']
  document.getElementById('winnerTeamSub').innerHTML = json['winner']
  document.getElementById('winnerProbability').innerHTML = json['winningProbability']
  team1List = json['team1']
  team2List = json['team2']
  for (i = 1; i <= 11; i++) {
    document.getElementById('team1' + i + 'name').innerHTML = team1List[i-1]['name']
    document.getElementById('team2' + i + 'name').innerHTML = team2List[i-1]['name']
    document.getElementById('team1' + i + 'role').innerHTML = team1List[i-1]['role']
    document.getElementById('team2' + i + 'role').innerHTML = team2List[i-1]['role']
  }

  // show results and hide loading
  loadingView.style.display = 'none'
  resultView.style.display = 'block'
}