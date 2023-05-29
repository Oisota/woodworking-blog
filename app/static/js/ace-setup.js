(() => {

	// setup editor
	const editor = ace.edit('editor');
	editor.setTheme('ace/theme/dracula');
	editor.session.setMode('ace/mode/markdown');
	editor.setKeyboardHandler('ace/keyboard/vim');
	editor.setShowPrintMargin(false);
	document.getElementById('editor').style.fontSize='16px';

	// setup form handling
	const form = document.getElementById('post-form');
	form.addEventListener('submit', function(evt) {
		// save editor text to hidden form input so it gets submitted in the form
		form['content'].value = editor.getValue();
	});

	// set editor content to match form
	editor.setValue(form['content'].value);

})();