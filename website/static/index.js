function deleteScreen(screenId) {
  fetch("/delete-screen", {
    method: "POST",
    body: JSON.stringify({ screenId: screenId }),
  }).then((_res) => {
    window.location.href = "/itinerary-settings";
  });
}

function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function rememberId(screenId) {
  fetch("/remember-id", {
    method: "POST",
    body: JSON.stringify({ screenId: screenId }),
  }).then((_res) => {
    window.location.href = "/service-time";
  });
}
