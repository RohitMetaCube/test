<b>Step 1:</b> Install the required softwares.<br>
1. Python 2.7<br>
2. MongoDB (preferably > 3.0, current ones have 2.4)<br><br>

<b>Step 2:</b> Get the source code repository form github.<br>
<b>2.1:</b> <i>git clone https://github.com/Crawlers.git</i><br><br>


I am assuming that the directory of the source code will be called <i>$CRAWLER_HOME</i><br><br>

<b>Step 3:</b> Installing pip (Version 8.1.1) (I have done it through apt-get other package managers can also be used)<br>
<b>3.1:</b> <i>sudo apt-get install python-pip python-dev gfortran libatlas-base-dev build-essential libxml2-dev libxslt1-dev zlib1g-dev</i><br>
<b>3.2:</b> <i>sudo pip install --upgrade pip</i><br> 
<b>3.3:</b> <i>sudo pip install --upgrade virtualenv</i><br><br>

Test it using <i>pip -V</i> which shows the version of the pip installation<br><br>

<b>Step 4:</b> Installing pip-tools for dependency management<br>
<b>4.1:</b> <i>sudo pip install pip-tools</i><br><br>

<b>Step 5:</b> Downgrade PIP to 8.1.1<br>
<b>5.1:</b> <i>sudo pip install --upgrade pip==8.1.1</i><br><br> 

<b>Step 6:</b> Install crawler specific requirements<br>

<b>6.1:</b><i>cd $CRAWLER_HOME/linkedin_crawler</i><br>

<b>6.2:</b> <i>sudo pip install -r requirements.in</i><br><br>


<b>Step 7:</b> Install Web Driver<br><br>

<i>You can pick any one of them<i><br><br>

<b>7.1:</b> <i>Chrome Driver</i><br>

curl -O http://chromedriver.storage.googleapis.com/2.30/chromedriver_linux64.zip<br>
unzip chromedriver_linux64.zip<br>
rm chromedriver_linux64.zip<br>
chmod +x chromedriver<br>
cp chromedriver /usr/local/bin/
<br><br>

<b>7.2:</b> <i>Mozilla Driver</i><br>

wget https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz<br>
tar -xvzf geckodriver-v0.11.1-linux64.tar.gz<br>
rm geckodriver-v0.11.1-linux64.tar.gz<br>
chmod +x geckodriver<br>
cp geckodriver /usr/local/bin/<br>
<br><br>


<b>Step 8:</b> <i>Install Selenium Library</i><br>

Since Selenium2Library has some dependencies for selenium library, you need to install selenium library. The easy way of installing selenium library is to use pip. You can use the following command to install selenium.
pip install -U selenium

<br><br>

<b>Step 9:</b> <i>Add user profile urls in ~HOME/dataset/profile_links.csv file</i><br><br>

<b>Step 10:</b> <i>Run Crawler</i><br>

<div>python crawler.py</div>


