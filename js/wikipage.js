let baseUrl = 'https://en.wikipedia.org/wiki/';
let wikipediaUrls = [
	"2017_Equifax_data_breach",
	"Snake_detection_theory",
	"Attempted_theft_of_George_Washington's_skull",
	"Extraterrestrial_real_estate",
	"Hiroo_Onoda",
	"Waldi",
	"Hamburger_University",
	"Digital_dark_age",
	"Tenevil",
	"Operation_Flagship",
	"Death_of_Garry_Hoy",
	"Hyatt_Regency_walkway_collapse",
	"Coffee_enema",
	"William_McGonagall",
	"List_of_obsolete_units_of_measurement",
	"Toki_Pona",
	"Andy_(goose)",
	"Adolf_Hitler_and_vegetarianism",
	"Emerald_Tablet",
	"Champawat_Tiger",
	"21_grams_experiment",
	"Project_Pigeon",
	"Stubbs_(cat)",
	"Louis_Wain",
	"C/2022_E3_(ZTF)",
	"Tulip_mania",
	"Omagh_bombing",
	"Polar_bear_jail",
	"Aeroflot_Flight_593",
	"Maternal_insult",
	"Bikini_Atoll",
	"Romanesco_broccoli",
	"Tree_(installation)",
	"Gay_Nineties",
	"The_Thing_(listening_device)",
	"HitchBOT",
	"Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo",
	"Dishwasher_salmon",
	"Exploding_animal",
	"Death_by_coconut",
	"Breast-shaped_hill",
	"Mary_Toft",
	"Mozart_and_scatology",
	"Year_2038_problem",
	"1945_Empire_State_Building_B-25_crash",
	"Extreme_ironing",
	"Time_flies_like_an_arrow;_fruit_flies_like_a_banana",
	"Lawsuits_against_the_Devil",
	"Guy_Fawkes",
	"The_Mad_Pooper",
	"List_of_games_that_Buddha_would_not_play",
	"Green_Boots",
	"Mitt_Romney_dog_incident",
	"Charles_Ingram",
	"Bone_Wars",
	"Homo_floresiensis",
	"Fairview_Lawn_Cemetery",
	"Bongcloud_Attack",
	"Pumpkin_chucking",
	"George_H._W._Bush_vomiting_incident",
	"Antipope",
	"Erfurt_latrine_disaster",
	"Anophthalmus_hitleri",
	"Intracolonic_explosion",
	"Phantom_pain",
	"Magellan_expedition",
	"Depths_of_Wikipedia",
	"Z-Library",
	"Pierrot",
	"Jan_Smit_(paleontologist)",
	"Whitney_Chewston",
	"Blobject",
	"Queening",
	"Straw_man",
	"File:Samoyed-and-teddy-bear.jpg",
];

document.addEventListener('DOMContentLoaded', function () {
	function getRandomUrlNotInStorage() {
		var shuffledUrls = wikipediaUrls.slice();
		var storedArticles = JSON.parse(localStorage.getItem('visitedArticles')) || [];

		// Shuffle the array to get a random order
		for (let i = shuffledUrls.length - 1; i > 0; i--) {
			const j = Math.floor(Math.random() * (i + 1));
			[shuffledUrls[i], shuffledUrls[j]] = [shuffledUrls[j], shuffledUrls[i]];
		}

		var randomUrl = shuffledUrls.find(url => !storedArticles.includes(url));

		// If all URLs have been visited, reset the storage and try again
		if (!randomUrl) {
			storedArticles = [];
			randomUrl = shuffledUrls[0];
		}

		// Add the current URL to the visited articles
		storedArticles.push(randomUrl);
		localStorage.setItem('visitedArticles', JSON.stringify(storedArticles));

		return randomUrl;
	}

	// Function to set iframe source to a random Wikipedia URL not in local storage
	function setRandomPage() {
		var randomUrl = getRandomUrlNotInStorage();
		document.getElementById('wikipedia-page').href = randomUrl;
	}

	// Add click event listener to the iframe
	document.getElementById('wikipedia-page').addEventListener('click', function () {
		setRandomPage();
	});

	// Set initial random page on page load
	setRandomPage();
});