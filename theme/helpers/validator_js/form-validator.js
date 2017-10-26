// validator code
var currentErrors = [];
var inputs = [];
var stopEnter = false;
for (var prop in constraints) {
    var input = document.getElementById(prop)
    inputs.push(input);
    var press = function(e){if(e.keyCode != "9") validateOne(this);}
    input.addEventListener("focus",function(e){this.addEventListener("keyup", press)});
    input.addEventListener("focusout",function(e){e.target.removeEventListener("keyup", press);validateOne(this);});
    if (input.nodeName == "TEXTAREA") {
        input.addEventListener("keydown", function (e) {
            if (e.keyCode == "13") {
                if (e.ctrlKey) {
                    stopEnter = false;
                    var val = this.value;
                    var index = this.selectionStart
                    var begin = val.slice(0, this.selectionStart);
                    var end = val.slice(this.selectionEnd, val.length);
                    this.value = begin + "\n" + end;
                    this.selectionStart = index+1;
                    this.selectionEnd = index+1;
                } else {
                    e.stopImmediatePropagation();
                    stopEnter = true;
                }
            }
        });
        input.addEventListener("keypress", function (e) {
            if (e.keyCode == '13' && stopEnter) {
                e.stopImmediatePropagation();
                for (var i=0; i < inputs.length; i++) {
                    if (this == inputs[i]) {
                        stopEnter = false;
                        inputs[i+1].focus();
                    }
                }
            }
        });
    }
}
document.getElementById("gform").addEventListener("submit", function(e) {
    e.preventDefault();
    var active = document.activeElement;
    var submit_btn = document.querySelector('.gform input[type=submit]');
    for (var i=0; i < inputs.length; i++) {
        if (active == inputs[i]) {
            if (inputs[i] == submit_btn || inputs[i+1] == submit_btn) {
                submit_btn.focus();
                if (isEmpty(validateAll())) success();
            } else {
                inputs[i+1].focus()
            }
        }
    }
});


function validateAll() {
    var errors = {};
    for (var prop in constraints) {
        var err = validateOne(document.getElementById(prop));
        if (!isEmpty(err)) errors[prop] = err
    }
    return errors;
}
function validateOne(input) {
    if (input.preventDefault) input = input.target;
    var err = validate({"value":input.value},{"value":constraints[input.id]}) || {};
    !isEmpty(err) ? errorInput(input, err) : resetInput(input);
    return err;
}
function errorInput (input, error) {
    if (!currentErrors[input.id]) {
        var errDiv = document.createElement("div");
        errDiv.classList.add("err");
        input.parentElement.parentElement.insertBefore(errDiv, input.parentElement);
        currentErrors[input.id] = errDiv;
    }
    currentErrors[input.id].innerText = error.value[0];
    for (var i = 1; i < error.value.length; i++) currentErrors[input.id].innerText += "\n" + error.value[i];
}
function resetInput (input) {
    if (currentErrors[input.id]) {
        currentErrors[input.id].parentElement.removeChild(currentErrors[input.id]);
        delete currentErrors[input.id];
    }
}
function success() {
    document.getElementById("gform").submit();
    document.getElementById("gform").style="display:none;"
    document.getElementById('thank-you').style="display:block";
}
function isEmpty(obj) {
    if (obj == null) return true;
    if (obj.length > 0)    return false;
    if (obj.length === 0)  return true;
    if (typeof obj !== "object") return true;
    var hasOwnProperty = Object.prototype.hasOwnProperty;
    for (var key in obj) if (hasOwnProperty.call(obj, key)) return false;
    return true;
}
