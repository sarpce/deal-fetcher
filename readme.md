## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/sarpce/deal-fetcher.git
   cd deal-fetcher
   ```

2. **Install dependencies:**

   Make sure you have Python installed. Then, install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

3. **Download ChromeDriver:**

   Do this and place the driver.exe in util folder: https://youtu.be/NB8OceGZGjA?t=190

## Usage

1. **Configure JSON file:**

   Edit the `config.json` file to choose the stores and GPUs you are interested in. Use the keyword 'yes' to select them.

   ```json
   {
     "stores": {
       "store1": "yes",
       "store2": "no"
     },
     "gpus": {
       "gpu1": "yes",
       "gpu2": "no"
     }
   }
   ```

2. **Run the tool:**

   Go to the `scripts` folder and run `main.py` to start fetching deals:

   ```sh
   cd scripts
   python main.py
   ```
3. **See the results:**

    Open up prices.html, see the retrieved prices and access the links.<br>  
    ![](https://i.imgur.com/QZONbSQ.png)<br>
    
## Notes
