
# Thanos Ipsum &mdash; A  website and API for Thanos Quotes

> Fine, I'll do it myself.
>
> &mdash; <cite>Thanos</cite>

Thanos Ipsum is a website and API that delivers iconic quotes from Marvel's beloved supervillain. A quote generator with a galactic touch that you could
embed as placeholder text into your apps, prototypes, personal projects, templates, or whatever.

Honestly, there's little chance this would be of use to anyone. 
I made this project to gain experience in full stack web development workflow, albeit at a basic level. But hey, "despise not the days of humble 
beginnings," right? 

Now, back to this thing.

---

## Features 

Features include 
- a Thanos Ipsum website to explore and generate Thanos's quotes
- a fully functional API for accessing Thanos's quotes programmatically 
- an API documentation . . . because every API needs a good one

--- 

## TOC

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [API Endpoints](#api-endpoints)
5. [License](#license)
6. [Contact](#contact)

---

## Getting Started 

I tried to follow best practices in web development and API design. I used tools
that are popular, widely supported, and easy to set up (for my own sanity, lol). So whether you're exploring the website or using the API, setting up and using this project shouldn't cause you any headache.  

---

## Installation

Ensure you have the following installed:

- Python 3.9+
- [PDM](https://pdm-project.org/en/latest)


> [!NOTE]
> I wanted to use poetry for dependency management because, as of this writing and following my philosophy above, poetry is the most popular among the slew of modern Python packaging tools. But python-poetry.org seems to be rejecting traffic from my local network. It might have something to do with Poetry website being blocked by AT&T fiber, per [this Github issue](https://github.com/python-poetry/website/issues/153#issue-2285760763). Luckily, PDM
is also excellent, relatively popualar, and, most important, easy to set up. 

### Steps

1. Clone this repo:
```bash 
git clone https://github.com/jegrami/thanosipsum.git 
# cd into the project dir.
cd thanosipsum
```

2. Install dependencies:
```bash 
pdm install 
```

3. Run the project locally:
```bash 
pdm run uvicorn app:app --reload
```

4. Open the website at localhost:8000/

---

## Usage

### Website

Visit the website and interact with the quote generator. Explore some words of doom from Thanos The Mad Titan.

### API Endpoints

If you're fetching quotes programatically, here are the few endpoints you need 
to know, all *GET*s (see? it doesn't "get" any easier than this):

The base url endpoint is https://thanosipsum.onrender.com/api, and then:

- `GET /quotes`
Fetches all avaialable quotes.
- `GET /quotes/{limit:int}`
Retrieves a specific number of random quotes.
- `GET /quotes/{movie:str}`
Gets all quotes from a given movie.
- `GET /quotes/{limit:int}/{movie:str}`
Retrieves a specific number of quotes from a given movie.

### Example request
```bash
curl https://thanosipsum.onrender.com/api/quotes/3/endgame 
```

Read the full documentation [here](https://thanosipsum.onrender.com/documentation).

## License

This project is under the [MIT License](/LICENSE). You know what that means. 

---

## Contact

* [Website](https://jegrami.com)
* [Email](mailto:jegrami.dev@gmail.com)
* [LinkedIn](https://linkedin.com/in/jeremiah-igrami)
* [X](https://twitter.com/je_grami)


























