let number = Math.floor(Math.random() *10)+1;

function checkGuess() {
    let guess= document.getElementById("guessInput").value;

    if(guess==number)
    {
        printMessage("Congratulations! You guessed the correct number.");
    }
    else if(guess<number)
    {
        printMessage("Your guess is too low. Try again.");
    }
    else
    {
        printMessage("Your guess is too high. Try again.");
    }
}

function printMessage(msg){
    document.getElementById("message").textContent = msg;
}