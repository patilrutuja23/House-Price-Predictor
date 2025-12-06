function getBathValue() {
  const radios = document.getElementsByName('uiBathrooms');
  for (let i = 0; i < radios.length; i++) {
    if (radios[i].checked) return Number(radios[i].value);
  }
  return -1;
}

function getBHKValue() {
  const radios = document.getElementsByName('uiBHK');
  for (let i = 0; i < radios.length; i++) {
    if (radios[i].checked) return Number(radios[i].value);
  }
  return -1;
}

function setLoading(on) {
  const spinner = document.getElementById('loadingSpinner');
  const btn = document.getElementById('estimateBtn');
  const resultCard = document.getElementById('resultCard');
  if (on) {
    spinner.hidden = false;
    btn.disabled = true;
    resultCard.hidden = true;
  } else {
    spinner.hidden = true;
    btn.disabled = false;
  }
}

function onClickedEstimatePrice() {
  console.log('Estimate price button clicked');
  const sqftEl = document.getElementById('uiSqft');
  const bhk = getBHKValue();
  const bathrooms = getBathValue();
  const locationEl = document.getElementById('uiLocations');
  const estPriceEl = document.getElementById('uiEstimatedPrice');

  const sqft = parseFloat(sqftEl.value);
  const location = locationEl.value;

  if (!sqft || sqft <= 0) { alert('Please enter a valid area (sqft).'); return; }
  if (!location) { alert('Please choose a location.'); return; }

  const url = '/api/predict_home_price';
  setLoading(true);

  $.post(url, {
    total_sqft: sqft,
    bhk: bhk,
    bath: bathrooms,
    location: location
  }, function(data, status) {
    setLoading(false);
    if (data && data.estimated_price !== undefined) {
      estPriceEl.innerHTML = data.estimated_price.toString() + ' Lakh';
      const resultCard = document.getElementById('resultCard');
      resultCard.hidden = false;
      resultCard.classList.remove('flash');
      // trigger reflow to restart animation
      void resultCard.offsetWidth;
      resultCard.classList.add('flash');
    } else {
      alert('Unexpected response from server');
    }
  }).fail(function(xhr, status, error) {
    setLoading(false);
    alert('Request failed: ' + (xhr.responseJSON && xhr.responseJSON.message ? xhr.responseJSON.message : error || status));
    console.error('Error:', status, error);
  });
}

function onPageLoad() {
  console.log('document loaded');
  const url = '/api/get_location_names';
  $.get(url, function(data, status) {
    console.log('got response for get_location_names request');
    if (data && data.locations) {
      const locations = data.locations;
      const uiLocations = document.getElementById('uiLocations');
      uiLocations.innerHTML = '<option value="" disabled selected>Choose a Location</option>';
      locations.forEach(function(loc) {
        const opt = new Option(loc, loc);
        uiLocations.appendChild(opt);
      });
      console.log('Loaded ' + locations.length + ' locations');
    }
  }).fail(function(xhr, status, error) {
    console.error('Failed to load locations:', status, error);
    alert('Could not load location names from server. Please refresh the page.');
  });
}

window.onload = onPageLoad;