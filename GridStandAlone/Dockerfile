FROM adoptopenjdk/openjdk11:jdk-11.0.11_9-debian-slim
WORKDIR /opt/app

RUN apt-get update
RUN apt-get install -y packagekit-gtk3-module
RUN apt-get install -y wget gnupg2 bzip2 libdbus-glib-1-2 libffi-dev libasound2
RUN apt-get install -y libx11-xcb1 python3-pip
RUN wget https://archive.mozilla.org/pub/firefox/releases/75.0/linux-x86_64/en-US/firefox-75.0.tar.bz2
RUN tar xjf firefox-75.0.tar.bz2
RUN mv firefox /opt/
RUN ln -s /opt/firefox/firefox /usr/bin/firefox
RUN wget https://archive.mozilla.org/pub/firefox/releases/102.0esr/linux-x86_64/es-ES/firefox-102.0esr.tar.bz2
RUN tar xjf firefox-102.0esr.tar.bz2
RUN mv firefox /opt/firefoxesr
RUN ln -s /opt/firefoxesr/firefox /usr/bin/firefoxesr
RUN apt install -y libxtst6 libxt6
WORKDIR /opt/app
# java -jar selenium-server-4.14.0.jar standalone --selenium-manager true
# --selenium-manager true
# java -jar selenium-server-4.14.0.jar --selenium-manager true
# java -Dwebdriver.gecko.driver=/opt/app/ServersJars/geckodriver -jar selenium-server-4.14.0.jar node --hub http://localhost:4444 -browser "browserName=firefox,version=102,maxInstances=5"
# ./selenium-manager --driver-version 0.29.1 --browser-version 75.0 --browser firefox --driver geckodriver
# java -jar selenium-server-4.14.0.jar node --driver-configuration