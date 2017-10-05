function checkContact() {
  var email_input = document.getElementById("exampleEmailInput");
  var subject_input = document.getElementById("exampleSubjectInput");
  var message_input = document.getElementById("exampleMessage");
  var alter_message = document.getElementById("alertMessage");
  if (email_input.value.length == 0) {
    alter_message.innerHTML = "Email cannot be empty";
    return false;
  } else if (subject_input.value.length == 0) {
    alter_message.innerHTML = "Subject cannot be empty!";
    return false;
  } else if (message_input.value.length == 0) {
    alter_message.innerHTML = "Message cannot be empty!";
    return false;
  } else {
    alter_message.innerHTML = "Your message has been sent!";
    return false;
  }
}

function submitComment() {
  return false;
}