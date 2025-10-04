<!DOCTYPE html>
<html>
<head>
  <toc: true
title>Quotes</toc: true
title>
</head>
<body>
  <h1>Random Quotes</h1>
  This page displays 10 random Quotes from my personal repository of Quotes I have collected (and continue to collect) over the years. Sadly, most of them do not have any citations. I will eventually try to write a script that finds the authors of the same.<br><br>
  These have been collected from books, websites, movies and music and each of them has taught me something over the years. Here I am sharing them with you, dear visitor :)<br><br>


  <button onclick="showRandomPoints()">Show Random Points</button>
  <ul id="pointsList"></ul>

  <script>
    function showRandomPoints() {
      fetch('../quotes')
        .then(response => response.text())
        .then(text => {
          const points = extractPoints(text);
          const randomPoints = getRandomPoints(points, 10);
          displayPoints(randomPoints);
        })
        .catch(error => {
          console.error('Error:', error);
        });
    }

    function extractPoints(text) {
    const lines = text.split('<li>');
      const points = lines.filter(line => line.trim());
            return points.map(point => point.trim().replace('<p>', '').replace('</p>', '').replace('</li>',''));
    }

    function getRandomPoints(points, num) {
      const randomPoints = [];
      const availableIndices = Array.from(Array(points.length).keys());
      for (let i = 0; i < num; i++) {
        const randomIndex = Math.floor(Math.random() * availableIndices.length);
        const pointIndex = availableIndices.splice(randomIndex, 1)[0];
        randomPoints.push(points[pointIndex]);
      }
      return randomPoints;
    }

    function displayPoints(points) {
      const pointsList = document.getElementById('pointsList');
      pointsList.innerHTML = '';
      points.forEach(point => {
        const li = document.createElement('li');
        li.textContent = point;
        pointsList.appendChild(li);
      });
    }
  </script>
</body>
</html>



