import os
import http.client
import xml.etree.ElementTree as ET
from operator import itemgetter
from datetime import date as dateName

# Navigation bar
# Centering if odd number of games
# Pictures
# Link videos
# Host on server 
# Styling, different colors, blue, dark blue
# Back button, next button

# Tweak shadow
# display: inline-block;
# width: 20%;
# height: 200px;
# background-color: #000;
# border: 0px solid #00ffbc;
# box-shadow: 12px 16px 24px #000;
# border-radius: 6px;
# margin-left: 9.5%;
# margin-bottom: 5%;

# NFL Official
# Key: 5dbyzszswdjteg4ab663g837
# NFL Classic
# Key: zvqbcxphvmpgyndjpqf2y27c

class Converter():

    standings = {
    "Arizona Cardinals": [0, 0, 0],
    "Atlanta Falcons": [0, 0, 0],
    "Baltimore Ravens": [0, 0, 0],
    "Buffalo Bills": [0, 0, 0],
    "Carolina Panthers": [0, 0, 0],
    "Chicago Bears": [0, 0, 0],
    "Cincinnati Bengals": [0, 0, 0],
    "Cleveland Browns": [0, 0, 0],
    "Dallas Cowboys": [0, 0, 0],
    "Denver Broncos": [0, 0, 0],
    "Detroit Lions": [0, 0, 0],
    "Green Bay Packers": [0, 0, 0],
    "Houston Texans": [0, 0, 0],
    "Indianapolis Colts": [0, 0, 0],
    "Jacksonville Jaguars": [0, 0, 0],
    "Kansas City Chiefs": [0, 0, 0],
    "Los Angeles Chargers": [0, 0, 0],
    "Los Angeles Rams": [0, 0, 0],
    "Miami Dolphins": [0, 0, 0],
    "Minnesota Vikings": [0, 0, 0],
    "New England Patriots": [0, 0, 0],
    "New Orleans Saints": [0, 0, 0],
    "New York Giants": [0, 0, 0],
    "New York Jets": [0, 0, 0],
    "Oakland Raiders": [0, 0, 0],
    "Philadelphia Eagles": [0, 0, 0],
    "Pittsburgh Steelers": [0, 0, 0],
    "San Diego Chargers": [0, 0, 0],
    "San Francisco 49ers": [0, 0, 0],
    "Seattle Seahawks": [0, 0, 0],
    "St. Louis Rams": [0, 0, 0],
    "Tampa Bay Buccaneers": [0, 0, 0],
    "Tennessee Titans": [0, 0, 0],
    "Washington Redskins": [0, 0, 0]
    }

    def __init__(self, startYear, type, week):
        self.startYear = startYear
        self.type = type
        self.week = week

    def makeHTMLTemplate(self):
        if self.type == "PST":
            if self.week == 1:
                title = "WILD CARD ROUND"
            elif self.week == 2:
                title = "DIVISIONAL ROUND"
            elif self.week == 3:
                title = "CONFERENCE CHAMPIONSHIPS"
            else:
                title = "SUPER BOWL"
        else:
            title = "WEEK " + str(self.week)

        file = open("HTML/" + str(self.startYear) + "/" + self.type + "/scorecard" + str(self.week) + ".html", "w")
        text = """<!DOCTYPE html>
<html>
    <head>
        <link href='https://fonts.googleapis.com/css?family=Roboto:400,100,300' rel='stylesheet' type='text/css'>
        <link href='https://fonts.googleapis.com/css?family=Oswald' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="/Users/ishaan/Coding/Projects/NFL_Website/CSS/scorecards.css">
    </head>
    <body>
        <div class="title">""" + str(self.startYear) +  """ NFL """ + str(title) + """</div>
        """
        for i in range(8):
            text += """<div class="row">
            <div class="card">
                <div class="date">Sun, 16/12</div>
                <div class="result">Final</div>
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty"></div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty"></div>  
                <div class="table">
                    <div class="scoring-header">
                        <ul>
                            <li class="team-name">Team</li>
                            <li class='quarter'>1</li>
                            <li class="quarter">2</li>
                            <li class="quarter">3</li>
                            <li class="quarter">4</li>
                            <li class="quarter-hidden">OT</li>
                            <li class="quarter">T</li>
                        </ul>
                    </div>
                    <div class="scoring">
                        <ul>
                            <li class="team-name1">Chicago Bears</li>
                            <li class='quarter1'>17</li>
                            <li class="quarter1">17</li>
                            <li class="quarter1">7</li>
                            <li class="quarter1">13</li>
                            <li class="quarter-hidden">OT</li>
                            <li class="quarter1">54</li>
                        </ul>
                    </div>
                    <div class="scoring">
                        <ul>
                            <li class="team-name2">Green Bay Packers</li>
                            <li class='quarter2'>17</li>
                            <li class="quarter2">17</li>
                            <li class="quarter2">6</li>
                            <li class="quarter2">13</li>
                            <li class="quarter-hidden">OT</li>
                            <li class="quarter2">53</li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="card">
                <div class="date">Sun, 16/12</div>
                <div class="result">Final</div>
                <div class="score1">54</div>
                <div class="score2">53</div>
                <div class="dash">-</div>
                <div class="name1">Chicago Bears</div>
                <div class="name2">Green Bay Packers</div>
                <div class="empty"></div>
                <div class="record1">(16 - 0)</div>
                <div class="record2">(15 - 1)</div> 
                <div class="empty"></div>  
                <div class="table">
                    <div class="scoring-header">
                        <ul>
                            <li class="team-name">Team</li>
                            <li class='quarter'>1</li>
                            <li class="quarter">2</li>
                            <li class="quarter">3</li>
                            <li class="quarter">4</li>
                            <li class="quarter-hidden">OT</li>
                            <li class="quarter">T</li>
                        </ul>
                    </div>
                    <div class="scoring">
                        <ul>
                            <li class="team-name1">Chicago Bears</li>
                            <li class='quarter1'>17</li>
                            <li class="quarter1">17</li>
                            <li class="quarter1">7</li>
                            <li class="quarter1">13</li>
                            <li class="quarter-hidden">OT</li>
                            <li class="quarter1">54</li>
                        </ul>
                    </div>
                    <div class="scoring">
                        <ul>
                            <li class="team-name2">Green Bay Packers</li>
                            <li class='quarter2'>17</li>
                            <li class="quarter2">17</li>
                            <li class="quarter2">6</li>
                            <li class="quarter2">13</li>
                            <li class="quarter-hidden">OT</li>
                            <li class="quarter2">53</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
            """
        file.write(text)
        file.close()        
    
    def makeInfo(self):
        conn = http.client.HTTPSConnection("api.sportradar.us")
        conn.request("GET", "/nfl/official/trial/v5/en/games/" + str(self.startYear) + "/" + self.type + "/" + str(self.week) + "/schedule.xml?api_key=5dbyzszswdjteg4ab663g837")
        res = conn.getresponse()
        data = res.read()
        text = data.decode("utf-8")
        output = open("Schedules/" + str(self.startYear) + "/" + self.type + "/schedule" + str(self.week) + ".xml", "w")
        output.write(text)
        output.close()

    def makeInfo2(self):
        conn = http.client.HTTPSConnection("api.sportradar.us")
        conn.request("GET", "/nfl-t1/" + str(self.startYear) + "/" + self.type + "/" + str(self.week) + "/boxscore.xml?api_key=zvqbcxphvmpgyndjpqf2y27c")
        res = conn.getresponse()
        data = res.read()
        text = data.decode("utf-8")
        output = open("Schedules/" + str(self.startYear) + "/" + self.type + "/schedule" + str(self.week) + ".xml", "w")
        output.write(text)
        output.close()

    def appendInfo(self, games):
        output = open("HTML/" + str(self.startYear) + "/" + self.type + "/scorecard" + str(self.week) + ".html", "a")
        text = ''
        count = 0
        for i in games:
            text += ' ' * 8 + '<div class="hiddenName">' + i[0][0] + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenName">' + i[1][0] + '</div>\n'
            count += 2
        for i in range(count, 32):
            text += ' ' * 8 + '<div class="hiddenName">None</div>\n'
        count = 0
        for i in games:
            text += ' ' * 8 + '<div class="hiddenScore">' + str(i[0][1]) + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenScore">' + str(i[1][1]) + '</div>\n'
            count += 2
        for i in range(count, 32):
            text += ' ' * 8 + '<div class="hiddenScore">None</div>\n'
        count = 0
        for i in games:
            for j in i[0][2]:
                text += ' ' * 8 + '<div class="hiddenPoint">' + str(j) + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenPoint">STOP</div>\n'
            for j in i[1][2]:
                text += ' ' * 8 + '<div class="hiddenPoint">' + str(j) + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenPoint">STOP</div>\n'
            count += 2
        for i in range(count, 32):
            text += ' ' * 8 + '<div class="hiddenPoint">None</div>\n'
        count = 0
        for i in games:
            text += ' ' * 8 + '<div class="hiddenTime">' + str(i[2][0]) + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenTime">' + str(i[2][0]) + '</div>\n'
            count += 2
        for i in range(count, 32):
            text += ' ' * 8 + '<div class="hiddenTime">None</div>\n'
        count = 0
        for i in games:
            text += ' ' * 8 + '<div class="hiddenDate">' + i[2][1] + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenDate">' + i[2][1] + '</div>\n'
            count += 2
        for i in range(count, 32):
            text += ' ' * 8 + '<div class="hiddenDate">None</div>\n'
        for i in Converter.standings:
            text += ' ' * 8 + '<div class="hiddenStanding1">' + i + '</div>\n'
        for i in Converter.standings:
            text += ' ' * 8 + '<div class="hiddenStanding2">' + str(Converter.standings[i][0]) + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenStanding2">' + str(Converter.standings[i][1]) + '</div>\n'
            text += ' ' * 8 + '<div class="hiddenStanding2">' + str(Converter.standings[i][2]) + '</div>\n'
        text += ' ' * 8 + '<script type="text/javascript" src="/Users/ishaan/Coding/Projects/NFL_Website/JS/scorecards.js"></script>'

        output.write(text)
        output.close()

        if (self.type == "PRE" and self.week == 4) or (self.type == "PST" and self.week == 4):
            for i in Converter.standings:
                index = 0
                for j in Converter.standings[i]:
                    Converter.standings[i][index] = 0
                    index += 1

    def convertDate(self, date):
        dayMapping = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu", 4: "Fri", 5: "Sat", 6: "Sun"}
        date = list(date)
        year1 = date[0:4]
        newYear = ''.join(year1)
        month = date[5:8]
        day = date[8:10]
        newDate = day + month
        newDate.remove('-')
        newDate.insert(2, '/')
        var1 = int(newYear)
        var2 = int(''.join(month[0:2]))
        var3 = int(''.join(day))
        dayOfWeek = dayMapping[dateName(var1, var2, var3).weekday()]
        value = 365 * int(newYear) + 10 * int(newDate[0]) + int(newDate[1]) + 30 * (10 * int(newDate[3]) + int(newDate[4]) - 1)
        newDate = ''.join(newDate)
        return value, dayOfWeek + ", " + newDate

    def convertInfo(self):
        self.makeHTMLTemplate()
        games = []
        tree = ET.parse("Schedules/" + str(self.startYear) + "/" + self.type + "/schedule" + str(self.week)+ ".xml")
        for elem in tree.iter():
            if elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}game": 
                date = elem.attrib["scheduled"]
                value, newDate = self.convertDate(date)
                records = []
                home = []
                away = []
                homePointsByQuarter = []
                awayPointsByQuarter = []
                count = 0
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}home":
                home.append(elem.attrib['name'])
                records.append(elem.attrib['name'])
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}away":
                away.append(elem.attrib['name'])
                records.append(elem.attrib['name'])
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}scoring":
                home.append(int(elem.attrib['home_points']))
                away.append(int(elem.attrib['away_points']))
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}quarter":
                homePointsByQuarter.append(int(elem.attrib['home_points']))
                awayPointsByQuarter.append(int(elem.attrib['away_points']))
                count += 1
                if count == 4:
                    homeSum = sum(homePointsByQuarter)
                    homePointsByQuarter.append(homeSum)
                    home.append(homePointsByQuarter)
                    awaySum = sum(awayPointsByQuarter)
                    awayPointsByQuarter.append(awaySum)
                    away.append(awayPointsByQuarter)
                    games.append([home, away, [value, newDate]])

                    if homeSum > awaySum:
                        Converter.standings[records[0]][0] += 1
                        Converter.standings[records[1]][1] += 1
                    elif homeSum < awaySum:
                        Converter.standings[records[0]][1] += 1
                        Converter.standings[records[1]][0] += 1    
                    else:
                        Converter.standings[records[0]][2] += 1
                        Converter.standings[records[1]][2] += 1
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/premium/schedule-v5.0.xsd}overtime":
                home[2].append(int(elem.attrib['home_points']))
                away[2].append(int(elem.attrib['away_points']))
                homeSum = sum(home[2])
                awaySum = sum(away[2])
                home[2][4] += int(elem.attrib['home_points'])
                away[2][4] += int(elem.attrib['away_points'])
                if homeSum > awaySum:
                    Converter.standings[records[0]][0] += 1
                    Converter.standings[records[1]][1] += 1
                    Converter.standings[records[0]][2] -= 1
                    Converter.standings[records[1]][2] -= 1
                elif homeSum < awaySum:
                    Converter.standings[records[0]][1] += 1
                    Converter.standings[records[1]][0] += 1
                    Converter.standings[records[0]][2] -= 1
                    Converter.standings[records[1]][2] -= 1        
                else:
                    pass

        games.sort(key = itemgetter(2))
        self.appendInfo(games)
    
    def convertInfo2(self):
        self.makeHTMLTemplate()
        games = []
        tree = ET.parse("Schedules/" + str(self.startYear) + "/" + self.type + "/schedule" + str(self.week) + ".xml")
        tracker = 0
        tracker2 = 0
        tracker3 = 0
        tracker4 = 0
        for elem in tree.iter():
            if elem.tag == "{http://feed.elasticstats.com/schema/nfl/boxscore-v1.0.xsd}game": 
                date = elem.attrib["scheduled"]
                value, newDate = self.convertDate(date)
                records = []
                home = []
                away = []
                homePointsByQuarter = []
                awayPointsByQuarter = []
                count = 0
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/boxscore-v1.0.xsd}team":
                try:
                    message = elem.attrib['market']
                    message += " " + elem.attrib['name']
                    if tracker == 0:
                        home.append(message)
                        tracker = 1
                    else:
                        away.append(message)
                        tracker = 0
                    records.append(message)
                except KeyError:
                    pass
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/boxscore-v1.0.xsd}scoring":
                if tracker2 == 0:
                    home.append(int(elem.attrib['points']))
                    tracker2 = 1
                else:
                    away.append(int(elem.attrib['points']))
                    tracker2 = 0
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/boxscore-v1.0.xsd}quarter":
                if tracker3 == 0:
                    homePointsByQuarter.append(int(elem.attrib['points']))
                    tracker3 = 1
                else:
                    awayPointsByQuarter.append(int(elem.attrib['points']))
                    tracker3 = 0
                    count += 1
                    if count == 4:
                        homeSum = sum(homePointsByQuarter)
                        homePointsByQuarter.append(homeSum)
                        home.append(homePointsByQuarter)
                        awaySum = sum(awayPointsByQuarter)
                        awayPointsByQuarter.append(awaySum)
                        away.append(awayPointsByQuarter)
                        games.append([home, away, [value, newDate]])

                        if homeSum > awaySum:
                            Converter.standings[records[0]][0] += 1
                            Converter.standings[records[1]][1] += 1
                        elif homeSum < awaySum:
                            Converter.standings[records[0]][1] += 1
                            Converter.standings[records[1]][0] += 1    
                        else:
                            Converter.standings[records[0]][2] += 1
                            Converter.standings[records[1]][2] += 1
            elif elem.tag == "{http://feed.elasticstats.com/schema/nfl/boxscore-v1.0.xsd}overtime":
                if tracker4 == 0:
                    home[2].append(int(elem.attrib['points']))
                    homeSum = sum(home[2])
                    home[2][4] += int(elem.attrib['points'])
                    tracker4 = 1
                else:
                    away[2].append(int(elem.attrib['points']))
                    awaySum = sum(away[2])
                    away[2][4] += int(elem.attrib['away_points'])
                    tracker4 = 0

                    if homeSum > awaySum:
                        Converter.standings[records[0]][0] += 1
                        Converter.standings[records[1]][1] += 1
                        Converter.standings[records[0]][2] -= 1
                        Converter.standings[records[1]][2] -= 1
                    elif homeSum < awaySum:
                        Converter.standings[records[0]][1] += 1
                        Converter.standings[records[1]][0] += 1
                        Converter.standings[records[0]][2] -= 1
                        Converter.standings[records[1]][2] -= 1        
                    else:
                        pass
        
        games.sort(key = itemgetter(2))
        self.appendInfo(games)

def makeCalls(startYear, endYear, switch):
    while startYear <= endYear:
        if startYear <= switch:
            type = "PRE"
            week = 1
            while week <= 4:
                converter = Converter(startYear, type, week)
                converter.makeInfo2()
                converter.convertInfo2()  
                week += 1
            type = "REG"
            week = 1
            while week <= 17:
                converter = Converter(startYear, type, week)
                converter.makeInfo2()
                converter.convertInfo2()  
                week += 1
            type = "PST"
            week = 1
            while week <= 4:
                converter = Converter(startYear, type, week)
                converter.makeInfo2()
                converter.convertInfo2()  
                week += 1
        else:
            type = "PRE"
            week = 1
            while week <= 4:
                converter = Converter(startYear, type, week)
                converter.makeInfo()
                converter.convertInfo()  
                week += 1
        
            type = "REG"
            week = 1
            while week <= 17:
                converter = Converter(startYear, type, week)
                converter.makeInfo()
                converter.convertInfo()  
                week += 1
            type = "PST"
            week = 1
            while week <= 4:
                converter = Converter(startYear, type, week)
                converter.makeInfo()
                converter.convertInfo()  
                week += 1
        startYear += 1

def main():
    makeCalls(2012, 2012, 2015)

if __name__ == '__main__':
    main()