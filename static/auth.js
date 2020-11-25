const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

username.addEventListener('change', (event) => {
  const usernameValue = username.value.trim();
  if(usernameValue === '') {
		setErrorFor(username, 'Username cannot be blank');
	}
  else {
  	setSuccessFor(username);
  }
});

if(email) {
	email.addEventListener('change', (event) => {
		const emailValue = email.value.trim();
		if (emailValue === '') {
			setErrorFor(email, 'Email cannot be blank');
		} else if (!isEmail(emailValue)) {
			setErrorFor(email, 'Not a valid email');
		} else {
			setSuccessFor(email);
		}
	})
};

password.addEventListener('change', (event) => {
  const passwordValue = password.value.trim();
  if(passwordValue === '') {
		setErrorFor(password, 'Username cannot be blank');
	} else if(passwordValue.length < 8){
  		setErrorFor(password,'Must be minimum 8 characters');
  }
  else{
  	setSuccessFor(password);
  }
});


if(password2) {
	password2.addEventListener('change', (event) => {
		const passwordValue = password.value.trim();
		const password2Value = password2.value.trim();
		if (passwordValue !== password2Value) {
			setErrorFor(password2, 'Passwords does not match');
		} else {
			setSuccessFor(password2);
		}
	})
};


function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}

function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}