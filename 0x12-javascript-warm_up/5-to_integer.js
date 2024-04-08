// Convert the first argument to an integer
const num = parseInt(process.argv[2]);

// Check if the conversion resulted in a valid integer
if (num !== NaN) {
    console.log(`My number: ${num}`);
} else {
    console.log("Not a number");
}
