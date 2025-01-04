

const limitSelect = document.getElementById('limit');
const movieSelect = document.getElementById('movie');
const summonButton = document.getElementById('summon');
const quoteDiv = document.getElementById('quote-box')
const copyButton = document.getElementById('copy');


// Functions 

function displayError(message) {
    quoteDiv.innerHTML = '';
    quoteDiv.innerHTML = `<p class="error">${message}</p>`;
}

function displayQuotes(quotes) {
    // Ensure quotes is always an array
    if (!Array.isArray(quotes)) quotes = [quotes];
    quoteDiv.innerHTML = quotes.map(quote => `<p>${quote.quote}</p>`).join('');
}

async function fetchQuotes() {
    quoteDiv.innerHTML = '';

    const limit = limitSelect.value;
    const movie = movieSelect.value;

    let url = `/api/quotes/${limit}`;
    if (movie) url += `/${encodeURIComponent(movie)}`

    try {
        const response = await fetch(url)
        if (!response.ok) {
            if (response.status === 404){
                displayError('No quotes found. Try reducing the limit or choosing another movie.');
            } else if (response.status === 500) {
                displayError('Well, I must have fucked up somewhere . . . Sorry.');
            } else {
                displayError('Unexpected error.');
            }
            return;
        }

        const quotes = await response.json();
        displayQuotes(quotes);
    }
    catch(error) {
        displayError('Failed to summon quotes. The Mad Titan is probably not in the mood. Try again?');
    }

}

// Event listener for copy button

copyButton.addEventListener('click', () => {
    let quoteText = quoteDiv.innerText.trim();
    if (quoteText)
        navigator.clipboard.writeText(quoteText).then(() => {
    alert('Copied!')
}); else {
    alert('No quote to copy.');
}
})

// Fetch and display random quote on page load

async function fetchRandomQuote() {
    try {
        const response = await fetch('/api/quotes/1');
        if (response.ok) {
            const quote = await response.json();
            displayQuotes(quote);
        }
        else {
            displayError('Something went wrong. Try again.');
        }
    }
    catch(error) {
        displayError('An error occurred while fetching.')
    }
}

summonButton.addEventListener('click', fetchQuotes);

fetchRandomQuote();

