function checkContact() {
  var subject_input = document.getElementById("exampleSubjectInput");
  var message_input = document.getElementById("exampleMessage");
  var alter_message = document.getElementById("alertMessage");
  var name_input = document.getElementById("nameInput");
  if (name_input.value.length == 0){
    alter_message.innerHTML = "Name cannot be empty!";
    return false;
  } else if (subject_input.value.length == 0) {
    alter_message.innerHTML = "Subject cannot be empty!";
    return false;
  } else if (message_input.value.length == 0) {
    alter_message.innerHTML = "Message cannot be empty!";
    return false;
  } else {
    alter_message.innerHTML = "Hi " + name_input.value + ", your message has been sent";
    post(name_input.value, subject_input.value, message_input.value)
    return false;
  }
}

function submitComment() {
  return false;
}

function post(name, subject, message) {
  method = "post";
  var form = document.createElement("form");
  form.setAttribute("method", method);
  form.setAttribute("action", '/email');
  var name_input = document.createElement("input");
  name_input.setAttribute("type", "hidden");
  name_input.setAttribute("name", "name");
  name_input.setAttribute("value", name);
  var subject_input = document.createElement("input");
  subject_input.setAttribute("type", "hidden");
  subject_input.setAttribute("name", "subject");
  subject_input.setAttribute("value", subject);
  var message_input = document.createElement("input");
  message_input.setAttribute("type", "hidden");
  message_input.setAttribute("name", "message");
  message_input.setAttribute("value", message);
  form.appendChild(name_input);
  form.appendChild(subject_input);
  form.appendChild(message_input);
  document.body.appendChild(form);
  form.submit();
}