<!DOCTYPE html>
<html>
<body>
  <h1>Stock News Alert</h1>
  <p>This Python script sends an SMS message to a designated mobile number with news articles related to a specified stock when the stock price changes by a certain percentage threshold between the previous two days.</p>
  
  <h2>Installation</h2>
  <ol>
    <li>Install Python 3.x from the <a href="https://www.python.org/downloads/">official website</a>.</li>
    <li>Install required packages using pip:
      <ul>
        <li><code>pip install requests</code></li>
        <li><code>pip install twilio</code></li>
      </ul>
    </li>
    <li>Clone this repository to your local machine.</li>
    <li>In the command line, navigate to the project directory and run the command: <code>python stock_news_alert.py</code></li>
  </ol>

  <h2>Configuration</h2>
  <p>Before running the script, you will need to configure several parameters:</p>
  <ul>
    <li><code>STOCK_NAME</code>: The stock symbol for which you want to receive news alerts.</li>
    <li><code>COMPANY_NAME</code>: The name of the company corresponding to the stock symbol.</li>
    <li><code>STOCK_API_KEY</code>: Your Alpha Vantage API key.</li>
    <li><code>NEWS_API_KEY</code>: Your News API key.</li>
    <li><code>TWILIO_SID</code>: Your Twilio account SID.</li>
    <li><code>TWILIO_TOKEN</code>: Your Twilio account token.</li>
    <li><code>MOBILE_NUMBER</code>: The mobile number to which you want to send the SMS alerts.</li>
    <li><code>THRESHOLD</code>: The percentage change threshold that triggers the script to retrieve news articles.</li>
  </ul>
  <p>You can modify these parameters in the script file before running it.</p>

  <h2>Usage</h2>
  <p>Once the script is running, it will retrieve the daily adjusted stock prices for the specified stock from the Alpha Vantage API. If the percentage change in the stock price between the previous two days meets the threshold, the script will retrieve news articles related to the specified company from the News API and send an SMS alert with the three most relevant articles to the designated mobile number using the Twilio API.</p>

</body>
</html>



