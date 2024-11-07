# Country Leaders API Scraper 🌍💼

Welcome to the **Country Leaders API Scraper** project from BeCode! This Python script allows you to scrape data from the public **Country Leaders API** to retrieve information about world leaders, their countries, and more. 🇺🇳✨
The file named wikipedia_scraper.ipynb contains exercise instructions, while the leaders_per_country.json is an example of output file

---

## Features 🚀

- Retrieve data about world leaders and their countries via an easy-to-use API.
- Extract useful information such as the leader's name, country, position, and a feature to scrape through their wikipedia page and get the first paragraph.
- Simple Python script utilizing **requests** to interact with the API and **JSON** for structured data.

---

## Requirements 📦

Before running this project, you'll need to install a few dependencies. These are listed in the `requirements.txt` file.

### How to Install:

1. **Create a Virtual Environment** (Recommended for better project isolation):
   It's a good practice to use a virtual environment to manage your dependencies. Here's how you can set it up:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install the Required Libraries**:
   After activating the virtual environment, run the following command to install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This will install all necessary libraries, including:
   - `requests` (for making HTTP requests to the API)
   - `beautifulsoup` (to scrape and parse html files)

---

## Usage 📖

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/kevinjamotte/wikipedia_scraper.git
   cd wikipedia_scraper
   ```

2. Run the scraper script (e.g., `leaders_scraper.py`) to start retrieving data from the API:

   ```bash
   python3 leaders_scraper.py
   ```


3. The script will fetch data from the API and print or save it in a structured format (such as a JSON file).

---

## Example Output 🎉

Once the script is run, you will retrieve a list of world leaders with their countries and positions. The output might look something like this:

```json
[
    {
        "id": "Q12983",
        "first_name": "Herman",
        "last_name": "None",
        "birth_date": "1947-10-31",
        "death_date": null,
        "place_of_birth": "Etterbeek",
        "wikipedia_url": "https://nl.wikipedia.org/wiki/Herman_Van_Rompuy",
        "start_mandate": "2008-12-30",
        "end_mandate": "2009-11-25",
        "first_paragraph": "Herman Achille graaf Van Rompuy (Etterbeek, 31 oktober 1947) is een Belgische politicus van de christendemocratische partij CD&V. Hij was tussen 30 december 2008 en 25 november 2009 de premier van België en van 1 januari 2010 tot en met 30 november 2014 voorzitter van de Europese Raad, in de media vaak incorrect 'president van Europa' genoemd. Op 19 november 2009 werd bekendgemaakt dat hij was verkozen tot de eerste permanente voorzitter en op 1 maart 2012 werd Van Rompuy met algemene stemmen door de 27 staatshoofden en regeringsleiders van de EU voor een tweede mandaat benoemd. Na deze termijn was hij niet meer herkiesbaar. "
    },
    {
        "id": "Q14989",
        "first_name": "Léon",
        "last_name": "Delacroix",
        "birth_date": "1867-12-27",
        "death_date": "1929-10-15",
        "place_of_birth": "Saint-Josse-ten-Noode",
        "wikipedia_url": "https://nl.wikipedia.org/wiki/L%C3%A9on_Delacroix",
        "start_mandate": "1918-11-21",
        "end_mandate": "1920-11-20",
        "first_paragraph": "Léon Fréderic Gustave Delacroix (Sint-Joost-ten-Node, 27 december 1867 – Baden-Baden, 15 oktober 1929) was een Belgisch katholiek politicus. De Léon Delacroixstraat in Anderlecht en het metrostation Delacroix werden naar hem vernoemd. "
    }
]
```

---

## Contributing 🤝

Feel free to fork this project and submit a pull request with improvements, bug fixes, or new features! I'd love to see your contributions. 😄

---

## License 📝

This project is under no license, feel free to use and tweak it.

---

## Contact 📬

If you have any questions or need help, feel free to reach out via GitHub issues.

---

Thank you for using the Country Leaders API Scraper! Happy coding! 🧑‍💻🌍

---
