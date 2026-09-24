import re

def update_contact():
    with open('contact.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update the form tag
    html = html.replace('<form id="contactForm" data-sb-form-api-token="API_TOKEN">', '<form id="contactForm">')

    # 2. Update the inputs to include name="..." and required, while stripping data-sb attributes
    html = re.sub(
        r'<input class="form-control" id="name" type="text" placeholder="[^"]+" data-sb-validations="[^"]+" />',
        '<input class="form-control" id="name" name="name" type="text" placeholder="Enter your name..." required />',
        html
    )
    
    html = re.sub(
        r'<input class="form-control" id="email" type="email" placeholder="[^"]+" data-sb-validations="[^"]+" />',
        '<input class="form-control" id="email" name="email" type="email" placeholder="name@example.com" required />',
        html
    )

    html = re.sub(
        r'<input class="form-control" id="phone" type="tel" placeholder="[^"]+" data-sb-validations="[^"]+" />',
        '<input class="form-control" id="phone" name="phone" type="tel" placeholder="(123) 456-7890" required />',
        html
    )

    html = re.sub(
        r'<textarea class="form-control" id="message" type="text" placeholder="[^"]+" style="[^"]+" data-sb-validations="[^"]+"></textarea>',
        '<textarea class="form-control" id="message" name="message" type="text" placeholder="Enter your message here..." style="height: 10rem" required></textarea>',
        html
    )

    # 3. Clean up the success message (remove start bootstrap text)
    success_text = """<div class="d-none" id="submitSuccessMessage">
                                        <div class="text-center mb-3">
                                            <div class="fw-bolder">Form submission successful!</div>
                                            To activate this form, sign up at
                                            <br />
                                            <a href="https://startbootstrap.com/solution/contact-forms">https://startbootstrap.com/solution/contact-forms</a>
                                        </div>
                                    </div>"""
                                    
    new_success_text = """<div class="d-none" id="submitSuccessMessage">
                                        <div class="text-center mb-3 text-light">
                                            <div class="fw-bolder text-primary">Message sent successfully!</div>
                                            I will get back to you soon.
                                        </div>
                                    </div>"""
                                    
    # Normalize spaces for regex or just use dotall
    html = re.sub(r'<div class="d-none" id="submitSuccessMessage">.*?</div>\s*</div>', new_success_text, html, flags=re.DOTALL)

    # 4. Enable the submit button
    html = html.replace('class="btn btn-primary btn-lg disabled"', 'class="btn btn-primary btn-lg"')

    # 5. Add custom JS and remove SB forms script
    sb_script = '<script src="https://cdn.startbootstrap.com/sb-forms-latest.js"></script>'
    
    custom_js = """
        <script>
            const form = document.getElementById('contactForm');
            const submitButton = document.getElementById('submitButton');
            const successMessage = document.getElementById('submitSuccessMessage');
            const errorMessage = document.getElementById('submitErrorMessage');
            const scriptURL = 'https://script.google.com/macros/s/AKfycbyr_6GcAOWFlHlRAT-le6zT1I1tRBZgNwv2YRwxAchSx5EyrsbfXKPQpkK_cs-ohH5y/exec';

            if(form) {
                form.addEventListener('submit', e => {
                    e.preventDefault();
                    submitButton.disabled = true;
                    submitButton.innerHTML = 'Sending...';
                    
                    fetch(scriptURL, { method: 'POST', body: new FormData(form) })
                        .then(response => {
                            successMessage.classList.remove('d-none');
                            errorMessage.classList.add('d-none');
                            form.reset();
                            submitButton.disabled = false;
                            submitButton.innerHTML = 'Submit';
                            
                            // Hide success message after 5 seconds
                            setTimeout(() => {
                                successMessage.classList.add('d-none');
                            }, 5000);
                        })
                        .catch(error => {
                            errorMessage.classList.remove('d-none');
                            successMessage.classList.add('d-none');
                            submitButton.disabled = false;
                            submitButton.innerHTML = 'Submit';
                            console.error('Error!', error.message);
                        });
                });
            }
        </script>
"""
    if sb_script in html:
        html = html.replace(sb_script, custom_js)
    else:
        # If it doesn't exist, insert before </body> (though there's already doodle JS there)
        # It's safer to just inject it at the end
        if "const form = document.getElementById('contactForm');" not in html:
            html = html.replace('</body>', custom_js + '\n</body>')

    with open('contact.html', 'w', encoding='utf-8') as f:
        f.write(html)

update_contact()
