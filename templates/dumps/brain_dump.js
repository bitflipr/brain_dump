function toggleVisibilityOfControl(control_id)
{
  var control = document.getElementById(control_id);
  if (control.style.display == "block" || control.style.display == "")
    control.style.display = "none";
  else
    control.style.display = "block";
}
