function submitCreateExerciseForm(e: Event) {
  e.preventDefault();
  if (!e.target) {
    return;
  }
  const formData = new FormData(e.target as HTMLFormElement);

  const request = new XMLHttpRequest();
  request.open('POST', '/workouts/exercises/', false);
  const result = request.send(formData);
  console.log(result);
}

const createExercisesForm = document.getElementById('id_create_exercise_form');

if (createExercisesForm) {
  createExercisesForm.addEventListener('submit', submitCreateExerciseForm);
}
