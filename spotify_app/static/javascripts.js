

// Reveal the rest of a caption.
function revealCaption(postID) {
    document.querySelector('#moreDots').style.display = 'none';
    document.querySelector('#moreCaption').style.display = 'inline';
  }

// Create a bar chart. First example in docs.
const ctx = document.getElementById('myChart');

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: '# of Votes',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});

