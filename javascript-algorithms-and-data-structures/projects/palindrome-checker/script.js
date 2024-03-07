const text_input = document.getElementById('text-input');
const check_button = document.getElementById('check-btn');
const result = document.getElementById('result');

check_button.addEventListener("click", ()=>{
  if(!text_input.value){
    alert('Please input a value');
  } else if (isPalindrome(text_input.value)) {
    result.innerHTML = `<p>${text_input.value} is a palindrome</p>`;
  } else {
    result.innerHTML = `<p>${text_input.value} is not a palindrome</p>`;
  }
});

const isPalindrome = (text) => {
  const cleanText = text.toLowerCase().replace(/[^a-z0-9]/g, '');
  const reversedText = cleanText.split('').reverse().join('');
  return cleanText === reversedText;
};