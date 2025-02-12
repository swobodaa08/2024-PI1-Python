// Spameak Calc

const display = document.getElementById("display");

function appendToDisplay(input){
    display.value += input;

}

function clearDisplay(){
    display.value = "";
}

function calculate(){
    try{
        display.value = eval(display.value);
        last_result = display.value;
    }
    catch(error){
        display.value = "Error";
    }
}

function lastResult(){
    display.value = last_result
}
