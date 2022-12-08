function submitCreateExerciseForm(e: Event) {
  e.preventDefault();
  if (!e.target) {
    return;
  }
  const formData = new FormData(e.target as HTMLFormElement);

  fetch('/workouts/exercises/', {
    method: 'POST',
    body: formData,
    credentials: 'same-origin',
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const exerciseList = document.getElementById('id_exercises_list');
      if (!exerciseList) {
        throw Error('Exercise list not found');
      }
      const newListItem = document.createElement('li');
      newListItem.textContent = data.name;
      exerciseList.appendChild(newListItem);
    })
    .catch((e) => {
      console.log(e);
    });
  // const request = new XMLHttpRequest();
  // request.open('POST', '/workouts/exercises/', false);
  // request.send(formData);
}

const createExercisesForm = document.getElementById('id_create_exercise_form');

if (createExercisesForm) {
  createExercisesForm.addEventListener('submit', submitCreateExerciseForm);
}
