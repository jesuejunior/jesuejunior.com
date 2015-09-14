::title:: Enviar email do formulario via JS
:date: 2015-08-12
:author: jesuejunior
:category: JS
:tags: js, JS, html, mandrill, sendmail, mail, mail, marketing
:slug: enviando-email-form-com-js


.. code-block:: html

	<form id="subscription" target="_blank" role="form">
		<input id="mc-email" type="email" placeholder="informe seu e-mail">
		<button onclick="sendMail(); return false" type="submit"><span class="icon icon-location"></span></button>
	</form>



.. code-block:: js

	function sendMail() {
		$.ajax({
			type: 'POST',
			url: 'https://mandrillapp.com/api/1.0/messages/send.json',
			data: {
			'key': 'SUA API KEY',
			'message': {
			'from_email': 'SEU@EMAIL.COM',
			'to': [
				{
				'email': 'DESTINATARIO@EMAIL.COM',
				'name': 'RECIPIENT NAME (OPTIONAL)',
				'type': 'to'
				}
				  ],
				'autotext': 'true',
				'subject': 'YOUR SUBJECT HERE!',
				'html': 'YOUR EMAIL CONTENT HERE! YOU CAN USE HTML!'
				}
			  }
		}).done(function(response) {
			console.log(response);
		});
	}